import numpy
import os
import matplotlib
from matplotlib import pyplot as plt
import PIL
from PIL import Image
import skimage
from skimage import io


img = io.imread(r"C:\Users\Admin\Desktop\AI_project\bmps\50.bmp")

plt.imshow(img)
plt.show()