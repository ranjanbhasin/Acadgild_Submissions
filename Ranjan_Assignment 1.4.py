# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:30:09 2018

@author: Ranjan
"""

"""This program will calculate the volume of sphere which has diameter of 12 cm"""

#import numpy
import numpy as np

# defining diameter as 12 cm
print("\n")
print("Radius of Sphere is 12 cm")
diam=12

#calculating volume=4/3 * pi * r-cube

volume=(4/3)*np.pi*(diam/2)**3

# printing volume
print("\n")
print("Volume of Sphere is: " ,volume)