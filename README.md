🧠 Offline AI Resume Builder

A powerful **offline resume generation system** built with Python and Flask. Users can **create**, **customize**, **score**, and **export** resumes using **AI-powered enhancements (via Mistral/Ollama)** — all without needing an internet connection.

---

🚀 Features

- ✨ Build resumes in **multiple templates** (formal, casual, modern)
- 📤 Export as **PDF**, **DOCX**, or **HTML**
- 🔍 Get **AI-generated feedback and scores** (Grammar, Clarity, Impact)
- 🛠 Improve resume using **Mistral (offline LLM)** via Ollama
- 🗂️ View and manage **resume history**
- 🔒 100% **offline** functionality (no cloud dependencies)
- 📦 Portable and **easy to run on Windows** (via batch script)

---

🛠️ Tech Stack

| Layer         | Technology Used                   |
|---------------|------------------------------------|
| Backend       | 🐍 Python 3.10+, Flask             |
| Templates     | 🧩 Jinja2 (HTML Templates)         |
| AI Engine     | 🧠 Ollama + Mistral (local model) |
| Resume Export | 📄 `python-docx`, `pdfkit`        |
| Frontend      | 🎨 HTML5 + CSS + JS               |
| Scripts       | 🖱️ Batch files (.bat) for launching|

---

📁 Project Folder Structure

offline-resume-builder/
│
├── run_app.bat # Batch script to start app (Windows only)
├── setup.py # For packaging the app
├── pyproject.toml # Python project metadata
├── README.md # You’re reading this :)
│
├── offline_resume_builder/
│ ├── app.py # Main Flask application
│ ├── requirements.txt # Required Python packages
│ ├── templates/ # HTML Templates (Jinja2)
│ ├── static/ # CSS and JS files
│ ├── utils/ # AI engine, PDF builder, resume tools
│ ├── resumes/ # Exported resumes (PDF/DOCX)
│ ├── temp/ # Temporary files for preview/download
│ ├── history/ # Stores resume creation logs
│ └── init.py
│
├── resumes/ # Global output resume folder
├── temp/ # Global temp HTML cache
├── history/ # Resume generation logs
└── resume_builder.egg-info/ # Python packaging metadata

yaml
Copy
Edit

---

🧰 Prerequisites

Make sure you have the following installed:

- ✅ Python 3.10 or later
- ✅ pip package manager
- ✅ [Ollama](https://ollama.com/download) (for local AI)
- ✅ Optional: [wkhtmltopdf](https://wkhtmltopdf.org/) (for PDF conversion)

---

⚙️ Installation & Running the App

🔧 Step 1: Set up virtual environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r offline_resume_builder/requirements.txt
▶️ Step 2: Start the App (Recommended for Windows)
bash
Copy
Edit
Double-click run_app.bat
What it does:

Activates the virtual environment

Starts the Flask server

Opens the app at http://localhost:5000

💡 Step 3: Enable AI Features (Optional but Powerful)
Install Ollama

Pull a model (Mistral is preferred):

bash
Copy
Edit
ollama run mistral
The app connects to http://localhost:11434 and uses this model for:

Resume improvement

Resume scoring

Interview question generation

🧪 Developer Notes
You can modify resume templates under:
offline_resume_builder/templates/

Generated resumes are saved to:
offline_resume_builder/resumes/

Resume scoring and improvement logic is in:
offline_resume_builder/utils/ai_engine.py
```
👨‍💻 Author
Krishsath CP

🔗 LinkedIn

💻 GitHub

📧 Email: cpkrishsath@gmail.com

