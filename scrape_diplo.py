from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

url ="https://academic.oup.com/dh/article/43/1/1/5236958"

response = get(url)
print(response.text)

