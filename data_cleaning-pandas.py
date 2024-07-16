# Cleaning Data: it means fixing the bad data in your data set, Bad Data could be: empty cells, data in a wrong 
# format duplicate and wrong data.


import pandas as pd
# print(load_data) # this line will show 5 line of starting and 5 lines of ending.
data = pd.read_csv('./dirtydata.csv')
# print(data.to_string())  # This line will give all rows of dataset.
# print(data.info())
# modify_data = data.dropna() # Removes NaN(empty) cell from the data.

# modify_data = data.fillna('USAMA')  # Filling empty cells with our own values. This code will fill all the empty cells in the entire dataset.

# If we want to fill empty cells of different columns
# data['Date'].fillna("for change in 1 col", inplace=True) # fill empty cell in Date column.
# print(data.to_string())

# We can also fill mean(), median() and mode() in the empty cells using fillna().
# Below code can be utilize for median and mode as well..
# mean_of_calories = data['Calories'].mean()
# data['Calories'].fillna(mean_of_calories, inplace=True)
# print(data.to_string())



# DATA IN WRONG FORMAT

# To fix this issue we have two ways: 
# 1. Removing the rows containing wrong format data.
# 2. Convert all data in that column in the same format.

# data['Date'] = pd.to_datetime(data['Date']) # override the date column with (pd.to_datetime(data['Date']))
# print(data.to_string())

# REMOVING WRONG DATA:

# Removing wrong data from a small dataset.
# data.loc[7, 'Duration'] = 45 # setting up new value to row 7 of col 'Duration'.
# print(data)

# if we have larger-data set then we cannot select the data row by row, for that 
# we need to loop thorugh the data.

# Thats how we loop through larger dataset.

for i in data.index:
    if data.loc[i, 'Duration'] > 200:
        data.loc[i, 'Duration'] = 11.9

print(data)





































