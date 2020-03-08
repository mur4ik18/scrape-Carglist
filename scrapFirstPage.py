import requests
from bs4 import BeautifulSoup 


class PageScrap():
    def __init__(self, url, shell, link, linkText):
        self.url            = url
        self.shell          = shell
        self.link           = link
        self.linkText       = linkText
#    
    def connect(self):
        # get HTTP 
        r = requests.get(self.url)
        # convert HTTP => html
        self.html = BeautifulSoup(r.content, "html.parser")
    
    def scrap(self):
        self.dict = {}  # write in this dirict categories : links
        for el in self.html.select(self.shell):
            # link
            m = el.find_all(self.link)
            # category
            t = el.find_all(self.linkText, attrs = {'class' : 'txt'})   
            for el in range(0, len(m)):
                # write links in list
                self.dict[t[el].get_text()]='https://sfbay.craigslist.org' + m[el].get('href')      
        return self.dict  
