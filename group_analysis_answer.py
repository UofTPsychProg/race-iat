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
data = np.loadtxt('subject_summary_num.csv',delimiter=',',skiprows=1)


#%%
# calculate overall average accuracy and average median RT
#
acc_avg = np.mean(data[:,3])
mrt_avg = np.mean(data[:,4])


#%%
# calculate averages split by category using a for loop and an if statement!
# (i.e., loop through the data to make a sum for each condition, then divide by
# the number of data points going into the sum)
#
n_data = len(data)
acc_man,acc_nat,mrt_man,mrt_nat = 0,0,0,0
n_man,n_nat = 0,0
for x in range(n_data):
    if data[x,1]==1:
        acc_man += data[x,3]
        mrt_man += data[x,4]
        n_man += 1
    else:
        acc_nat += data[x,3]
        mrt_nat += data[x,4]
        n_nat += 1
acc_man = acc_man/n_man
acc_nat = acc_nat/n_nat
mrt_man = mrt_man/n_man
mrt_nat = mrt_nat/n_nat


#%%
# calculate averages split by congruency using indexing, slicing, and 
# numpy's mean function (hint: only one line of code is needed per average)
#
acc_con = np.mean(data[data[:,2]==1,3])
acc_inc = np.mean(data[data[:,2]==2,3])
mrt_con = np.mean(data[data[:,2]==1,4])
mrt_inc = np.mean(data[data[:,2]==2,4])


#%% 
# calculate averages for interaction (category x congruency)
# by using for loops and indexing/slicing!
#
acc_int = np.zeros([2,2])
mrt_int = np.zeros([2,2])
for ct in [1,2]:
    for cn in [1,2]:
        ix = np.all([data[:,1]==ct,data[:,2]==cn],axis=0)
        acc_int[ct-1,cn-1] = np.mean(data[ix,3])
        mrt_int[ct-1,cn-1] = np.mean(data[ix,4])


#%%        
# compare congruency conditions within categories using scipy's paired-sample 
# t-test: scipy.stats.ttest_rel()
#
ixc = np.all([data[:,1]==1,data[:,2]==1],axis=0)
ixi = np.all([data[:,1]==1,data[:,2]==2],axis=0)
man_acc_ttest = sp.stats.ttest_rel(data[ixc,3],data[ixi,3])
man_mrt_ttest = sp.stats.ttest_rel(data[ixc,4],data[ixi,4])

ixc = np.all([data[:,1]==2,data[:,2]==1],axis=0)
ixi = np.all([data[:,1]==2,data[:,2]==2],axis=0)
nat_acc_ttest = sp.stats.ttest_rel(data[ixc,3],data[ixi,3])
nat_mrt_ttest = sp.stats.ttest_rel(data[ixc,4],data[ixi,4])


#%%
# print out averages and t-test results
# (hint: use the ''.format() method to create formatted strings)
#
print('\nOVERALL: {:.2f}%, {:.1f} ms'.format(100*acc_avg,mrt_avg))
print('\nMAIN EFFECTS')
print('category - manmade: {:.2f}%, {:.1f} ms'.format(100*acc_man,mrt_man))
print('         - natural: {:.2f}%, {:.1f} ms'.format(100*acc_nat,mrt_nat))
print('congruency - congruent: {:.2f}%, {:.1f} ms'.format(100*acc_con,mrt_con))
print('           - incongruent: {:.2f}%, {:.1f} ms'.format(100*acc_inc,mrt_inc))
print('\nINTERACTION')
print('manmade,congruent:   {:.2f}%, {:.1f} ms'.format(100*acc_int[0,0],mrt_int[0,0]))
print('manmade,incongruent: {:.2f}%, {:.1f} ms'.format(100*acc_int[0,1],mrt_int[0,1]))
print('natural,congruent:   {:.2f}%, {:.1f} ms'.format(100*acc_int[1,0],mrt_int[1,0]))
print('natural,incongruent: {:.2f}%, {:.1f} ms'.format(100*acc_int[1,1],mrt_int[1,1]))
print('\nSTATS')
print('manmade, accuracy:  t = {:.4f}, p = {:.6f}'.format(man_acc_ttest[0],man_acc_ttest[1]))
print('manmade, median rt: t = {:.4f}, p = {:.6f}'.format(man_mrt_ttest[0],man_mrt_ttest[1]))
print('manmade, accuracy:  t = {:.4f}, p = {:.6f}'.format(nat_acc_ttest[0],nat_acc_ttest[1]))
print('manmade, median rt: t = {:.4f}, p = {:.6f}'.format(nat_mrt_ttest[0],nat_mrt_ttest[1]))