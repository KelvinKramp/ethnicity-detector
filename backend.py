from deepface import DeepFace
import face_recognition
from scraper import loop_scrape_functions
import json
import os
from get_images import get_images as gi
import random
import shutil
import pandas as pd
import time
import pickle
import re

def loop_list_websites(website_link):
    from main import dir_pic, dir_nn
    # # SCRAPE LINKS
    # Add website link with https in the beginning https://www and / at the end
    print("IN FUNCTION LOOPLISTWEBSITE THE WEBSITE LINK =", website_link)
    loop_scrape_functions(website_link)

    # FUNCTION
    # Create random time interval between 0 and 5 to prevent from getting blocked while scraping
    def rand_sleep_int():
        random_time = str(random.random())
        time_to_sleep = float(random_time)
        time.sleep(time_to_sleep)
        print("waited", time_to_sleep, "seconds")

    # # OPEN JSON FILE WITH LINKS
    with open('data.json') as json_file:
        data = json.load(json_file)


    # # PARSE THROUGH LINKS AND DOWNLOAD IMAGES
    print("STARTING WITH DOWNLOADING IMAGES")
    print(len(data), "to go")
    counter_data = 0
    for link in data:
        counter_data += 1
        # if counter_data == 3:
        #     break
        print("IMAGE DOWNLOAD LOOP NR", counter_data)
        rand_sleep_int()
        # If not crawled through this page start crawling and get links
        gi(link, website_link)



    # CHECK IF ONE FACE ON IMAGES, REMOVE FILES WITHOUT FACE OR MORE THAN ONE FACE
    print("STARTING WITH FACE CHECK")
    for image_file in os.listdir(dir_pic):
        try:
            if os.path.isfile(dir_pic + image_file):
                abs_path = os.path.abspath(dir_pic + image_file)
                image = face_recognition.load_image_file(abs_path)
                face_locations = face_recognition.face_locations(image)
                if len(face_locations) != 1:
                    os.remove(abs_path)
        except Exception as e:
            print("Error in checking faces for file")
            print(image_file)
            print(e)


    # GIVE AN IDENTITY NUMBER TO EVERY FACE
    dict_duplicate_check = {}
    for image_file in os.listdir(dir_pic):
        s1 = str(random.random())
        s1 = s1[-15:] # take last 15 random figures, so remove the comma
        dict_duplicate_check[image_file] = s1


    # SAVE IMAGE WITH IDENTIFICATION NUMBER
    print("SAVING IMAGE WITH IDENTIFICATION NUMBER")
    extension_list = [".jpeg", ".jpg", ".png", ".gif"]
    check_dictionary = {}
    counter = len(dict_duplicate_check)
    for image_file in dict_duplicate_check:
        counter -= 1
        print(counter, " OF ", len(dict_duplicate_check), "TO GO")
        abs_path_original = os.path.abspath(dir_pic+image_file)
        name_new = dict_duplicate_check[image_file]
        if name_new in check_dictionary:
            continue
        for i in extension_list:
            if i in abs_path_original:
                abs_path_new = os.path.abspath(dir_nn+name_new+i)
                if not os.path.exists(dir_nn):
                    os.mkdir(dir_nn)
                shutil.copyfile(abs_path_original, abs_path_new)
        check_dictionary[name_new] = None


    # GET SKIN COLOR AND GENDER
        # GET SKIN COLOR AND GENDER
        print("GETTING SKIN COLOR")
        try:
            if os.path.isfile(dir_pic + image_file):
                abs_path = os.path.abspath(dir_pic + image_file)
            obj = DeepFace.analyze(img_path=abs_path, actions=['gender', 'race', 'emotion'])
            check_dictionary[name_new] = image_file, obj["dominant_race"], obj["gender"], obj["emotion"]
        except Exception as e:
            print("Error in finding skin color and gender")
            print(e)


    # CONVERT DICTIONARY TO PANDAS DATAFRAME
    df = pd.DataFrame.from_dict(check_dictionary, orient='index')
    df = df.rename_axis('ID_number').reset_index()
    df = df.rename(columns={0:"Image filename", 1: "Ethnicity", 2:"Gender", 3:"Emotion"})

    # SAVE PANDAS DATAFRAME AS CSV FILE AND DICTIONARY AS PICKLE FILE
    m = re.search('https?://([A-Za-z_0-9.-]+).*', website_link)
    print(m.group(1))
    website_link = m.group(1)
    with open(website_link + '/dictionary.pickle', 'wb') as handle:
        pickle.dump(check_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)
    csv_path = website_link+"/ethnicity_analysis.csv"
    df.to_csv(csv_path,index=False)