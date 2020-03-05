import requests
from bs4 import BeautifulSoup 


class PageScrap():
    def __init__(self, url, shell, link):
        self.url = url
        self.shell = shell
        self.link = link
    
    def connect(self):
        r = requests.get(self.url)
        html = BeautifulSoup(r.contet, "html.parser")
        return html
    
    def scrap(self , html):
        

