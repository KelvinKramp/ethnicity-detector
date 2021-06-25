from googlesearch import search
import pandas as pd
import requests

# # def google_search_companies(url):
url = 'https://www.houthoff.com/Search/our-people'
html = requests.get(url).content
df = pd.read_html(html, flavor = 'lxml')
# to search
print(df)
query = "law firm"
L = list(search(query, tld="co.in", num=10, stop=10, pause=2))
website_link = L[0] # get first item in list

from requests_html import HTMLSession
session = HTMLSession()

# r = session.get('https://www.consultancy.nl/nieuws/24501/de-25-grootste-advocatenkantoren-van-nederland')
# print(r.text)