import pytesseract as pt
import numpy as np
import skimage
from skimage import io
from skimage import color
import matplotlib
from matplotlib import pyplot as plt
import PIL
from PIL import Image

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


#Red-blue filter
def rbfilter(img):
    d1 = img.shape[0];
    d2 = img.shape[1];
    for i in range(d1):
        print(i)
        for j in range(d2):
            r,g,b = img[i][j]
            mean = (r+g+b)/3
            sd = np.std(img[i][j])
            if sd>=(0.5*mean):
                img[i][j] = [255,255,255]
    return img






cam = io.imread(r"C:\Users\Admin\Desktop\19.bmp")
#cam = rbfilter(cam)

cam2 = (color.rgb2gray(cam))*255
ax = plt.hist(cam2.ravel(), bins = 256)
plt.show()

print(cam2.shape)
plt.imshow(cam)
plt.show()
plt.imshow(cam2,'gray')
plt.show()




#Image.fromarray(cam).save(r"C:\Users\Admin\Desktop\fig3.png")
a = pt.image_to_string(cam2)
print(a)