# The code will work perfectly
# if both images match dimensions

from PIL import Image
from numpy import array

# Images Full Path
Image1 = r'GoingCrazy.jpg'
Image2 = r'GoingCrazy2.jpg'

# Open the images with PIL
img1 = Image.open(Image1)
img2 = Image.open(Image2)

# We get the dimensions of both images
# to make sure that they match
img1width = array(img1).shape[1]
img1height = array(img1).shape[0]
img2width = array(img2).shape[1]
img2height = array(img2).shape[0]

# Print the dimensions of each image
print(f'{img1width} x {img1height}')
print(f'{img2width} x {img2height}')

# Get each pixel RGB value
img1_colordata = img1.getdata()
img2_colordata = img2.getdata()

# Create Empty list to store
# Pixel RGB values
PixelList1 = []
PixelList2 = []
# Trigger increases by 1
# when for loop is running
Trigger = 0
state = 0

# We interlace both images lines
for pixel1, pixel2 in zip(img1_colordata,img2_colordata):
    
    # 1270 = 2 lines of pixels since image 635 width
    if state == 0:
        # We add RGB pixel values to Pixel Lists
        PixelList1.extend(pixel1)
        PixelList2.extend(pixel2)
        Trigger += 1
    else:
        # We add RGB pixel values to Pixel Lists
        PixelList1.extend(pixel2)
        PixelList2.extend(pixel1)
        Trigger += 1

    if((Trigger/635).is_integer()):
        print(Trigger)
        if(state == 0): state = 1
        else: state = 0

# We get PixelList and convert RGB numbers to image
# Convert list to bytes
img1colors = bytes(PixelList1)
img2colors = bytes(PixelList2)
# Convert bytes to image
img1 = Image.frombytes('RGB', (img1width,img1height), img1colors)
img2 = Image.frombytes('RGB', (img1width,img1height), img2colors)
# Opens image in Image Viewer
img1.show()
img2.show()
# Saves image to current script folder
img1.save(r'MorpheusBlueSolved.jpg')
img2.save(r'MorpheusRedSolved.jpg')
