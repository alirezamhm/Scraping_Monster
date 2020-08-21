import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Iran'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
job_elements = results.find_all('section', class_='card-content')
for element in job_elements:
    title = element.find('h2', class_='title')
    company = element.find('div', class_='company')
    location = element.find('div', class_='location')
    if not (title and company and location):
        continue
    link = element.find('a')['href']
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print(link)
    print()