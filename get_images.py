import re
import requests
from bs4 import BeautifulSoup
import os
# from backend import dir_pic

def get_images(link, website_link):
    site = link
    response = requests.get(site)
    m = re.search('https?://([A-Za-z_0-9.-]+).*', website_link)
    print(m.group(1))
    website_link = m.group(1)
    dir_pic = website_link + "/pics_raw/"
    # Create new directory
    parent_dir = str(os.getcwd())
    path = os.path.join(parent_dir, dir_pic)
    if not os.path.exists(path):
        os.mkdir(path)

    # Find all image files with image tags in html and add to list
    try:
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        print("could not parse url for downloadable image due to following error")
        print(e)
        return
    img_tags = soup.find_all('img')
    try:
        urls = [img['src'] for img in img_tags]
    # Parse list and download image if ends with jpg,gif, jpeg or png
        for url in urls:
            filename = re.search(r'/([^\/]+(jpg|gif|jpeg|png))$', url)
            if filename is not None:
                if not os.path.isfile(path + filename.group(0)[1:]):
                    with open(path+filename.group(0)[1:], 'wb') as f:
                        if url.lower().startswith("http"):
                            response = requests.get(url)
                        else:
                            response = requests.get(website_link+url)
                        f.write(response.content)
                # print(link)
                # print(url)
                    print("FILE", filename.group(0)[1:], " SAVED")

    except Exception as e:
        print("NO IMG TAGGED IMAGES FOUND ON THIS PAGE")
        print(e)

    # Find all image files with avatar tag in html and add to second list
    avatars = soup.find_all("div", {"class": "avatar"})
    try:
        urls = [avatar['style'] for avatar in avatars]
        file_name_counter = 0
        for url in urls:
            file_name_counter += 1
            url = re.search(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',
                                 url)
            url = url.group(0)
            filename = re.search(r'/([^\/]+(jpg|gif|jpeg|png))$', url)
            if filename is not None:
                if not os.path.isfile(path + filename.group(0)[1:]):
                    with open(path+filename.group(0)[1:], 'wb') as f:
                        if url.lower().startswith("http"):
                            response = requests.get(url)
                        else:
                            response = requests.get(website_link+url)
                        f.write(response.content)
                    # print(link)
                    # print(url)
                    print("FILE", url, " SAVED")
    except Exception as e:
        print("NO AVATAR TAGGED IMAGES FOUND ON THIS PAGE")
        print(e)

    # Find all image files with avatar tag in html and add to second list
    a_class_members = soup.find_all("a", {"class": "member"})
    try:
        urls = [a_class_member['data-bg-member'] for a_class_member in a_class_members]
        file_name_counter = 0
        for url in urls:
            file_name_counter += 1
            url = re.search(r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',
                            url)
            url = url.group(0)
            filename = re.search(r'/([^\/]+(jpg|gif|jpeg|png))$', url)
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

    # Find all image files with image stored in scrset  tag in html and add to third list
    article_class_persons = soup.find_all(attrs={"srcset": True})
    try:
        # urls = [a_class_member['data-bg-member'] for a_class_member in article_class_persons]
        file_name_counter = 0
        for url in article_class_persons:
            url = str(url)
            file_name_counter += 1  # /<[^\>]*[^\>\S]+srcset=['"]((?:[^"'\s,]+\s*(?:\s+\d+[wx])(?:,\s*)?)+)["']/gm
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
                    print("FILE", url, " SAVED")
    except Exception as e:
        print("NO AVATAR TAGGED IMAGES FOUND ON THIS PAGE")
        print(e)