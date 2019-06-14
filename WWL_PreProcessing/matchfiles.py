# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 09:43:18 2018

@author: a
"""

############匹配两个文件夹下的文件，吧其中一个文件夹中文件名相同的文件另存#########

import os
import hashlib
import shutil

pathdcm = 'D:/zgy/WWL/20190523/data/abd/dicom/512/'
#pathdcm = 'r/'
pathnpy = 'D:/zgy/WWL/20190523/data/abd/npy/512/'
#pathnpy = 't/'
pathsame = 'D:/zgy/WWL/20190523/data/512npy/'

#pathsame = 's/'
md5dict = {}

filedcm_list = os.listdir(pathdcm)
#num_dcm = len(filedcm_list)

filenpy_list = os.listdir(pathnpy)
#num_npy = len(filenpy_list)

for filename in filedcm_list:
    dcmname = filename.split('_')[-1].split('.')[0]
    hashvalue = hashlib.md5(dcmname.encode('utf-8')).hexdigest()
    md5dict[hashvalue]=os.path.join(pathdcm, dcmname)
for filename in filenpy_list:
    npyname = filename.split('.')[0]    
    hashvalue = hashlib.md5(npyname.encode('utf-8')).hexdigest()
    if hashvalue in md5dict:
        shutil.copy(os.path.join(pathnpy, filename), os.path.join(pathsame, filename))
    
    