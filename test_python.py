# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
conda update anaconda
conda install spyder=5.1.5

import math
math.sqrt(16)

#%%
getcwd() # get working directory 
from os import chdir # set working directory 
chdir("/Users/tengsi/Desktop/Summer school_Data Analysis")

import pandas as pd # load csv data 
df = pd.read_csv ("taylor_swift_lyrics.csv")
print (df)

test_df= pd.read_table ("pokemon.txt") # load txt. data 
print (test_df)

del dtest_df # Remove object from environment 

#%%
import matplotlib as plt 

#%%
# Introduction to Computation and Programming 
# Conditional exercise
# Strings
'a'
3*4
3*'a'
3+4
'a'+'a'
new_id
'a'*'a'
'4' < 3
x = 3.9
type(x)
int(x)
# F-string
name = "TengSi"
print(f'my name is {name}')
# Input (always returns input as string)
name = input('Enter your name: ')
print(f'Are you really {name}?')
# Exercise 
birthday = input('Enter your birthday in mm/dd/yyyy: ')
print(f'You were born in the year {birthday[-4:]}.')
# Encoding 
# -*- coding: utf-8 -*-
print('Mluvíš anglicky?') 
print(' ा आप अं ेज़ी बोलते ह ?') # got some sort of error here
# stopped at pg 58

#%%
# 6.0001 Lecture 1 
pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)

# change values of radius <- another comment
# use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
area = pi*(radius**2)
print(area)


#############################
#### COMMENTING LINES #######
#############################
# to comment MANY lines at a time, highlight all of them then CTRL+1
# do CTRL+1 again to uncomment them
# try it on the next few lines below!

#area = pi*(radius**2)
#print(area)
#radius = radius + 1
#area = pi*(radius**2)
#print(area)

#############################
#### AUTOCOMPLETE #######
#############################
# Spyder can autocomplete names for you
# start typing a variable name defined in your program and hit tab 
# before you finish typing -- try it below

# define a variable
a_very_long_variable_name_dont_name_them_this_long_pls = 0

# below, start typing a_ve then hit tab... cool, right!
# use autocomplete to change the value of that variable to 1

# use autocomplete to write a line that prints the value of that long variable
# notice that Spyder also automatically adds the closed parentheses for you!

# Problem set 0 
x = int(input('Enter number x: '))
y = int(input('Enter number y: '))
print(f'X**y = {x**y}')
import numpy as np
print(f'log(x) = {int(np.log2(x))}')
