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



#Red-blue filter
def rbfilter(img):
    d1 = img.shape[0];
    d2 = img.shape[1];
    for i in range(d1):
        print(i)
        for j in range(d2):
            r,g,b = img[i][j]
            if max([r,g,b])>=1.5*img[i][j].mean():
                img[i][j] = [255,255,255]
    return img

img = rbfilter(cam)


#Convert to grayscale
img = color.rgb2gray(cam)


d1 = img.shape[0]
d2 = img.shape[1]
print(img.shape)
mean = img.mean()
print(mean)


img = mean_filter(img)

#binarizes the image into only black and white pixels
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


#normalize
img = binarize(img)
img = mean_filter(img)
img = img/img.max()        


#The next steps re-transform the grayscale image into rbg png format
cam2 = cam.copy();
d1 = cam.shape[0]
d2 = cam.shape[1]
d3 = cam.shape[2]-1

for i in range(d1):
    for j in range(d2):
        for k in range(3):
            cam2[i][j][k] = img[i][j]*255

img2 = Image.fromarray(img);
#img2.save(r'C:\Users\Admin\Desktop\AI_Project\test.jpg')
plt.imshow(cam)
plt.show()
plt.imshow(cam2)
plt.show()

a = pt.image_to_string(cam)
print(a)

a = pt.image_to_string(img2)
print(a)






