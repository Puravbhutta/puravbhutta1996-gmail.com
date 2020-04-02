import os
import skimage
from skimage import io
import PIL
from PIL import Image
import matplotlib
from matplotlib import pyplot
import pytesseract

path = r"C:\Users\Admin\Desktop\positive"
a = []
count = 0
for file in os.listdir(path):
    t = Image.open(path+"\\"+file)
    a.append(pytesseract.image_to_string(t))
    count = count + 1;
    if count%10==0:
        print(count)
    

    
for i in range(len(a)):
    print(a[i]+os.listdir(path)[i]);
    

