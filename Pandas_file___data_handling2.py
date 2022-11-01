#creating an INTERACTIVE TOOL for prompting and helping the user get the right data file
#try to execute, understad and analyze how the code sets might be useful/helpful

print('Here we go ...')
print('\n')
import pandas as p

import os

print('OUTPUT A - Here is your working folder or directory and the directory path....')
print(os.getcwd())
print('\n')

print('OUTPUT B - Here are the files in the working directory listed above...')
print(os.listdir())
print('\n')

print('Please use the path and the selected file information from OUTPUS A & B above to enter the working file information next')
print('\n')
x = input('Please enter your file name along with complete file path now - if needed copy-paste from above, and press ENTER:',)

file1 = p.read_csv(x)

print(file1)
print('\n')
print(file1.info())
print(file1.describe())

print('What else can i do for you???? :)')


