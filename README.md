# SITBOT - Flask Chatbot

SITBOT is a simple Flask-based college information chatbot.  
It answers common student queries like admissions, fees, courses, placements, hostel, library, scholarships, contact, and location.

## Project Structure

```text
hack-o-week/
|- app.py
|- unanswered.txt
|- static/
|  |- style.css
|  |- logo.png
|- templates/
|  |- index.html
```

## Requirements

- Python 3.8+
- Flask

## Setup and Run (Windows PowerShell)

1. Create a virtual environment:

```powershell
py -m venv .venv
```

2. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Install Flask:

```powershell
py -m pip install flask
```

4. Run the app:

```powershell
py app.py
```

5. Open in browser:

```text
http://127.0.0.1:5000
```

## How It Works

- `GET /` renders `templates/index.html`.
- `POST /get` receives the user message and returns a JSON chatbot reply.
- Unknown questions are logged to `unanswered.txt` for future improvements.

## Notes

- The app runs with `debug=True` in `app.py`, which is useful for development.
- Some reply text currently shows encoding artifacts in terminal/editor output; using UTF-8 consistently will fix emoji/symbol rendering.
