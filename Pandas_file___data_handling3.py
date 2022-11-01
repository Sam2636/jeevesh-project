#we will revoiew the 'path' module in this document
#'path' is a sub-module or method within the 'OS' module ....
#and unlike the 'listdir' or 'getcwd' os methods we have seen before...
#'path' allows us to slice and dice, add and combine the various elements of the full path directory to a data file


#IMPORTANT... IMPORTANT... IMPORTANT
#the path module combined with the other 'os' methods we have reviewed before...
#can be crucial tools for INTERACTIVE modules and functions

#let's start
#please review the comments preceding the code blocks


# a very basic dataframe import
#AGAIN....IMPORTANT... IMPORTANT... IMPORTANT
#please replace the dots, i.e. '....', in the codes below with actual file/folder/directory paths 

import os
import pandas as pd

data1 = pd.read_csv('C:/Users/...Documents/Test_Python/5P19/cars.csv')

print(data1.columns)




#we now start various 'path' modules, we use only a few of the many available 'path' modules below
#please note carefully the outputs of the two 'basename' codes...
#as well as the outputs for the three 'dirname' codes

print(os.path.basename('C:/Users/.../Documents/Test_Python/5P19'))

print(os.path.basename('C:/Users/.../Documents/Test_Python/5P19/cars.csv'))

print(os.path.dirname('C:/Users/.../Documents/Test_Python/5P19/cars.csv'))

print(os.path.dirname('C:/Users/.../Documents/Test_Python/5P19/'))

print(os.path.dirname('C:/Users/.../Documents/Test_Python/5P19'))


#this one chnages the awful forward slashes to the familiat backslshes used in windows directories
print (os.path.normpath('C:/Users/.../Documents/Test_Python/5P19'))



#you can also pass the value of a "basename" or 'dirname' module output to a variable

x = os.path.basename('C:/Users/...Documents/Test_Python/5P19/cars.csv')

print(x)

y = os.path.dirname('C:/Users/.../Documents/Test_Python/5P19/')



#now we can print the joins of the two variables 'x' and 'y' 
# by the way there is also actually a 'join' module within 'path'
#but why complicate our lives???


#carefully examine the outputs of the two print codes below... 
print(y  + '/' + x)

print('\''  +   y  +   '/'  +   x  +  '\'')


#we will now pass the value of the entire path to a variable, and use the variable to read in a csv
z = y  + '/' + x



data2 = pd.read_csv(z)

print(data2.shape)



#we can prove that 'data1' and 'data2' are the same dataframes

if ((data1.shape) == (data2.shape)) and ((data1.columns.all()) == (data2.columns.all())):
    print('Proved once and for all...' , '\'' + 'data1' + '\'' , 'and',  '\'' + 'data2' + '\'', 'are exact same dataframes')
else:
    print('hard luck')


#by the way, will the following approach work?
#declare 'w' as follows....
#w = '\''  +   y  +   '/'  +   x  +  '\''
# data3 = pd.read_csv(w)
#will data3 be a legit dataframe, why or why not???
