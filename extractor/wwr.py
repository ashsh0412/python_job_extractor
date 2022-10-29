from requests import get
from bs4 import BeautifulSoup

def wwr_job_scrapper(keyword):
    URL = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    responses = get(f"{URL}{keyword}")
    if responses.status_code != 200:
        print("WEBSITE IS NOT AVAILABLE")
    else:
        result = []
        print(f"SEARCHING {keyword}")
        soup = BeautifulSoup(responses.text, "html.parser")
        contents = soup.find_all('li', class_ = "feature")
        for content in contents:
            job_information = content.find_all('a')
            features = job_information[1]
            companies, times, regions = features.find_all("span", class_ = 'company')
            company_links = features['href']
            titles = features.find('span', class_ = "title")
            https = "https://weworkremotely.com"
            job_data = {
                'link' : f"{https}{company_links}",
                'company' : companies.string.replace(',', ' '),
                'location'  : regions.string.replace(',', ' '),
                'position' : titles.string.replace(',', ' ')
            }
            result.append(job_data)
        return result






