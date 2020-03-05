import requests
from bs4 import BeautifulSoup

class Main():
    def __init__(self, dicts, shell, title, link, price, date):
        self.dict = dicts
        self.shell = shell
        self.title = title
        self.link = link
        self.price = price 
        self.date = date






# getting all ours links
    def takeLinks(self):
        self.links = []
        for i in self.dict:
            self.links.append(self.dict[i])
        print(self.links)

    def main(self):
        for i in range(0 , len(self.links)):
            url = self.links[i]
            r = requests.get(url)
            html = BeautifulSoup(r.content, "html.parser")
            print(self.links[i])
            #print(html)

            for el in html.select(self.shell):
                title = el.select(self.title)
                link = el.select(self.title)
                price = el.select(self.price)
                date = el.select(self.date)

                print("------------------------------------")
                print(date[0].text)
                print(link[0].get('href'))
                print(title[0].text)
                print(price[0].text)
