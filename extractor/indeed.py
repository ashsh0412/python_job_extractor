from cmath import exp
from selenium import webdriver
from bs4 import BeautifulSoup   
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def get_page_count(name):
    chrom_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(f'./{chrom_ver}/chromedriver.exe')
    except:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrom_ver}/chromedriver.exe')
    driver.get(f"https://kr.indeed.com/jobs?q={name}&l=&from=searchOnHP&vjk=1015284880e2ff62")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find('nav', class_ = "css-jbuxu0 ecydgvn0")
    if pagination == None:
        return 1
    pages =pagination.find_all("div", class_ = "css-tvvxwd ecydgvn1", recursive=False)
    count = len(pages)
    if count >= 5:
        return 1
    else:
        return count

def extract_job(name):
    pages = get_page_count(name)
    results = []
    for page in range(pages):
        chrom_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(f'./{chrom_ver}/chromedriver.exe')
        except:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(f'./{chrom_ver}/chromedriver.exe')
        driver.get(f"https://kr.indeed.com/jobs?q={name}&start={page*10}")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_info_containers = soup.find("ul", class_ = "jobsearch-ResultsList css-0")
        jobs = job_info_containers.find_all('li', recursive=False)
        for job in jobs:
            title = job.find("span") 
            if title != None:
                string_title = title.string
                anchor = job.select_one("h2 a")
                link = anchor['href']
                company = job.find("span", class_ = "companyName")
                location = job.find('div', class_ = "companyLocation")
                job_data = {
                    'link' : f'https://kr.indeed.com{link}',
                    'company' : company.string.replace(',', ' '),
                    'location' : location.string,
                    'position' : string_title
                }
                results.append(job_data)
    return results
                  


