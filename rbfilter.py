import numpy as np
import pytesseract as pt
import matplotlib
from matplotlib import pyplot as plt
import skimage
from skimage import io
from skimage import color
import PIL
from PIL import Image

cam = io.imread(r'C:\Users\Admin\Desktop\73.bmp')


print(cam.shape)


cam2 = cam.copy();

#red-blue filter

def rbfilter(img):
    d1 = img.shape[0];
    d2 = img.shape[1];
    for i in range(d1):
        print(i)
        for j in range(d2):
            r,g,b = img[i][j]
            if max([r,g,b])>=1.25*img[i][j].mean():
                img[i][j] = [255,255,255]
    return img

#img2 = rbfilter(cam2)

img3 = color.rgb2gray(cam2)

def mean_filter(img):
    sum = 0
    d1 = img.shape[0]
    d2 = img.shape[1]
    newimg = img.copy()
    for i in range(d1):
        for j in range(d2):
            if(i>=1 and j>=1 and i<=d1-2 and j<=d2-2):
                for u in range(3):
                    for v in range(3):
                        sum = img[i-1+u][j-1+v] + sum
            newimg[i][j] = sum/9;
            sum = 0;
            return newimg
        
        
#img2 = mean_filter(img2)


def binarize(img):
    mean = img.mean();
    d1 = img.shape[0];
    d2 = img.shape[1];
    for i in range(d1):
        for j in range(d2):
            if (img[i][j]>=mean):
                img[i][j] = 1
            else:
                img[i][j] = 0
    return img



img3 = binarize(img3)



#The next steps re-transform the grayscale image into rbg png format
img4 = cam.copy();
d1 = cam.shape[0]
d2 = cam.shape[1]
d3 = cam.shape[2]-1

for i in range(d1):
    for j in range(d2):
        for k in range(3):
            img4[i][j][k] = img3[i][j]*255



plt.imshow(img4)
plt.show()
a = pt.image_to_string(img4)
print(a)
