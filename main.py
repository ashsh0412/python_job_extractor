import imp
from tkinter.messagebox import NO
from extractor.indeed import extract_job
from extractor.wwr import wwr_job_scrapper

keyword = input("WHAY DO YOU WANT TO SEARCH?")

indeed = extract_job(keyword)
wwr = wwr_job_scrapper(keyword)

jobs = indeed + wwr

file = open(f"{keyword}.csv", "w", encoding="utf-8")
for job in jobs:
    file.write("Position, Company, Location, URL\n")
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
file.close()    




