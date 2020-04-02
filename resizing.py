import numpy
import os
import matplotlib
from matplotlib import pyplot as plt
import PIL
from PIL import Image
import skimage
from skimage import io
import cv2

count = 0
path1 = r"C:\Users\Admin\Desktop\AI_project\bmpimages"
path2 = r"C:\Users\Admin\Desktop\AI_project\bmpimages1"

for file in os.listdir(path1):
    count = count+1
    img = io.imread(path1+"\\"+file)
    img2 = cv2.resize(img,(480,320))
    img3 = Image.fromarray(img2)
    img3.save(r"C:\Users\Admin\Desktop\AI_project\bmps"+"\\"+str(count)+".bmp")