import requests
from bs4 import BeautifulSoup 
# my second files imports:
import scrapFirstPage
 
# Our variables
url = "https://sfbay.craigslist.org/"
shell = ".community > #ccc"
link = "a"


FirstPage = scrapFirstPage.PageScrap(url, shell, link)
html = FirstPage.connect()
