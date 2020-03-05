import requests
from bs4 import BeautifulSoup 
# my second files imports:
import scrapFirstPage
import main 

# Our variables for start page
url = "https://sfbay.craigslist.org/"
shell = ".housing > #sss"
link = "a"
linkText = "span"

# Our variabels for every page 

Pshell = 'li.result-row'
Ptitle = 'a.result-title'
Plink = 'a.result-title'
Pprice = 'span.result-price'
Pdate = '.result-date'










dicti = {}

FirstPage = scrapFirstPage.PageScrap(url, shell, link, linkText)
FirstPage.connect()
dicti = FirstPage.scrap()

main = main.Main(dicti, Pshell, Ptitle, Plink, Pprice, Pdate)
main.takeLinks()
main.main()