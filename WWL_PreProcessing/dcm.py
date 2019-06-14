# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 09:52:26 2018

@author: a
"""

import numpy as np
import pydicom
import os


Path_s = 'D:/zgy/WWL/20190523/WWL_images/'
Path_data = 'D:/zgy/WWL/20190523/data/data_s/'
Path_256npy = 'D:/zgy/WWL/20190523/data/256npy/'
Path_512npy = 'D:/zgy/WWL/20190523/data/512npy/'
Path_1024npy = 'D:/zgy/WWL/20190523/data/1024npy/'
Path_256dcm = 'D:/zgy/WWL/20190523/data/256dcm/'
Path_512dcm = 'D:/zgy/WWL/20190523/data/512dcm/'
Path_1024dcm = 'D:/zgy/WWL/20190523/data/1024dcm/'

'''
##########################将test中的_s数据存到rest文件夹中######################
#################是为了将数据统一存放，方便后续处理##############################
dcm_list_s = os.listdir(Path_s)
num_list_s = len(dcm_list_s)
for i in range(num_list_s):
    filename = dcm_list_s[i]
    if '_' in filename:
        ds_s = pydicom.dcmread(os.path.join(Path_s, filename))
        ds_s.save_as(os.path.join(Path_data, filename))
        
'''        
        


#########################读取rest文件夹中的数据#################################
#####################生成标签label_second,以及像素数据并另存#####################
dcm_list = os.listdir(Path_data)
num_list = len(dcm_list)     
label_second = np.empty([int(num_list), 3], dtype = np.int32)
for num in range(num_list):
    filename = dcm_list[num]
    filename_new = filename.split('_')[0] + '_' + str(num) + '.dcm'
    filepath = os.path.join(Path_data, filename)
    filepath_new = os.path.join(Path_data, filename_new)
    os.rename(filepath, filepath_new)
    ds = pydicom.dcmread(os.path.join(Path_data, filename_new))
    label_second[num][0] = num
    label_second[num][1] = ds.WindowWidth
    label_second[num][2] = ds.WindowCenter
    pixels = ds.pixel_array
    if pixels.shape == (256, 256):
        ds.save_as(os.path.join(Path_256dcm, filename_new))
        Path_npy = os.path.join(Path_256npy, str(num))
        np.save(Path_npy, pixels)
    elif pixels.shape == (512, 512): 
        ds.save_as(os.path.join(Path_512dcm, filename_new))
        Path_npy = os.path.join(Path_512npy, str(num))
        np.save(Path_npy, pixels)
    elif pixels.shape == (1024, 1024):
        ds.save_as(os.path.join(Path_1024dcm, filename_new))
        Path_npy = os.path.join(Path_1024npy, str(num))
        np.save(Path_npy, pixels)
    num += 1
np.save('label.npy', label_second)
        
    