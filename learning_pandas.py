import pandas as pd


#  1. Creating Pandas-Series(column), it is a 1D column which holds data of different types..
# new_series = [1,5,99,'usama', True, 11.56]
# print(pd.Series(new_series))


# 2. Getting data row-wise using indexing.
# second_series = [1,22,63,79,28,70,99]
# second_series = pd.Series(second_series)
# print(second_series[3])

# 3. Creating our own indexing for the Series.

# third_series = [32,65,4,96,42,88,17,9801,6432]
# third_series = pd.Series(third_series, index=['A', 'B','C','D','E','F','G','H','I'])
# print(third_series)

# 4. Making series in Dictionary
# dict_series = {'Day1': 230, 'Day2': 120, 'Day3': 450}
# dict_series = pd.Series(dict_series)
# print(dict_series) 

# 4. Getting Data from Dictionary using Indexing.
# dict_series = {'Day1': 230, 'Day2': 120, 'Day3': 450}
# dict_series = pd.Series(dict_series)
# print(dict_series['Day2']) 

# 5. DATAFRAMES:
# Data sets in python are usually multidimensional tables, and they are called DataFrames.
# Series are only columns and DataFrames are whole tables.

# Below we will create DataFrames using 2 or Series.

# data_frame = {'cal': [458,550,230,100,230], "duration": [20,40,80,96,36]}
# data_frame = pd.DataFrame(data_frame)
# print(data_frame)

# 5.A) Using "loc" attribute

# data_frame = {'cal': [458,550,230,100,230],"age":[13,28,47,33,90], "duration": [20,40,80,96,36]}
# data_frame = pd.DataFrame(data_frame)
# print(data_frame)

# A slight difference b/w two below lines but results are same.. 
# print(data_frame.loc[0:1]) 
# print(data_frame.loc[[0,1]])

# In .loc[], we need to define our columns by names.
# SYNTAX FOR .loc[rows, ['colName-1', 'colName-2']] 
    # 1. rows can also be mention through slicing.
#print(data_frame.loc[1:3, ['cal', 'duration']])   # give rows from 1-3 of columns 'cal', 'duration'.
#print(data_frame.loc[[0,4], ['cal', 'duration']])   # give rows at index 0 and 4 of columns 'cal', 'duration'.



# In .iloc[], we can call our columns by indexing.
# SYNTAX FOR .iloc[rows-index, col-index] 

# print(data_frame.iloc[0:3, :]) # Return row from 0-3, and all columns.
# print(data_frame.iloc[1:4, 1:3])


load_data = pd.read_csv('./data.csv')
# print(load_data) # this line will show 5 line of starting and 5 lines of ending.
print(load_data.to_string())  # This line will give all roes of dataset.


