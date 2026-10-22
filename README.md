PURE PYTHON IMAGE PROCESSOR 

1.INVERT IMAGE 

Purpose:Inverts the brightness of each pixel
Working:Subtracts each pixel value from 255 which reverses the brightness of the image.
Output:Dark pixels become light and vice versa 

OUTPUT:

[255,205,155,105,55]
[230,180,130,80,30]
[245,195,145,95,45]
[250,200,150,100,50]
[220,170,120,70,20]

2.BRIGHTNESS ADJUSTMENT 

Purpose:Increases or decreases the brightness of an image
Working:Adds the given amount to every pixel.
Output:

[30,80,130,180,230]
[55,105,155,205,255]
[40,90,140,190,240]
[65,115,165,215,255]
[35,85,135,185,255]

3.THRESHOLDING IMAGE

Purpose:Converts grayscale image into black and white image
Working:Pixels below the threshold value (100) become 0,while equal and above becomes 255.
Output:

[0,0,255,255,255]
[0,0,255,255,255]
[0,0,255,255,255]
[0,0,255,255,255]
[0,0,255,255,255]

4.FLIPPING THE IMAGE

Purpose:Flips the image horizontally
Working:Pixel order in each row gets reversed
Output:

[200,150,100,50,0]
[225,175,125,75,25]
[210,160,110,60,10]
[235,185,135,85,35]
[255,155,105,55,5]

5.ROTATING AN IMAGE

Purpose:Rotates image 90 degrees clockwise
Working:Rearranges the rows and columns to rotate.
Output:

[5,35,10,25,0]
[55,85,60,75,50]
[105,135,110,125,100]
[155,185,160,175,150]
[255,235,210,225,200]

6.CROPPING AN IMAGE

Purpose:Crops image to get a smaller portion of the original image
Working:Selecting pixels between specific rows and columns indices.The ending indices are excluded.
Output:

[75,125,175]
[60,110,160]
[85,135,185]

7.BLURRING IMAGE

Purpose:Applies blur effect
Working:Calcultes the average of the 3x3 neighbourhood around each inner pixel and replaces the pixel with the average.We use integer division to get a whole number
Output:

[0,50,100,150,200]
[25,61,11,161,225]
[10,73,123,173,210]
[35,66,116,172,235]
[5,55,105,155,255]

8.RGB ADJUSTMENT

Purpose:Adjusts brightness of coloured image
Working:Adds the specified amount separately to the red,green,blue values of each pixel.
Output:

a.for the rgb test image
[(255,0,0),(0,255,0)]
[(0,0,255),(255,255,0)]

b.with a brightness adjustment of 30
[(255,30,30),(30,255,30)]
[(30,30,255),(255,255,30)]

9.PPM LOADING

Purpose:Loads a colour image from a P3 PPM file.
Working:Reads the image dimensions and RGB pixel values from sample.ppm then arranges them into rows of RGB tuples.
Output:

loaded PPM image:
[(255,0,0),(0,255,0)]
[(0,0,255),(255,255,0)]


