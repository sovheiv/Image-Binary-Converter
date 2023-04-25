import os
from datetime import datetime

import numpy as np
from PIL import Image


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(str(datetime.now() - start_time).split(":")[2] + " " + func.__name__)

        return result

    return wrapper


@time_decorator
def encrypt_images(input_image_path, intermediate_save=False):
    all_input_images = os.listdir(input_image_path)
    print(f"Start encrypting all")

    for input_image in all_input_images:
        print(f"{input_image} encrypting started")

        img = Image.open(input_image_path + "/" + input_image)
        img.load()
        img_array = np.asarray(img, dtype=np.uint8)

        if intermediate_save:
            save_intermediate(input_image, img_array)

        img_numbers = text_array_wrapper(gen_str(img_array), img_array.shape[1])
        save_str_as_txt(convert_to_binary(img_numbers), input_image)


@time_decorator
def convert_to_binary(input_string):
    binary_string_array = [format(int(i), "04b") for i in input_string]
    binary_string = "".join(binary_string_array)
    return binary_string


@time_decorator
def gen_str(input_array):
    input_array = np.reshape(input_array, newshape=(-1))
    img_str = ""

    for i in input_array:
        item_str = str(i)
        while len(item_str) < 3:
            item_str = "0" + item_str
        img_str += item_str
    return img_str


@time_decorator
def text_array_wrapper(input_array, width):
    width_str = str(width)
    while len(width_str) < 5:
        width_str = "0" + width_str

    img_str = width_str + input_array
    return img_str


@time_decorator
def save_str_as_txt(
    str_data, name, postfix="_encrypted", format=".txt", path="encrypted_images"
):
    os.makedirs(path, exist_ok=True)
    name = name.split(".")[0]
    with open(path + "/" + name + postfix + format, "w") as img_file:
        img_file.write(str_data)


def save_intermediate(name, img_array, path="intermediate_arrays"):
    os.makedirs(path, exist_ok=True)
    img_str = img_array.astype(str)
    img_2d = np.array([[" ".join(pixel) for pixel in row] for row in img_str])

    np.savetxt(
        f'{path}/{name.split(".")[0]}_pixels_2d_array.txt', img_2d, fmt="%-10s", delimiter="|"
    )


if __name__ == "__main__":
    encrypt_images(input_image_path="image_to_encrypt", intermediate_save=True)
