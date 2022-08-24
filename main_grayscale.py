"""
Created on 2022, 24 Aug (24/08/22) at 19:28
    Title: main_grayscale.py - ...
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
from matplotlib import image, pyplot as plt
from PIL import Image

# Importing Custom Modules
from image_grayscale import color2gray

...
'''Lena Image Computation'''
img_lena = image.imread("./Image_Samples/lena_color.tiff")    #RGB reading of Image

img_lena_gray = color2gray(img_lena)

plt.subplot(1,2,1)
plt.imshow(img_lena)
plt.title('Input Color Image')

plt.subplot(1,2,2)
plt.imshow(img_lena_gray, cmap='gray')
plt.title("Gray Lena Image")
plt.show()

img_gray = Image.fromarray(img_lena_gray)
img_gray.save("./Image_Results/lena_grayscale.tiff")
img_gray.show()