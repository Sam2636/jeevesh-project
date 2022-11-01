#pandas data and file handling codes

#IMPORTANT...IMPORTANT...IMPORTANT!!!!!!!!!!!!!
#A DATAFRAME is the basic unit of data file as handled by Python/pandas
#just like you would store data in 'Excel Sheets' or in SPSS .sav data files..
#you store data in DATAFRAMES IN PYTHON/PANDAS 

#please focus on one code block at a time
#code blocks are separateD by distinct comment sets

#please note the USE OF IMPORTS

#pandas demo 1
#creating a data file using pandas from SCRATCH 
#first create a DICTIONARY
#then, use the DataFrame method or function from Pandas to cast it as dataframe
#IMPORTANT: will need to import pnadas to begin with


import pandas
import os 

table_one = {
    'students': ['john', 'jane', 'jon'],
    'grades': ['a', 'a+', 'a++'],
    'marks': [98, 99, 100]
     }


#note the difference betwee the two print commands below
#what features did you note about a dataframe?????

print(pandas.DataFrame(table_one))
print(table_one)



#pandas demo 2
#use of aliases or synomyms for the pandas library as 'pd' 

import pandas as pd

table_one = {
    'students': ['john', 'jane', 'jon'],
    'grades': ['a', 'a+', 'a++'],
    'marks': [98, 99, 100]
     }

print(pd.DataFrame(table_one))



#pandas SERIES 
#series is another data handling tool use by pandas...
#IN ADDITION TO DATAFRAMES 

print(pd.Series(table_one))



#We will now try to get an entire excel sheet with data imported
# we will start with couple mock 'WRONG' attempts

# IMPORTANT... Please remove the wildcards i have used from the code below:
# i.e. remove ... (the dots), and use appropriate folder path
#it might be a good idea to do an import os at this point (in shell)... and then...
#print(os.getcwd())... to get the current working directory


# get csv wrong1
#wrong slashes used in file path
#THIS CODE BLOCK WILL NOT EXECUTE 


data1 = pd.read_csv('C:\Users\...\Test_Python\5p19\cars.csv')
print(data1.shape)


# get csv wrong2, another MOCK wrong code block
#wrong directory used to get the needed csv
#i.e., cars.csv IS NOT in the 5P19 folder in my specific case 

data1 = pd.read_csv('C:/Users/.../Test_Python/5p19/cars.csv')
print(data1.shape)




# get csv right
# again... please remove the wildcards i have used: i.e. ..., and use appropriate folder path
# again... it might be a good idea to do an import os at this point... and then...
#print(os.getcwd())... to get the current working directory 
#ensure the required data file, i.e. the csv, is in the current working directory


data1 = pd.read_csv('C:/Users/.../cars.csv')
print(data1.shape)




# get csv another file

data2 = pd.read_csv('C:/Users/.../data1.csv')
print(data1.shape, data2.shape)





#a good number of pandas 'methods' are being used now...
#e.g., 'shape' tells you how many rows/clumns in a dataframe
#similarly, 'columns' is another pandas 'method'
#explore all the outputs associated with different methods 


# we can even use variables to store datafile information 
x = data1.shape
print(x, type(x))

#get file info
print(data2.columns)
print(data1.columns)

print(data1)

#get more file info 1
print(data1.dtypes)

#get more file info 2
print(data1.info())
print(data2.info())


#get more file info 3
#head/tail are used to get specific rows form the dataframe
#explore different executions of head/tail
print(data2.head())
print(data2.tail())

#get more file info 4

print(data1.head(10))
print(data2.tail(13))


#get more file info 5
print(data1.describe())
print(data2.describe())


#get data info by column/row 1
#this gives you THE specific cell value 
print(data1.iloc[0,2])
print(data2.iloc[5,12])


#get data info by column/row 2
##this gives you THE specific ROWS
print(data1.iloc[0:2])
print(data2.iloc[0:12])


#get data info by column/row 3
#try to execute and understand the diffrent row/column operations
print(data1.iloc[0:2, 0:5])
print(data2.iloc[0:12, 0:4])



#create data subsets by column/row 1 
subset1_data1 = data1.iloc[0:2, 0:5]
subset1_data2 = data2.iloc[0:12, 0:4]

print(subset1_data1, '\n', subset1_data2)
print(subset1_data1.info(), subset1_data2.info())

#save the new subsetted data
#NOTE: check the current working directory for the newly saved csv's
subset1_data1.to_csv('donnytrunpy1.csv')
subset1_data2.to_csv('donnytrunpy2.csv')

print('the subsetted files were saved to the working directory')


#calculate column/row specific descriptive stats, using GROUPING COLUMN
#i am getting a new csv for this one
#using a diffrent file now (posted as data6 on Sakai

data3 = pd.read_csv('C:/Users/...5p19/example/data6.csv')
print(data3)
print(data3.info())

means_for_durations = data3.groupby('Duration')[['Pulse', 'Calories']].mean()
print(means_for_durations)

counts_for_durations = data3.groupby('Duration')[['Pulse', 'Calories']].count()
print(counts_for_durations)

max_values_for_durations = data3.groupby('Duration')[['Pulse', 'Calories']].max()
print(max_values_for_durations)



#calculate column/row specific descriptive stats, NO GROUPING COLUMN
col_means = data3[['Pulse', 'Calories']].mean()
print(col_means)

