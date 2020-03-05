import requests
from bs4 import BeautifulSoup 


class PageScrap():
    def __init__(self, url, shell, link):
        self.url = url
        self.shell = shell
        self.link = link
#    
    def connect(self):
        r = requests.get(self.url)
        self.html = BeautifulSoup(r.content, "html.parser")
    
    def scrap(self):
        for el in self.html.select(self.shell):
            print(el.find_all(self.link))

