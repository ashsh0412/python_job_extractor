from bs4 import BeautifulSoup
import requests


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            links = job.find('a', class_ = "preventLink")
            link = links['href']
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            if company:
                company = company.string.strip().replace(",", " ")
            if position:
                position = position.string.strip().replace(",", " ")
            if location:
                location = location.string.strip().replace(",", " ")

            if company and position and location:
                job = {
                    'company': company,
                    'title': position,
                    'location': location,
                    'link': f'https://remoteok.com{link}'
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results

