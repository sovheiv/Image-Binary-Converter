import os
import numpy as np
from PIL import Image
from datetime import datetime


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print(str(datetime.now() - start_time).split(":")[2] + " " + func.__name__)

        return result

    return wrapper


@time_decorator
def decode_image(encrypted_image_path):

    all_input_images = os.listdir(encrypted_image_path)

    for input_image in all_input_images:
        img_binary_text = open(encrypted_image_path + "/" + input_image, "r").read()
        img_text = convert_from_binary_to_decimal(img_binary_text)
        save_image(convert_to_array(img_text), input_image)


@time_decorator
def convert_from_binary_to_decimal(input_binary_text):
    input_binary_array = np.array(list(input_binary_text))
    input_binary_array = input_binary_array.reshape(-1, 4)
    img_text_array = [str(int("".join(item), 2)) for item in input_binary_array]
    img_text = "".join(img_text_array)
    return img_text


@time_decorator
def convert_to_array(input_str_data):
    img_char_array = list(input_str_data)
    width_str = ""

    for i in range(5):
        width_str += img_char_array[0]
        img_char_array.pop(0)

    width = int(width_str)

    img_str_array = np.array(img_char_array, dtype=str)
    img_str_array = img_str_array.reshape(-1, 3)

    img_array = np.array([int("".join(item)) for item in img_str_array], dtype=np.uint8)
    img_array = img_array.reshape(-1, width, 3)
    return img_array


@time_decorator
def save_image(
    img_array, name, postfix="_decoded", format=".jpg", path="decoded images"
):
    os.makedirs(path, exist_ok=True)
    name = name.split(".")[0]
    Image.fromarray(img_array, mode="RGB").save(path + "/" + name + postfix + format)


if __name__ == "__main__":
    decode_image("image to decode")
    # I know that i can use open(image_path,"rb") but it isn't interesting
