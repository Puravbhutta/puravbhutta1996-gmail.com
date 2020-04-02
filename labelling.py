import numpy
import os
import matplotlib
from matplotlib import pyplot as plt
import PIL
from PIL import Image
import skimage
from skimage import io


path = r"C:\Users\Admin\Desktop\AI_project\Roads"
path2 = r"C:\Users\Admin\Desktop\AI_project\Roads_labelled"

for file in os.listdir(path):
    img = Image.open(path+"\\"+file)
    img.save(path2+"\\"+file)
    print(file.index)


