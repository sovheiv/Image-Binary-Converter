from PIL import Image
import numpy as np
import os
from datetime import datetime


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(str(datetime.now() - start_time).split(":")[2] + " " + func.__name__)

        return result

    return wrapper

@time_decorator
def encrypt_images(input_image_path):
    all_input_images = os.listdir(input_image_path)

    for input_image in all_input_images:

        img = Image.open(input_image_path + "/" + input_image)
        img.load()
        img_array = np.asarray(img, dtype=np.uint8)

        save_str_as_txt(
            text_array_wrapper(gen_str(img_array), img_array.shape[1]), input_image
        )


def gen_str(input_array):

    input_array = np.reshape(input_array, newshape=(-1))
    img_str = ""

    for i in input_array:
        item_str = str(i)
        while len(item_str) < 3:
            item_str = "0" + item_str
        img_str += item_str
    return img_str


def text_array_wrapper(input_array, width):
    width_str = str(width)
    while len(width_str) < 5:
        width_str = "0" + width_str

    img_str = width_str + input_array
    return img_str


def save_str_as_txt(str_data, name, postfix="_encrypted", format = ".txt",  path="encrypted images"):
    os.makedirs(path, exist_ok=True)
    name = name.split(".")[0]
    with open(path + "/" + name + postfix + format, "w") as img_file:
        img_file.write(str_data)


if __name__ == "__main__":

    encrypt_images(input_image_path="image to encrypt")
