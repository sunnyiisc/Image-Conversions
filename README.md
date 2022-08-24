# Image-Conversions
This repository had several functions and their working code 
for several Image Conversions as follows:

- Color to GrayScale Conversion
- Color to Binary Conversion
- Image Interpolation

Sample Images Folder - 'Image_Samples' [click here](Image_Samples)

### Color to Grayscale Conversion:
The RBG image consists of 3 bands 'Red', 'Green' and 'Blue'. This
three bands can be combined to get a single grayscale band
according the formula given ITU Recommendation (Rec. 601) as

$$ Y = (0.299 \times R) + (0.587 \times G) + (0.114 \times B) $$

- Function for RGB to Gray. [click here](image_grayscale.py)
- Main code for RGB to Gray Conversion with 'Lena' Image. [click here](main_grayscale.py)

Result on Lena Image:
![Figure_1](https://user-images.githubusercontent.com/47363228/186481544-500a86e6-6053-4f9e-afa9-91f7264c2686.png)


### Image Interpolation:
Image interpolation can be used to increase the size of an image.

- Function for Image Interpolation. [click here](image_interpolation.py)
- Code for interpolation of RGB 'Lena' Image by some factor. - Function for RGB to Gray. [click here](main_interpolation.py)