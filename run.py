import requests
from bs4 import BeautifulSoup 
# my second files imports:
import scrapFirstPage
import main 

# Our variables for start page
url = "https://sfbay.craigslist.org/"
shell = ".community > #ccc"
link = "a"
linkText = "span"

dicti = {}

FirstPage = scrapFirstPage.PageScrap(url, shell, link, linkText)
FirstPage.connect()
dicti = FirstPage.scrap()

main = main.Main(dicti)
main.takeLinks()