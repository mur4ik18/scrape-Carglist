import requests
from bs4 import BeautifulSoup 
# my second files imports:
import scrapFirstPage
 
# Our variables
url = "https://sfbay.craigslist.org/"
shell = ".community > #ccc"
link = "a"
linkText = "a > span"


FirstPage = scrapFirstPage.PageScrap(url, shell, link, linkText)
FirstPage.connect()
FirstPage.scrap()

"""
dicte = {}
for i in range(0, 10):
    dicte[i]= 'pie'+ str(i)
print(dicte)
"""