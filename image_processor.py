
#INVERTING AN IMAGE

image=[
    [0,50,100,150,200],
    [25,75,125,175,225],
    [10,60,110,160,210],
    [5,55,105,155,205],
    [35,85,135,185,235]

]

def invert_image(image):
    new_image = []
    for row in image:
        new_row = []
        for pixel in row:
            new_pixel = 255 - pixel
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image

print("Original Image:")
for row in image:
    print(row)

inverted= invert_image(image)

print("\nInverted Image:")
for row in inverted:
    print(row)

#BRIGHTNESS ADJUSTMENT

def adjust_brightness(image, amount):
    new_image = []
    for row in image:
        new_row = []
        for pixel in row:
            new_pixel = pixel + amount
            new_pixel = max(0, min(255, new_pixel))  # Ensure pixel value is within [0, 255]
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image  

brighter=adjust_brightness(image, 30)
print("\nBrighter Image:")
for row in brighter:
    print(row)

darker=adjust_brightness(image, -30)
print("\nDarker Image:")
for row in darker:
    print(row)

#THRESHOLDING AN IMAGE

def threshold_image(image,threshold):
    new_image = []
    for row in image:
        new_row = []
        for pixel in row:
            if pixel < threshold:
                new_pixel = 0
            else:
                new_pixel = 255
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image

thresholded=threshold_image(image, 100)
print("\nThresholded Image (threshold=100):")
for row in thresholded:
    print(row)


#FLIPPING AN IMAGE

def flip_horizontal(image):
    new_image = []
    for row in image:
        new_row = row[::-1]  # Reverse the row
        new_image.append(new_row)
    return new_image

flipped=flip_horizontal(image)
print("\nFlipped Image (Horizontal):")
for row in flipped:
    print(row)

#ROTATING AN IMAGE

def rotate_90_clockwise(image):
    rows=len(image)
    cols=len(image[0])
    new_image = []

    for col in range(cols):
        new_row = []
        for row in range(rows-1, -1, -1):
            new_row.append(image[row][col])
        new_image.append(new_row)
    return new_image

rotated=rotate_90_clockwise(image)
print("\nRotated Image (90 degrees clockwise):")
for row in rotated:
    print(row)

def crop_image(image, start_row, start_col, end_row, end_col):
    new_image = []
    for row in range(start_row, end_row):
        new_row = image[row][start_col:end_col]
        new_image.append(new_row)
    return new_image

cropped=crop_image(image, 1, 1, 4, 4)
print("\nCropped Image:")
for row in cropped:
    print(row)

#BLURRING AN IMAGE

def blur_image(image):
    rows=len(image)
    cols=len(image[0])
    new_image = [row[:] for row in image]  # Create a copy of the original image

    for row in range(1,rows-1):
        for col in range(1,cols-1):
            total=0
            
            for r in range(row-1,row+2):
                for c in range(col-1,col+2):
                    total+=image[r][c]
            average=total//25
            new_image[row][col]=average
                
    return new_image

blurred=blur_image(image)
print("\nBlurred Image:")
for row in blurred:
    print(row)

#COLOUR IMAGES  

rgb_image=[
    [(255,0,0),(0,255,0)],
    [(0,0,255),(255,255,0)]
]
print("\nOriginal RGB Image:")
for row in rgb_image:
    print(row)

def adjust_brightness_rgb(image, amount):
    new_image = []
    for row in image:
        new_row = []
        for pixel in row:
            r, g, b = pixel
            r = max(0, min(255, r + amount))
            g = max(0, min(255, g + amount))
            b = max(0, min(255, b + amount))
            new_pixel=(r, g, b)
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image
brighter_rgb=adjust_brightness_rgb(rgb_image, 30)
print("\nBrighter RGB Image:")
for row in brighter_rgb:
    print(row)

#PPM
def load_ppm(filename):
    with open(filename, 'r') as file:
        content=file.read()
    # Remove comments and empty lines
    lines = []

    for line in content.splitlines():
        line=line.split("#")[0]
        lines.append(line)

    values=" ".join(lines).split()
    if len(values)==0:
        raise ValueError("Empty PPM file")

    if len(values)<4:
        raise ValueError("Invalid PPM file format")

    if values[0]!="P3":
        raise ValueError("Invalid PPM file format: missing P3 header")

    width=int(values[1])
    height=int(values[2])
    max_value=int(values[3])

    if max_value<1 or max_value >65535:
        raise ValueError("Invalid max value in PPM file")

    numbers=[int(value) for value in values[4:]]
    if len(numbers) != width*height*3:
        raise ValueError("Invalid number of pixel values in PPM file")

    if any(value<0 or value>max_value for value in numbers):
        raise ValueError("Pixel values out of range in PPM file")

    image=[]
    index=0

    for _ in range(height):
        new_row=[]
        for col in range(width):
            r=numbers[index]
            g=numbers[index+1]
            b=numbers[index+2]
            new_row.append((r,g,b))
            index+=3

            r=r*255//max_value
            g=g*255//max_value
            b=b*255//max_value

            new_row.append((r,g,b))

        image.append(new_row)

    return image

def print_image(image):
    for row in image:
        print(row)

def show_before_after(name, original, result):
    print("\n===========" ,name, "===========")
    print("Before Operation :")
    print_image(original)
    print("\nAfter Operation :")
    print_image(result)


loaded_image=load_ppm("sample.ppm")
print("\nLoaded PPM Image:")
for row in loaded_image:
    print(row)


#TEST CALL SECTION

#Test inversion
result=invert_image(image)
show_before_after("Inversion", image, result)

#Test brightness adjustment
result=adjust_brightness(image, 30)
show_before_after("Brightness Adjustment (+30)", image, result)

#Test thresholding
result=threshold_image(image, 100)
show_before_after("Thresholding (100)", image, result)

#Test flipping
result=flip_horizontal(image)
show_before_after("Flipping (Horizontal)", image, result)

#Test rotation
result=rotate_90_clockwise(image)
show_before_after("Rotation (90 degrees clockwise)", image, result)

#Test cropping
result=crop_image(image, 1, 1, 4, 4)
show_before_after("Cropping", image, result)

#Test blurring
result=blur_image(image)
show_before_after("Blurring", image, result)



    
   