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
![color_to_grayscale](https://user-images.githubusercontent.com/47363228/186732450-a204a1b1-ea90-4d56-bdff-4ed304c1fd61.png)


### Image Interpolation:
Image interpolation can be used to increase the size of an image.

- Function for Image Interpolation. [click here](image_interpolation.py)
- Code for interpolation of RGB 'Lena' Image by some factor. - Function for RGB to Gray. [click here](main_interpolate.py)

Result on Lena Image for interpolation with a factor of 8:
![interpolation_scipy](https://user-images.githubusercontent.com/47363228/186732698-db0e9fd8-9f7a-4a23-8c5c-ecc4a2095e15.png)
