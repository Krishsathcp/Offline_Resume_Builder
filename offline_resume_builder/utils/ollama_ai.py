import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# ------------------------------
def query_llama3(prompt):
    response = requests.post(OLLAMA_API_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")

def generate_ai_resume_sections(skills_text, experience_text, education_text, projects_text, job_description=""):
    prompt = f"""Convert the following raw resume content into professional HTML blocks.

Use <ul><li> for each item. Return in this format:
Skills:
<ul>...</ul>
Experience:
<ul>...</ul>
Education:
<ul>...</ul>
Projects:
<ul>...</ul>

Skills:
\"\"\"{skills_text}\"\"\"

Experience:
\"\"\"{experience_text}\"\"\"

Education:
\"\"\"{education_text}\"\"\"

Projects:
\"\"\"{projects_text}\"\"\"

Job Description (if any):
\"\"\"{job_description}\"\"\"
"""

    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        result = response.json()
        text = result.get("response", "")
        print("\n===== AI Structured Resume Section Response =====")
        print(text)

        if "Skills:" in text:
            text = text.split("Skills:")[1]
            text = "Skills:" + text  

    except Exception as e:
        print("Error from LLaMA for section formatting:", e)
        return {"skills": "", "experience": "", "education": "", "projects": ""}

    def extract_section(title):
        try:
            section = text.split(f"{title}:")[1]
            for other in ["Skills", "Experience", "Education", "Projects"]:
                if other != title and f"{other}:" in section:
                    section = section.split(f"{other}:")[0]
            return section.strip()
        except:
            return ""

    return {
        "skills": extract_section("Skills"),
        "experience": extract_section("Experience"),
        "education": extract_section("Education"),
        "projects": extract_section("Projects")
    }

def generate_ai_resume_content(user_data):
    extra = "\n".join([f"{s.get('heading')}: {s.get('content')}" for s in user_data.get('extra_sections', []) if s.get('heading')])

    prompt = f"""
    You are an AI resume assistant. Based on the user's resume and inputs, improve the professional summary and suggest enhancements.

    Name: {user_data.get('name')}
    Summary: {user_data.get('summary')}
    Skills: {', '.join(user_data.get('skills', []))}
    Experience: {user_data.get('experience')}
    Education: {user_data.get('education')}
    Projects: {user_data.get('projects')}
    User Suggestions: {user_data.get('user_suggestions')}
    Extra Sections:
    {extra}

    Respond in the following format:

    Improved Summary:
    <Your improved professional summary here>

    Suggestions:
    - Suggestion 1
    - Suggestion 2
    """


    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        })

        result = response.json()
        output = result.get("response", "")

        if "Improved Summary:" in output:
            parts = output.split("Improved Summary:")[1].split("Suggestions:")
            ai_summary = parts[0].strip()
            suggestions = "- " + parts[1].strip() if len(parts) > 1 else ""
        else:
            ai_summary = ""
            suggestions = output.strip()

        return {
            "ai_summary": ai_summary,
            "suggestions": suggestions
        }

    except Exception as e:
        print("AI content generation failed:", e)
        return {
            "ai_summary": "",
            "suggestions": ""
        }

def convert_text_to_education_list(edu_text):
    prompt = f"""Convert this education text into a JSON list like:
[
  {{"degree": "B.E. CSE", "institution": "MIT Campus", "years": "2023–2027"}}
]

Text:
\"\"\"{edu_text}\"\"\"
"""
    try:
        res = requests.post(OLLAMA_API_URL, json={"model": MODEL_NAME, "prompt": prompt, "stream": False})
        return json.loads(res.json()["response"])
    except Exception as e:
        print("Education parse error:", e)
        return []

def convert_text_to_experience_list(exp_text):
    prompt = f"""Convert this experience text into a JSON list like:
[
  {{
    "role": "Software Developer",
    "company": "Google",
    "years": "2022–2024",
    "details": ["Developed REST APIs", "Improved system performance"]
  }}
]

Text:
\"\"\"{exp_text}\"\"\"
"""
    try:
        res = requests.post(OLLAMA_API_URL, json={"model": MODEL_NAME, "prompt": prompt, "stream": False})
        return json.loads(res.json()["response"])
    except Exception as e:
        print("Experience parse error:", e)
        return []

def format_experience(experience_list):
    text = ""
    for exp in experience_list:
        text += f"\nRole: {exp.get('role', '')}, Company: {exp.get('company', '')}, Years: {exp.get('years', '')}\n"
        details = exp.get("details", [])
        if isinstance(details, list):
            for d in details:
                text += f"- {d}\n"
    return text
