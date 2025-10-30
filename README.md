# Student Performance Tracker (Flask)

## What this project is
A Flask web app to add students, add subjects, enter marks (out of 100), and automatically calculate total, average and grade. Includes templates and simple UI.

## Files to submit
- `app.py` — main Flask application
- `templates/` — folder with HTML templates (index, add_student, add_subject, add_marks)
- `requirements.txt` — Python dependencies
- `Procfile` — for Heroku deployment
- `README.md` — this file

## How to run locally (Windows)
1. Open VS Code and open this project folder.
2. Activate virtual environment:
   - PowerShell: `.\venv\Scripts\Activate.ps1`
   - CMD: `.\venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open browser: `http://127.0.0.1:5000`

## How to test features
- Add Student → Add a student (name + roll)
- Add Subject → Add any new subject (e.g., History)
- Add / Update Marks → Enter marks 0–100 for each subject
- The Index page shows Subjects (out of 100), Total (e.g. 280/300), Average, and Grade


