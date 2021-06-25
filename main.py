import os
from backend import loop_list_websites
import json
import shutil


# Opening JSON file
with open('variables.json') as f:
    data = json.load(f)
list_websites = data.keys()
list_websites = list(list_websites)
# www.boelszanders.com -> image downloader naar avatar tag aangepast "https://www.boelszanders.nl/":  "None",
# www.nautadutilh.com -> image downloader naar scrset tag aangepast

# list amsterdam
# https://legalista.nl/adviseurs/categorie/amsterdam-advocaten
#
# https://akoost.nl/onze-advocaten
# http://www.akan.nl/advocaten/
# https://www.amsadvocaten.nl/de-advocaten/
# https://baarsjes-advocaten.nl/
# https://www.brantjesadvocaten.nl/
# https://cleerdin-hamer.nl/amsterdam/
# https://vandoorncs.nl/advocaten/
# https://eisenmann.org/advocaten/
# https://www.vanessen-advocaat.nl/
# https://www.ficqadvocaten.nl/advocaten/
# be carefull will http and https when filling in the links in tje JSON file

list_websites = ["https://www.alpha-advocaten.nl/"]

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


