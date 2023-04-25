#  Image-Binary-Converter
This software allows you to convert images to binary code and vice versa

This iteration of program can convert .jpg images only

To convert an image to binary code put it to "image to encrypt" folder and run encrypter.py your converted image will appear in "encrypted images" folder.

To convert a binary code to image put it to "image to decode" folder and run decoder.py your converted image will appear in "decoded images" folder.

### Dev setup
1. Optional PowerShell permitions: `Set-ExecutionPolicy unrestricted`
1. `python -m venv venv`
1. `.\venv\Scripts\activate`
1. `pip install -r .\requirements.txt`
1. `python decoder.py`