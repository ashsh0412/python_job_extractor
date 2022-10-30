from unicodedata import name
from flask import Flask,render_template,request
from extractor.indeed import extract_job
from extractor.wwr import wwr_job_scrapper

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="sungho")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_job(keyword)
        wwr = wwr_job_scrapper(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run()
