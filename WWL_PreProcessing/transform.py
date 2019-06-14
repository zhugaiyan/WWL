# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:02:03 2018

@author: a
"""

import numpy as np
#from skimage import transform
import os
#from PIL import Image
import cv2

Path_256npy = 'D:/zgy/WWL/20190523/data/else/npy/256/'
Path_1024npy = 'D:/zgy/WWL/20190523/data/else/npy/1024/'
#Path_1024npy = '1024npy/'
Path_256_512 = 'D:/zgy/WWL/20190523/data/else/npy/512/'
Path_1024_512 = 'D:/zgy/WWL/20190523/data/else/npy/512/'

####################将256*256的图像放大到512*512################################
file256_list = os.listdir(Path_256npy)
num_256 = len(file256_list)
for i in range(num_256):
    filename_256 = file256_list[i]
    file_256 = np.load(os.path.join(Path_256npy, filename_256))
#    img_256 = transform.resize(file_256, (512, 512))
    img_256 = cv2.resize(file_256, (512, 512))
    np.save(os.path.join(Path_256_512, filename_256), img_256)
  

###################将1024*1024的图像缩小到512*512##############################   
file1024_list = os.listdir(Path_1024npy)
num_1024 = len(file1024_list)
for i in range(num_1024):
    filename_1024 = file1024_list[i]
    file_1024 = np.load(os.path.join(Path_1024npy, filename_1024))
#    img_256 = transform.resize(file_256, (512, 512))
    img_1024 = cv2.resize(file_1024, (512, 512))
    np.save(os.path.join(Path_1024_512, filename_1024), img_1024)