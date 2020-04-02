import matplotlib
import numpy
from matplotlib import pyplot as plt
import skimage
from skimage import io;
import pytesseract
import PIL
from PIL import Image
cam = io.imread(r"C:\Users\Admin\Desktop\AI_project\capture.png")
#cam = Image.open("C:\\Users\\Admin\\Desktop\\tese.png")

def rgb2gray(rgb_img):
    r,g,b = rgb_img[:,:,0],rgb_img[:,:,1],rgb_img[:,:,2]
    gray = (r*0.2989+g*0.5870+b*0.1140)
    return gray



cam2 = Image.open(r"C:\Users\Admin\Desktop\AI_project\capture.png")

new_img = cam2.save('grayscale.png') 

print(cam2.shape)

img = Image.fromarray(cam)

plt.imshow(img,'gray')
plt.show()
plt.imshow(cam2,'gray')
plt.show()

#img.save("Savedimg.bmp")




#plt.imshow(cam,'gray');
#plt.show();
