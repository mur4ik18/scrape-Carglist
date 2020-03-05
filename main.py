import requests
from bs4 import BeautifulSoup

class Main():
    def __init__(self, dicts):
        self.dict = dicts

    def takeLinks(self):
        self.links = []
        for i in self.dict:
            self.links.append(self.dict[i])
        print(self.links)