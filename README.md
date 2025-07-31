# CV Matcher App (Updated)

A simple job-matching website:
- Collects name & preferred location
- Uploads a PDF CV
- Extracts content using `pdfplumber`
- Matches against a list of job openings based on keywords & location
- Can be hosted for free using Render

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` to test.

## Deploy for Free
1. Push code to GitHub
2. Connect GitHub repo to [https://render.com](https://render.com)
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
