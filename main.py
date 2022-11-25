from flask import Flask, render_template,request, redirect,send_file
from remoteok import extract_jobs
from weworkremotely import wework_scrapper
from file import save_to_file

app = Flask("Jobscarpper")

db = {}

@app.route("/")
def home():
  return render_template("index.html",)

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else:
    result1 = extract_jobs(keyword)
    result2 = wework_scrapper(keyword)
    jobs = result1 + result2
    db[keyword] = jobs
  return render_template("search.html", keyword = keyword, jobs = jobs)


@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")
