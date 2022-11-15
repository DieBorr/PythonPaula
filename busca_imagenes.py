import cv2
import os 

input_images_path = "/home/diego/Escritorio/python/input_images"
files_names = os.listdir(input_images_path)


for file_name in files_names:
    #print(file_name)
    if '.jpg' in file_name:
        image_path = input_images_path + "/" + file_name
        image = cv2.imread(image_path)

        cv2.imshow("Image", image)
        cv2.waitKey(0)
    else:
        print(file_name)
        continue

