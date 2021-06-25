from deepface import DeepFace
import face_recognition
import json
import os
import random
import shutil
import pandas as pd
import time
import pickle


website_link = "https://www.cleerdin-hamer.nl/"


dir_link = "./www.cleerdin-hamer.nl/"
# CHECK IF ONE FACE ON IMAGES, REMOVE FILES WITHOUT FACE OR MORE THAN ONE FACE
print("STARTING WITH FACE CHECK")
for image_file in os.listdir(dir_link):
    print(image_file)
    try:
        if os.path.isfile(dir_link + image_file):
            abs_path = os.path.abspath(dir_link + image_file)
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
for image_file in os.listdir(dir_link):
    s1 = str(random.random())
    s1 = s1[-15:]  # take last 15 random figures, so remove the comma
    dict_duplicate_check[image_file] = s1


# SAVE IMAGE WITH IDENTIFICATION NUMBER
print("SAVING IMAGE WITH IDENTIFICATION NUMBER")
extension_list = [".jpeg", ".jpg", ".png", ".gif"]
check_dictionary = {}
counter = len(dict_duplicate_check)
for image_file in dict_duplicate_check:
    counter -= 1
    print(counter, " OF ", len(dict_duplicate_check), "TO GO")
    abs_path_original = os.path.abspath(dir_link + image_file)
    name_new = dict_duplicate_check[image_file]
    if name_new in check_dictionary:
        continue
    for i in extension_list:
        if i in abs_path_original:
            abs_path_new = os.path.abspath(dir_link + name_new + i)
            if not os.path.exists(dir_link):
                os.mkdir(dir_link)
            shutil.copyfile(abs_path_original, abs_path_new)
    check_dictionary[name_new] = None

    # GET SKIN COLOR AND GENDER
    # GET SKIN COLOR AND GENDER
    print("GETTING SKIN COLOR")
    try:
        if os.path.isfile(dir_link + image_file):
            abs_path = os.path.abspath(dir_link + image_file)
        obj = DeepFace.analyze(img_path=abs_path, actions=['gender', 'race', 'emotion'])
        check_dictionary[name_new] = image_file, obj["dominant_race"], obj["gender"], obj["emotion"]
    except Exception as e:
        print("Error in finding skin color and gender")
        print(e)

# SAVE DICTIONARY IN PICKLE
with open(dir_link+'dictionary.pickle', 'wb') as handle:
    pickle.dump(check_dictionary, handle, protocol=pickle.HIGHEST_PROTOCOL)

# CONVERT DICTIONARY TO PANDAS DATAFRAME
df = pd.DataFrame.from_dict(check_dictionary, orient='index')
df = df.rename_axis('ID_number').reset_index()
df = df.rename(columns={0: "Image filename", 1: "Ethnicity", 2: "Gender", 3: "Emotion"})

# SAVE PANDAS DATAFRAME AS CSV FILE
import re

m = re.search('https?://([A-Za-z_0-9.-]+).*', website_link)
print(m.group(1))
website_link = m.group(1)
csv_path = dir_link + "ethnicity_analysis.csv"
df.to_csv(csv_path, index=False)