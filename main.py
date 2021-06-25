import os
from backend import loop_list_websites
import json

# Opening JSON file
with open('variables.json') as f:
    data = json.load(f)
list_websites = data.keys()
list_websites = list(list_websites)

# list amsterdam
# be carefull will http and https when filling in the links in tje JSON file

list_websites = ["https://www.example.nl/"]

for i in list_websites:
    ind = i.index("//")
    website_link = i[ind+2:]
    dir_nn = website_link + "pics_id_nr/"
    print(dir_nn)
    dir_pic = website_link + "pics_raw/"
    print(dir_pic)
    if not os.path.exists(website_link):
        os.mkdir(website_link)
    if not os.path.exists(dir_nn):
        os.mkdir(dir_nn)
    if not os.path.exists(dir_pic):
        os.mkdir(dir_pic)
    loop_list_websites(i)


