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
acc_avg = ...   # 91.48%
mrt_avg = ...   # 477.3ms


#%%
# calculate averages (accuracy & RT) split by category using a for loop and an 
# if statement. (i.e., loop through the data to make a sum for each condition, 
# then divide by the number of data points going into the sum)
#
...

# natural: 88.6%, 489.4ms   man-made: 94.4%, 465.3ms


#%%
# calculate averages (accuracy & RT) split by congruency using indexing, 
# slicing, and numpy's mean function 
# (hint: only one line of code is needed per average)
#
acc_con = ...  # 94.0%
acc_inc = ...  # 88.9%
mrt_con = ...  # 469.6ms
mrt_inc = ...  # 485.1ms


#%% 
# calculate average median RT for each of the four conditions:
# natural/congruent, natural/incongruent, man-made/congruent, man-made-incongruent
# use for loops, indexing/slicing, or both!
# (hint: it might be easier to slice the data into separate natural 
# and man-made dataset variables...)
#
...

# natural/congruent: 478.4ms
# natural/incongruent: 500.3ms
# man-made/congruent: 460.8ms
# man-made/incogruent: 469.9ms


#%%        
# compare congruency conditions' effect on RT within categories using scipy's 
# paired-sample t-test: scipy.stats.ttest_rel()
#
import scipy.stats
...

# natural: t=-5.36, p=2.19e-5
# man-made: t=-2.84, p=0.0096


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
...