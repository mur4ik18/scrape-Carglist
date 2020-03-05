import requests
from bs4 import BeautifulSoup

class Main():
    def __init__(self, dicts):
        self.dict = dicts
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
            print(html)