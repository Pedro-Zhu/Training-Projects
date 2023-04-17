from bs4 import BeautifulSoup
import requests

url = "https://nhentai.net"
result = requests.get(url)

soup = BeautifulSoup(result.content, "html.parser")

data = soup.find(class_= "gallery")
codes = data.find_all("a", href= True)

for code in codes:
    print(code.string)

