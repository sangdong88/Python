#웹 크롤링

import bs4
import urllib
from urllib.request import Request

url = "https://naver.com"
web_page = urllib.request.urlopen(url)


html_text = bs4.BeautifulSoup(web_page,"html.parser")
html_text.find('li',class_='ah_time')
