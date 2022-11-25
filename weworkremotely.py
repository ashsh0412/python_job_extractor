from bs4 import BeautifulSoup
import requests

def wework_scrapper(term):
  result = []
  URL = f'https://weworkremotely.com/remote-jobs/search?term={term}&button='
  request = requests.get(URL)
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('ul')
    for job in jobs:
      lies = job.find_all("li")
      for li in lies:
        title = li.find('span', class_ = "title")
        company = li.find('span', class_ = "company")
        region = li.find('span', class_ = "region company")
        links = li.find("a", href=lambda href: href and f"remote-jobs" in href)
        if links != None:
         href = links['href']
        if title and company and region != None:
          value = {
            "title" : title.string.replace(",", " "),
            "company" : company.string.replace(",", " "),
            "location" : region.string.replace(",", " "),
            "link" : f"https://weworkremotely.com/{href}"
          }
          result.append(value)
  return result




            

