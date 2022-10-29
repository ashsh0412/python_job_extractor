from unittest import result
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup   

def get_page_count(name):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless")

    driver = webdriver.Chrome(options=options)
    driver.get(f"https://kr.indeed.com/jobs?q={name}&l=&from=searchOnHP&vjk=1015284880e2ff62")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find('nav', class_ = "css-jbuxu0 ecydgvn0")
    if pagination == None:
        return 1
    pages =pagination.find_all("div", class_ = "css-tvvxwd ecydgvn1", recursive=False)
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count

def extract_job(name):
    pages = get_page_count(name)
    results = []
    for page in range(pages):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.get(f"https://kr.indeed.com/jobs?q={name}&start={page*10}")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_info_containers = soup.find("ul", class_ = "jobsearch-ResultsList css-0")
        jobs = job_info_containers.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_ = "mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_ = "companyName")
                location = job.find('div', class_ = "companyLocation")
                job_data = {
                    'link' : f'https://kr.indeed.com{link}',
                    'company' : company.string.replace(',', ' '),
                    'location' : location.string.replace(',', ' '),
                    'position' : title.replace(',', ' ')
                }
                results.append(job_data)
    return results
