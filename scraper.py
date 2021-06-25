import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import validators
import time
import random
# NOTES
# How to prevent yourself from getting blocked while scraping
# https://www.scraperapi.com/blog/5-tips-for-web-scraping/

# FUNCTION
# Create random time interval between 0 and 5 to prevent from getting blocked while scraping
def rand_sleep_int():
    random_time = str(random.random())
    time_to_sleep = float(random_time)
    time.sleep(time_to_sleep)

# DEFINE FUNCTIONS
def getdata(url):
    r = requests.get(url)
    return r.text


def get_links(website_link):
    rand_sleep_int()
    html_data = getdata(website_link)
    try:
        soup = BeautifulSoup(html_data, "html.parser")
    except TypeError as e:
        print("URL DOES NOT REFER TO AN HTML FILE")
        return {}
    # print(soup)
    list_links = []
    counter = 0
    for link in soup.find_all("a", href=True):
        # test1 = validators.url(link["href"])
        # test2 = validators.url(website_link+"/"+link["href"])
        # Append to list if new link contains original link
        if str(link["href"]).startswith((str(website_link))):
            list_links.append(link["href"])
        # Skip links to other websites
        elif ("https") in str(link["href"]):
            continue

        # Include all href that do not start with website link and attach website link
        if str(link["href"]).startswith("/"):
            if link["href"] not in dict_href_links:
                print(link["href"])
                dict_href_links[link["href"]] = None
                # If the homepage = something.com/en/ but the subpages are something.com/subpagelink
                with open('variables.json') as f:
                    data = json.load(f)
                website = website_link
                print(website)
                if website.count("/") > 3:
                    ind = website[:-1].rfind("/",)
                    website = website[:(ind+1)]
                link_with_www = website + link["href"][1:]
                print("adjusted link =", link_with_www)
                list_links.append(link_with_www)
            # print(link["href"])
        # elif validators.url(website_link+"/"+link["href"]):
        #     list_links.append(website_link+"/"+link["href"])
        # Append to list if link is an url
        # elif (test1 == True) or (test2 == True):
        # elif validators.url(website_link+"/"+link["href"]):
        #     # Take the first character ("/") of the link string and concatenate with website link if slash present at start of link
        #     if link["href"][0] == "/":
        #         link_with_www = website_homepage_link + link["href"][1:]
        #     else:
        #         link_with_www = website_homepage_link + link["href"]
        #     list_links.append(link_with_www)
    # Convert list of links to dictionary and define keys as the links and the values as "Not-checked"
    dict_links = dict.fromkeys(list_links, "Not-checked")
    return dict_links


def get_subpage_links(l):
    counter = 0
    for link in tqdm(l):
        counter += 1
        # if counter ==3:
        #     break
        # If not crawled through this page start crawling and get links
        if l[link] == "Not-checked":
            dict_links_subpages = get_links(link)
            # Change the dictionary value of the link to "Checked"
            l[link] = "Checked"
        else:
            # Create an empty dictionary in case every link is checked
            dict_links_subpages = {}
        # Add new dict to old dictionary
        l = {**dict_links_subpages, **l}
    return l

def loop_scrape_functions(website):
    global dict_href_links
    dict_href_links = {}
    # create dictionary of website
    global dict_links
    dict_links = {website: "Not-checked"}
    global website_homepage_link
    website_homepage_link = website
    # create counters
    counter, counter2 = None, 0
    # start while loop
    while counter != 0:
        counter2 += 1
        limit = 500
        if counter2 == limit:
            print("LINK SEARCH LOOP STOPPED: ", limit, " PAGES REACHED")
            break

        print("IN FUNCTION LOOP SCRAPE FUNCTION", dict_links)
        dict_links2 = get_subpage_links(dict_links)
        # Count number of non-values and set counter to 0 if there are no values within the dictionary equal to the string "Not-checked"
        # https://stackoverflow.com/questions/48371856/count-the-number-of-occurrences-of-a-certain-value-in-a-dictionary-in-python
        counter = sum(value == "Not-checked" for value in dict_links2.values())
        # Print some statements
        print("")
        print("THIS IS SUBPAGE CHECK LOOP ITERATION NUMBER", counter2)
        print("LENGTH OF DICTIONARY WITH LINKS =", len(dict_links2))
        print("NUMBER OF 'Not-checked' LINKS = ", counter)
        print("")
        dict_links = dict_links2
        # Save list in json file
        a_file = open("data.json", "w")
        json.dump(dict_links, a_file)
        a_file.close()
        rand_sleep_int()


