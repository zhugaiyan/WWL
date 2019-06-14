# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:08:57 2018

@author: a
"""

#import numpy as np
import pydicom
import os
###将图像按部位分到不同的文件夹####

Pathimg = 'D:/zgy/WWL/20190523/data/1024dcm/'
Pathimg_head = 'D:/zgy/WWL/20190523/data/head/dicom/1024/'
Pathimg_abdomen = 'D:/zgy/WWL/20190523/data/abd/dicom/1024/'
Pathimg_Lspine = 'D:/zgy/WWL/20190523/data/L-spine/dicom/1024/'
Pathimg_Cspine = 'D:/zgy/WWL/20190523/data/C-spine/dicom/1024/'
Pathimg_knee = 'D:/zgy/WWL/20190523/data/knee/dicom/1024/'
Pathimg_hip = 'D:/zgy/WWL/20190523/data/hip/dicom/1024/'
Pathimg_pelvis = 'D:/zgy\WWL/20190523/data/pelvis/dicom/1024/'
Pathimg_cardiac = 'D:/zgy/WWL/20190523/data/cardiac/dicom/1024/'
Pathimg_else = 'D:/zgy/WWL/20190523/data/else/dicom/1024/'

file_list = os.listdir(Pathimg)
num = len(file_list)

for i in range(num):
    filename = file_list[i]
    ds = pydicom.dcmread(os.path.join(Pathimg, filename))
    bodypart = ds.BodyPartExamined
    if bodypart == 'HEAD':
        ds.save_as(os.path.join(Pathimg_head, filename))
    elif bodypart == 'ABDOMEN':
        ds.save_as(os.path.join(Pathimg_abdomen, filename))
    elif bodypart == 'L-SPINE':
        ds.save_as(os.path.join(Pathimg_Lspine, filename))
    elif bodypart == 'C-SPINE':
        ds.save_as(os.path.join(Pathimg_Cspine, filename))
    elif bodypart == 'KNEE':
        ds.save_as(os.path.join(Pathimg_knee, filename))
    elif bodypart == 'HIP':
        ds.save_as(os.path.join(Pathimg_hip, filename))
    elif bodypart == 'PELVIS':
        ds.save_as(os.path.join(Pathimg_pelvis, filename))
    elif bodypart == 'CARDIAC':
        ds.save_as(os.path.join(Pathimg_cardiac, filename))
    else :
        ds.save_as(os.path.join(Pathimg_else, filename))
        
    