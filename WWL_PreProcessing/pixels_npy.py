# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:17:13 2018

@author: a
"""

import pydicom
import numpy as np
import os

################################将dicom另存为npy###############################

pathdcm = 'D:/zgy/WWL/20190523/data/else/dicom/1024/'
path_save = 'D:/zgy/WWL/20190523/data/else/npy/1024/'

file_list = os.listdir(pathdcm)
for filename in file_list:
    ds = pydicom.dcmread(os.path.join(pathdcm,filename))    
    pixels = ds.pixel_array
    new_name = filename.split('_')[-1].split('.')[0] 
    np.save(os.path.join(path_save, new_name), pixels)