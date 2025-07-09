@echo off
echo Starting Offline AI Resume Builder...
echo Activating virtual environment...

:: Activate venv (assumes venv is in the root directory)
call "%~dp0venv\Scripts\activate"

:: Navigate to app directory
cd /d "%~dp0offline_resume_builder"

:: Run the app
python app.py

pause
