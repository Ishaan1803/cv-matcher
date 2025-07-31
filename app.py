from flask import Flask, render_template, request
import pdfplumber
import json

app = Flask(__name__)

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages if page.extract_text())

def load_jobs():
    with open('jobs.json', 'r') as f:
        return json.load(f)

def match_jobs(cv_text, location, jobs):
    matched = []
    for job in jobs:
        if location.lower() in job['location'].lower():
            for keyword in job['keywords']:
                if keyword.lower() in cv_text.lower():
                    matched.append(job)
                    break
    return matched

@app.route('/', methods=['GET', 'POST'])
def index():
    matched_jobs = []
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        file = request.files['cv']
        if file and file.filename.endswith('.pdf'):
            cv_text = extract_text_from_pdf(file)
            jobs = load_jobs()
            matched_jobs = match_jobs(cv_text, location, jobs)
    else:
        name = ""
        location = ""
    return render_template('index.html', jobs=matched_jobs)

if __name__ == '__main__':
    app.run(debug=True)
