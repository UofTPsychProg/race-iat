# scene-cat
PSY 1210 Problem Assignment 2

We're giving you some data files and the skeleton of a data analysis script. You need to flesh out the missing sections of the analysis script to implement a simple analysis of the data.

## The experiment
Here's a quick description of the experiment behind the data: 23 participants categorized briefly-presented scenes as natural (e.g., forests, mountains, landscapes, beaches) or man-made (e.g., cities, highways, buildings). Scenes had objects that were either congruent with the scene's category (e.g., a tree in a natural landscape) or incongruent with the scene's category (e.g., a man-made house in a natural landscape). The question was whether or not these incongruent objects significantly impacted participants' scene categorization. If you want a spoiler, check out [Mack & Palmeri, 2010](http://macklab.utoronto.ca/uploads/8/1/8/3/8183/mackpalmeri2010a.pdf).

## The data
We provide the summary data for each participant (including their accuracy and median reaction time (RT) for each of the four conditions (natural vs. man-made scenes crossed with congruent vs. incongruent objects). Since the data was collected in three different testing rooms, these summary data files (all named experiment_data.csv) are separated into three different directories (testingroom{A,B,C}). Each file contains data from 7 or 8 participants.

The data is formatted into 5 columns:
* subject number
* category: 1 = natural, 2 = man-made
* congruency: 1 = congruent, 2 = incongruent
* accuracy
* median RT (ms)

## Your task
Fill in the missing sections of the skeleton analysis script with python code in order to:
1. Copy these files into the rawdata directory, renaming each file to include the corresponding testing room letter (e.g., experiment_data_A.csv). _hint:_ check out the `os` and `shutil` python libraries.
2. Read in all the data from the newly copied data files.
3. Calculate the following:
   * Overall average accuracy and median RT
   * Averages of accuracy and median RT split by category (natural vs. man-made) using a `for` loop, `if` statement, and arithmetic
   * Averages of accuracy and median RT split by congruency (congruent vs. incongruent) using numpy's mean function
   * Average median RT for each of the four conditions
4. conduct t-tests to compare congruent vs. incongruent RT for each category using `scipy.stats.ttest_rel()`
5. Print out all of the averages and t-test results in a coherent format.

The analysis script skeleton repeats these instructions and gives you a few more pointers on how to accomplish these tasks. This is not a group assignment, but you are strongly encouraged to help each other.

Good luck!
