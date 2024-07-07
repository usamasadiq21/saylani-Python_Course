import pandas as pd


#  1. Creating Pandas-Series(column), it is a 1D column which holds data of different types..
# new_series = [1,5,99,'usama', True, 11.56]
# print(pd.Series(new_series))


# 2. Getting data row-wise using indexing.
# second_series = [1,22,63,79,28,70,99]
# second_series = pd.Series(second_series)
# print(second_series[3])

# 3. Creating our own indexing for the Series.

third_series = [32,65,4,96,42,88,17,9801,6432]
third_series = pd.Series(third_series, index=['A', 'B','C','D','E','F','G','H','I'])
print(third_series)

# 4. Making series in Dictionary
dict_series = {'Day1': 230, 'Day2': 120, 'Day3': 450}
dict_series = pd.Series(dict_series)
print(dict_series) 

# 4. Getting Data from Dictionary using Indexing.
dict_series = {'Day1': 230, 'Day2': 120, 'Day3': 450}
dict_series = pd.Series(dict_series)
print(dict_series['Day2']) 

# DATAFRAMES:
# Data sets in python are usually multidimensional tables, and they are called DataFrames.
# Series are only columns and DataFrames are whole tables.

# Below we will create DataFrames using 2 or Series.

data_frame = {'cal': [458,550,230,100,230], "duration": [20,40,80,96,36]}
data_frame = pd.DataFrame(data_frame)
print(data_frame)











