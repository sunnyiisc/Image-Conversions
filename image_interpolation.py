"""
Created on 2022, 23 Aug (23/08/22) at 20:14
    Title: image_interpolation.py - Different functions for interpolations
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import numpy as np
from scipy import ndimage, interpolate, signal

# Importing Custom Modules
...

...
def img_interpolate(img, factor):
    azi_x = img.shape[0]
    rng_y = img.shape[1]
    x = np.linspace (0, (azi_x - 1), num=azi_x)
    y = np.linspace (0, (rng_y - 1), num=rng_y)
    f = interpolate.interp2d(x, y, img, kind='linear')

    xx = np.linspace (0, (azi_x - 1), num=(factor*azi_x))
    yy = np.linspace (0, (rng_y - 1), num=(factor*rng_y))
    interpol_img = np.abs(f(xx, yy))

    return(interpol_img)