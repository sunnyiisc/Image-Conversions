"""
Created on 2022, 23 Aug (23/08/22) at 20:10
    Title: main_interpolate.py - Interpolating the input single/multi-band image of some size by a given factor.
    Description:
        -   Interpolating the given image by a factor.
        -   Using different interpolation methods to interpolate.
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Importing Custom Modules
from image_interpolation import *

...
img = np.array( Image.open('./Image_Samples/lena_color.tiff') )

factor = int( input('Enter the factor by which you want to interpolate: ') )
inter_type = input('Enter the interpolation type (''linear'', ''cubic'', ''quintic''): ')

if len(img.shape) == 2:
    img_interpol = np.zeros((factor * img.shape[0], factor * img.shape[1]), dtype=img.dtype)
    img_interpol = img_interpolate(img, factor, inter_type)
else:
    num_band = img.shape[2]
    img_interpol = np.zeros((factor*img.shape[0], factor*img.shape[1], img.shape[2]), dtype=img.dtype)
    for b in range(num_band):
        img_interpol[:,:,b] = img_interpolate(img[:,:,b], factor, inter_type)


print('Input Image Size =', img.shape[0:2])
print('Interpolated Image Size =', factor,'*',img.shape[0:2], '=', img_interpol.shape[0:2])

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(img_interpol)
plt.title("Interpolated Image by factor of %d" %(factor))
plt.show()

# img_org = Image.fromarray(img)
# img_org.show()

img_int = Image.fromarray(img_interpol)
img_int.save("./Image_Results/lena_interpol.tiff")
# img_int.show()