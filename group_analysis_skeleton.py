#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
from scipy import stats
import os
import shutil


#%%
# copy files from testing room folders to raw data, rename files to include
# testing room letter in the filename
#
testingrooms = ['A','B','C']
for room in testingrooms:
...

#%%
# read in all the data files in rawdata directory using a for loop
# columns: subject, category, congruency, accuracy, median RT
#
data = np.empty((0,5))
for room in testingrooms:
...

#%%
# calculate overall average accuracy and average median RT
#
acc_avg = ...
mrt_avg = ...


#%%
# calculate averages split by category using a for loop and an if statement!
# (i.e., loop through the data to make a sum for each condition, then divide by
# the number of data points going into the sum)
#
...


#%%
# calculate averages split by congruency using indexing, slicing, and 
# numpy's mean function (hint: only one line of code is needed per average)
#
acc_con = ...
acc_inc = ...
mrt_con = ...
mrt_inc = ...


#%% 
# calculate averages for interaction (category x congruency)
# by using for loops and indexing/slicing!
# hint: check out np.all() for combining multiple conditionals in an index
#
acc_int = np.zeros([2,2])
mrt_int = np.zeros([2,2])
for ct in [1,2]:
    for cn in [1,2]:
        ...


#%%        
# compare congruency conditions within categories using scipy's paired-sample 
# t-test: scipy.stats.ttest_rel()
#
...


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...