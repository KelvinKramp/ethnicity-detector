import re
import requests
from bs4 import BeautifulSoup
import os

response = requests.get("https://www.nautadutilh.com/nl/medewerkers?expertise=77&glossary=S")
soup = BeautifulSoup(response.text, 'html.parser')
# Find all image files with image stored in scrset  tag in html and add to third list
article_class_persons = soup.find_all(attrs = {"srcset": True})
try:
    # urls = [a_class_member['data-bg-member'] for a_class_member in article_class_persons]
    file_name_counter = 0
    for url in article_class_persons:
        url = str(url)
        file_name_counter += 1 # /<[^\>]*[^\>\S]+srcset=['"]((?:[^"'\s,]+\s*(?:\s+\d+[wx])(?:,\s*)?)+)["']/gm
        url = re.search(r"""((?:[^"'\s,]+\s*(?:\s+\d+[wx])(?:,\s*)?)+)""",
                        url)
        url = url.group(0)
        url = url.split(",")[0]
        url = url[:-3]
        url = website_link[:-1] + url
        filename = re.search(r'/([^\/]+(jpg|gif|jpeg|png))', url)
        if filename is not None:
            if not os.path.isfile(path + filename.group(0)[1:]):
                with open(path + filename.group(0)[1:], 'wb') as f:
                    if url.lower().startswith("http"):
                        response = requests.get(url)
                    else:
                        response = requests.get(website_link + url)
                    f.write(response.content)
                # print(link)
                # print(url)
                print("FILE", url, " SAVED")
except Exception as e:
    print("NO AVATAR TAGGED IMAGES FOUND ON THIS PAGE")
    print(e)