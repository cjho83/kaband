# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:44:09 2018

@author: cjho
"""

# Use GDAL to read the NITF data
#

import gdal
from gdalnumeric import *
from gdalconst import *

import numpy as np
import cv2

filename    = './NITF/A_BH_Labs_3km_NESW_1.ntf'
dataset     = gdal.Open(filename,GA_ReadOnly)

amplitudeBand   = dataset.GetRasterBand(1)
phaseBand       = dataset.GetRasterBand(2)
amplitudeArr    = BandReadAsArray(amplitudeBand)
phaseArr        = BandReadAsArray(phaseBand)

def aveShape(a, shape):
    sh = shape[0],a.shape[0]//shape[0],shape[1],a.shape[1]//shape[1]
    return a.reshape(sh).mean(-1).mean(1)

sh      = amplitudeArr.shape
factor  = 8
imgsm   = aveShape(amplitudeArr,(sh[0]//factor,sh[1]//factor))

imguint8 = cv2.convertScaleAbs(imgsm)

cv2.imshow(filename,imguint8)
cv2.waitKey(0)
cv2.destroyAllWindows()