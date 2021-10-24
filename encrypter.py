from PIL import Image
import numpy as np
import os


def encrypt_images(input_image_path):
    all_input_images = os.listdir(input_image_path)

    for input_image in all_input_images:

        img = Image.open(input_image_path + "/" + input_image)
        img.load()
        img_array = np.asarray(img, dtype=np.uint8)

        print(img_array)
        
        # convert array 

        # gen str and .txt file

if __name__ == "__main__":

    encrypt_images(input_image_path="image to encrypt")
