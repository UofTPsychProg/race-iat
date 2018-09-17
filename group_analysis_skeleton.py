#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scene-cat problem set for PSY 1210 - Fall 2018

@author: Michael Mack
"""

#%% import block 
import numpy as np
import scipy as sp


#%%
# read in data file: subject_summary_num.csv
# columns: subject, category, congruency, accuracy, median RT
#
data = ...


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
n_data = len(data)
acc_man,acc_nat,mrt_man,mrt_nat = 0,0,0,0
n_man,n_nat = 0,0
for x in ...


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
#
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
