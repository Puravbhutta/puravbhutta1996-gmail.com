import numpy
import os
import matplotlib
from matplotlib import pyplot as plt
import PIL
from PIL import Image
import skimage
from skimage import io

#Setup
path1 = r"C:\Users\Admin\Desktop\AI_project\bmps"
path2 = r"C:\Users\Admin\Desktop\AI_project\bmps1"
cordinates = []
count = 0


#Blackening

for file in os.listdir(path1):
    img1 = io.imread(path1+"\\"+file)
    img2 = io.imread(path2+"\\"+file)
    img3 = img2.copy()
    rect = [0,0,0,0]
    check1 = 0
    d1 = img1.shape[0]
    d2 =img1.shape[1]
    d3 = img1.shape[2]
    for i in range(d1):
        for j in range(d2):
            for k in range(d3):
                
                if(img1[i][j][k]==img2[i][j][k]):
                    img3[i][j][k] = 0
       
       
#Labelling
    
    for i in range(d1):
        for j in range(d2):
            if img3[i][j][0]>220 and check1==0:
                rect[0] = j
                rect[1] = i
                check1 = 1;
            elif img3[i][j][0]>220:
                rect[2] = j
                rect[3] = i
                
                
                
    cordinates.append(rect)
    print(count)
    count = count+1
    
    

print(cordinates)
f = open(r"C:\Users\Admin\Desktop\er.txt",'w')
f.write(str(cordinates))
f.close()