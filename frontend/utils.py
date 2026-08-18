# from PIL import Image

# def load_image(path):

#     try:

#         img=Image.open(path)

#         return img

#     except:

#          return Image.open("images/default.jpg")







# from PIL import Image
# import os

# # def load_image(path):

# #     if os.path.exists(path):
# #         return Image.open(path)

# #     default_path = os.path.join("images", "default.jpg")

# #     if os.path.exists(default_path):
# #         return Image.open(default_path)

# #     return None


# from PIL import Image
# import os


# def load_image(path):

#     try:

#         if os.path.exists(path):

#             return Image.open(path)

#         else:

#             return Image.open("images/default.jpg")

#     except Exception:

#         return Image.open("images/default.jpg")





import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_IMAGE = os.path.join(BASE_DIR, "images", "default.jpg")


def load_image(path):

    try:

        if os.path.exists(path):

            return Image.open(path)

        else:

            return Image.open(DEFAULT_IMAGE)

    except Exception as e:

        print(e)

        return Image.open(DEFAULT_IMAGE)