import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Iran'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elements = results.find_all('section', class_='card-content')
for element in job_elements:
    title = element.find_all('h2', class_='title')
    company = element.find_all('div', class_='company')
    location = element.find_all('div', class_='location')
    print(title)
    print(company)
    company = element.find_all('div', classmethod)
    print(location, end='\n'*2)