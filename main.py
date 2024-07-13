# 1. import the data
# 2. clean the data
# 3. split the data into training/test sets
# 4. create a model: selecting an algorithm to analyse the data
# 5. train the model
# 6. make predictions
# 7. evaluate and improve

'''Libraries used in machine learning projects:
Numpy- provides a multidimensional array
Pandas- a data analysis library that provides a concept called data frame;
        a data frame is a 2-dimensional data structure similar to an Excel spreadsheet
MatPlotLib- a two-dimensional plotting library for creating graphs on plots
Scikit-Learn- provides common algorithm like decision trees, neural networks, etc.'''

# with machine learning, we use an environment called jupyter for writing our code
# to install jupyter, we are going to use platform called Anaconda
# use jupyter notebook
# search for video game sales on www.kaggle.com
# download csv file of datasets, place it next to jupyter notebook file

# in jupyter notebook:
# import pandas as pd
# dataframe = pd.read_csv('vgsales.csv')
# dataframe


'''
# different attributes and methods:

dataframe.shape 
shows 16598 records/rows and 11 columns

dataframe.describe()
we can see the output for each segment right next to it
shows count, mean, std, min, 25%, 50%, 75%, and max for rank, year, and sales columns
we call this method to get basic statistics of our data

df.values
returns 2-D array, the square bracket indicate 
'''

'''
jupyter shortcuts:
green or blue bar on the side means edit mode or command mode, respectively 
in command mode, after we press esc, if we press h, we can see list of all the keyboard shortcuts

a- inserts new cell above current cell
b- inserts new cell below current cell
dd- to delete cell

*Note: the code executed in that cell will run, but doesnt affect the code in other cells, they will not execute
*Note: if you want to run all cells then press the Run tab and select Run All Cells

if you type dataframe. and then press tab, you will see all the attributes and methods in that object

with the cursor on the name of the method, press shift and tab, to see tooltip
that describes what the method does and what parameter it takes

same command to comment, ctrl + /
'''

# now delete all cells or create a new jupyter notebook to start project
