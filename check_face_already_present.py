
###############################
# CHECK IF FACE ALREADY PRESENT
# try:
#     print("STARTING CHECK DUPLICATES")
#     dict_duplicate_check = {}
#     for image_file in os.listdir("./Pictures"):
#         if image_file in dict_duplicate_check:
#             continue
#         s1 = str(random.random())
#         s1 = s1[-15:] # take last 15 random figures, so remove the comma
#         dict_duplicate_check[image_file] = s1
#         # print(image_file)
#         abs_path = os.path.abspath("./Pictures/"+image_file)
#         for image_file2 in os.listdir("./Pictures"):
#             abs_path2 = os.path.abspath("./Pictures/" + image_file2)
#             if abs_path != abs_path2:
#                 # print("Checking pictures")
#                 # finetune the threshold max_treshold_to_verify value https://sefiks.com/2020/05/22/fine-tuning-the-threshold-in-face-recognition/
#                 # the study shows a optimal threshold of 0.3147 calculated with decision tree
#                 result = DeepFace.verify(abs_path, abs_path2, model_name="VGG-Face")
#                 # print(result)
#                 if result["verified"] == True:
#                     print("SAME FACE FOUND")
#                     dict_duplicate_check[image_file2] = s1
#                 else:
#                     pass
# except Exception as e:
#     print(e)
#
# print(dict_duplicate_check)
#
# print("STARTING CHECK DUPLICATES")
# try:
#     print("STARTING CHECK DUPLICATES")
#     dict_duplicate_check = {}
#     for image_file in os.listdir("./Pictures"):
#         if image_file in dict_duplicate_check:
#             continue
#         s1 = str(random.random())
#         s1 = s1[-15:] # take last 15 random figures, so remove the comma
#         dict_duplicate_check[image_file] = s1
#         # print(image_file)
#         abs_path = os.path.abspath("./Pictures/"+image_file)
#         for image_file2 in os.listdir("./Pictures"):
#             abs_path2 = os.path.abspath("./Pictures/" + image_file2)
#             if abs_path != abs_path2:
#                 # print("Checking pictures")
#                 # finetune the threshold max_treshold_to_verify value https://sefiks.com/2020/05/22/fine-tuning-the-threshold-in-face-recognition/
#                 # the study shows a optimal threshold of 0.3147 calculated with decision tree
#                 result = DeepFace.verify(abs_path, abs_path2, model_name="Facenet")
#                 # print(result)
#                 if result["verified"] == True:
#                     print("SAME FACE FOUND")
#                     dict_duplicate_check[image_file2] = s1
#                 else:
#                     pass
# except Exception as e:
#     print(e)
#
# print(dict_duplicate_check)
#
# print("STARTING CHECK DUPLICATES")
# try:
#     print("STARTING CHECK DUPLICATES")
#     dict_duplicate_check = {}
#     for image_file in os.listdir("./Pictures"):
#         if image_file in dict_duplicate_check:
#             continue
#         s1 = str(random.random())
#         s1 = s1[-15:] # take last 15 random figures, so remove the comma
#         dict_duplicate_check[image_file] = s1
#         # print(image_file)
#         abs_path = os.path.abspath("./Pictures/"+image_file)
#         for image_file2 in os.listdir("./Pictures"):
#             abs_path2 = os.path.abspath("./Pictures/" + image_file2)
#             if abs_path != abs_path2:
#                 # print("Checking pictures")
#                 # finetune the threshold max_treshold_to_verify value https://sefiks.com/2020/05/22/fine-tuning-the-threshold-in-face-recognition/
#                 # the study shows a optimal threshold of 0.3147 calculated with decision tree
#                 result = DeepFace.verify(abs_path, abs_path2, model_name="OpenFace")
#                 # print(result)
#                 if result["verified"] == True:
#                     print("SAME FACE FOUND")
#                     dict_duplicate_check[image_file2] = s1
#                 else:
#                     pass
# except Exception as e:
#     print(e)
#
# print(dict_duplicate_check)
#
# print("STARTING CHECK DUPLICATES")
# try:
#     print("STARTING CHECK DUPLICATES")
#     dict_duplicate_check = {}
#     for image_file in os.listdir("./Pictures"):
#         if image_file in dict_duplicate_check:
#             continue
#         s1 = str(random.random())
#         s1 = s1[-15:] # take last 15 random figures, so remove the comma
#         dict_duplicate_check[image_file] = s1
#         # print(image_file)
#         abs_path = os.path.abspath("./Pictures/"+image_file)
#         for image_file2 in os.listdir("./Pictures"):
#             abs_path2 = os.path.abspath("./Pictures/" + image_file2)
#             if abs_path != abs_path2:
#                 # print("Checking pictures")
#                 # finetune the threshold max_treshold_to_verify value https://sefiks.com/2020/05/22/fine-tuning-the-threshold-in-face-recognition/
#                 # the study shows a optimal threshold of 0.3147 calculated with decision tree
#                 result = DeepFace.verify(abs_path, abs_path2, model_name="DeepFace")
#                 # print(result)
#                 if result["verified"] == True:
#                     print("SAME FACE FOUND")
#                     dict_duplicate_check[image_file2] = s1
#                 else:
#                     pass
# except Exception as e:
#     print(e)
#
# print(dict_duplicate_check)