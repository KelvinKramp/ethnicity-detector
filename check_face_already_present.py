

###############################
# CHECK IF FACE ALREADY PRESENT
# from main import dir_pic

# print("STARTING CHECK DUPLICATES")
#     print("STARTING CHECK DUPLICATES")
#     dict_duplicate_check = {}
#     for image_file in os.listdir("dir_pic"):
#         if image_file in dict_duplicate_check:
#             continue
#         s1 = str(random.random())
#         s1 = s1[-15:] # take last 15 random figures, so remove the comma
#         dict_duplicate_check[image_file] = s1
#         # print(image_file)
#         abs_path = os.path.abspath(".dir_pic"+image_file)
#         for image_file2 in os.listdir(dir_pic):
#             abs_path2 = os.path.abspath(dir_pic + image_file2)
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

# print(dict_duplicate_check)