# This is a sample Python script.

from PIL import Image

# ASCII characters used for string art
ASCII_CHARS = "@%#*+=-:. "

# Resize the image to the desired width while preserving aspect ratio
def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width / 2.5
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert the grayscale image into a string art representation
def image_to_string_art(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

# Load the image file
image_path = "path_to_your_image.png"
image = Image.open(image_path).convert("L")

# Resize the image and convert it to string art
image = resize_image(image, 100)
string_art = image_to_string_art(image)

# Print the string art
width, height = image.size
string_art = "\n".join(string_art[i:i+width] for i in range(0, len(string_art), width))
print(string_art)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
