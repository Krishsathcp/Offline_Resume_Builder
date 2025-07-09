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

### 📁 Project Structure

- `offline_resume_builder/` – Core Flask backend application  
  - `app.py` – Main Flask application entry point  
  - `requirements.txt` – Lists all required Python packages  
  - `templates/` – Jinja2 HTML templates for rendering resume UI  
  - `static/` – CSS and JavaScript files  
  - `utils/` – Utility modules: AI engine, PDF generator, formatting tools  
  - `resumes/` – Stores exported resumes (PDF, DOCX)  
  - `temp/` – Temporary storage for HTML previews and draft resumes  
  - `history/` – Tracks generated resumes with timestamped logs  
  - `__init__.py` – Package initializer for Flask module

- `resumes/` – Global folder for storing final generated resumes

- `temp/` – Global folder for temporary HTML/JSON data

- `history/` – Global folder to log generation activities and session info

- `resume_builder.egg-info/` – Metadata files for Python packaging (auto-generated)

- `run_app.bat` – Batch file to start the Flask app (for Windows)

- `setup.py` – Python setup script for packaging and installation

- `pyproject.toml` – Python project metadata (PEP 518)

- `README.md` – Project documentation and usage instructions


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
```

▶️ Step 2: Start the App (Recommended for Windows)
```bash

Double-click run_app.bat
What it does:

Activates the virtual environment

Starts the Flask server

Opens the app at http://localhost:5000
```

💡 Step 3: Enable AI Features (Optional but Powerful)
```bash
Install Ollama

Pull a model (Mistral is preferred):

ollama run mistral
The app connects to http://localhost:11434 and uses this model for:

Resume improvement

Resume scoring

Interview question generation
```

🧪 Developer Notes
```bash
You can modify resume templates under:
offline_resume_builder/templates/

Generated resumes are saved to:
offline_resume_builder/resumes/

Resume scoring and improvement logic is in:
offline_resume_builder/utils/ai_engine.py
```
👨‍💻 Author
Krishsath CP

📬 Contact Me
- 🔗 [LinkedIn](https://www.linkedin.com/in/krishsath-cp-59754532a/)
- 💻 [GitHub](https://github.com/Krishsathcp)
- 📧 Email: cpkrishsath@gmail.com

