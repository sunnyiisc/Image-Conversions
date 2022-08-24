"""
Created on 2022, 24 Aug (24/08/22) at 19:26
    Title: image_grayscale.py - Functions to Convert RGB image to Gray-Scale Image
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import numpy as np

# Importing Custom Modules
...

...
def color2gray(img):
    #Image Dimensions
    img_row = img.shape[0]
    img_col = img.shape[1]

    #Image Band spliting (RGB Image)
    img_r = img[:,:,0]
    img_g = img[:,:,1]
    img_b = img[:,:,2]

    img_gray = np.ones( shape=[img_row, img_col], dtype=img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_gray[i][j] = (0.2989*img_r[i][j]) + (0.5780*img_g[i][j]) + (0.1140*img_b[i][j])

    return(img_gray)