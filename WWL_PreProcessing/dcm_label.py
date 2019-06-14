# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:36:15 2019

@author: zhuhanyou
"""

import numpy as np
import pydicom
import os


Path_data = 'D:/zgy/WWL/20190523/data/data_s/'


##########读取窗宽窗位值，并另存为标签#########################

dcm_list = os.listdir(Path_data)
num_list = len(dcm_list)     
label_second = np.empty([int(num_list), 3], dtype = np.int32)
for num in range(num_list):
    filename = dcm_list[num]
    new_num = filename.split('_')[-1].split('.')[0] 
    ds = pydicom.dcmread(os.path.join(Path_data, filename))
    label_second[num][0] = new_num
    label_second[num][1] = ds.WindowWidth
    label_second[num][2] = ds.WindowCenter
    num += 1
np.save('label.npy', label_second)