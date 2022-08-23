"""
Created on 2022, 23 Aug (23/08/22) at 20:10
    Title: main_interpolate.py - ...
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Importing Custom Modules
from image_interpolation import *

...
'''Lena Image Import'''
img = np.array( Image.open('./Image_Samples/lena.tiff') )
np.save('lena.npy', img)

factor = 8

img_interpol = factor * factor * np.absolute( img_interpol(img, factor) )

plt.subplot(1,2,1)
plt.pcolormesh(img, shading='auto')
#plt.invert_yaxis()
plt.colorbar()
plt.subplot(1,2,2)
plt.pcolormesh(img_interpol, shading='auto')
#plt.invert_yaxis()
plt.colorbar()
plt.show()

img_int = Image.fromarray(img_interpol)
img_int.save("lena_interpol.tif")
img_int.show()

x = np.linspace(0, len(img[:]) - 1, num=len(img_interpol[:]))
plt.plot( 10 * np.log10( img[128,:] ), 'o' )
plt.plot(x, 10 * np.log10( img_interpol[(128*factor),:] ) )
plt.title('Centre Row')
plt.xlabel('Pixel Number')
plt.ylabel('Amplitude')
plt.grid()
plt.show()