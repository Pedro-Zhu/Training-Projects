from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"
result = requests.get(url)

soup = BeautifulSoup(result.content, "html.parser")

data = soup.find(id= "ResultsContainer")
jobs_title = data.find_all("h2", class_="title is-5")

for job in jobs_title:
    print(job.string)


