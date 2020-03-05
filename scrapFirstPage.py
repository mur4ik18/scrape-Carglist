import requests
from bs4 import BeautifulSoup 


class PageScrap():
    def __init__(self, url, shell, link, linkText):
        self.url = url
        self.shell = shell
        self.link = link
        self.linkText = linkText
#    
    def connect(self):
        r = requests.get(self.url)
        self.html = BeautifulSoup(r.content, "html.parser")
    
    def scrap(self):
        self.dict = {}
        for el in self.html.select(self.shell):
            m = el.find_all(self.link)
            t = el.find_all(self.linkText, attrs = {'class' : 'txt'})   
            for el in range(0, len(m)):
                self.dict[t[el].get_text()]='https://sfbay.craigslist.org' + m[el].get('href')
                print(t[el].get_text())
        
        print(len(m))
        print(self.dict)