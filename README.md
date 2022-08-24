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

<img src="https://render.githubusercontent.com/render/math?math={Y = (0.299 \times R) + (0.587 \times G) + (0.114 \times B)}#gh-light-mode-only">
<img src="https://render.githubusercontent.com/render/math?math={\color{white}Y = (0.299 \times R) + (0.587 \times G) + (0.114 \times B)}{Reference Power}}#gh-dark-mode-only">

- Main code for RGB to Gray Conversion with 'Lena' Image. [click here](main_grayscale.py)
- Function for RGB to Gray. [click here](image_grayscale.py)

Result on Lena Image:

### Image Interpolation: