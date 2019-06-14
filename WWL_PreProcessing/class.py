# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 19:34:00 2018

@author: a
"""

#import numpy as np
import os
import random
import shutil

###将一个文件夹中的图像，随机抽取一部分，分到另一个文件夹####

Path_256 = 'D:/zgy/WWL/20190523/data/pelvis/npy/512/'
#Path_256 = 't/'
#Path_1024 = '1024npy/'
#Path_512 = '512npy/'
#Path_train = 'data_true/train/'
Path_test = 'D:/zgy/WWL/20190523/data/test/'
#Path_test = 'r/'
Path_valid = 'D:/zgy/WWL/20190523/data/valid/'
#Path_valid = 's/'


#img_test = []
file256_list = os.listdir(Path_256)
sample_test = random.sample(file256_list, 200)
for name in sample_test:
    shutil.copyfile(Path_256 + name, Path_test + name)   
    os.remove(Path_256 + name)
file256new_list = os.listdir(Path_256)
sample_valid = random.sample(file256new_list, 5)
for name in sample_valid:
    shutil.copyfile(Path_256 + name, Path_valid + name)

'''
file512_list = os.listdir(Path_512)
sample_test = random.sample(file512_list, 2390)
for name in sample_test:
    shutil.copyfile(Path_512 + name, Path_test + name)   
    os.remove(Path_512 + name)
file512new_list = os.listdir(Path_512)
sample_valid = random.sample(file512new_list, 11)
for name in sample_valid:
    shutil.copyfile(Path_512 + name, Path_valid + name)
'''

'''
file1024_list = os.listdir(Path_1024)
sample_test = random.sample(file1024_list, 100)
for name in sample_test:
    shutil.copyfile(Path_1024 + name, Path_test + name)   
    os.remove(Path_1024 + name)
file1024new_list = os.listdir(Path_1024)
sample_valid = random.sample(file1024new_list, 4)
for name in sample_valid:
    shutil.copyfile(Path_1024 + name, Path_valid + name)
'''

'''
file1024_list = os.listdir(Path_1024)
for name in file1024_list:
    img = np.load(Path_1024 + name)
'''
    