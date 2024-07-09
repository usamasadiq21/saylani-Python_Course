import pandas as pd
data = pd.read_csv('./dirtydata.csv')
# print(data.to_string())

# modify_data = data.dropna() # Removes NaN(empty) cell from the data.

# modify_data = data.fillna('USAMA')  # Filling empty cells with our own values. This code will fill all the empty cells in the entire dataset.

# If we want to fill empty cells of different columns
# data['Date'].fillna("for change in 1 col", inplace=True) # fill empty cell in Date column.
# print(data.to_string())

# We can also fill mean(), median() and mode() in the empty cells.
# Below code can be utilize for median and mode as well..
mean_of_calories = data['Calories'].mean()
data['Calories'].fillna(mean_of_calories, inplace=True)
print(data.to_string())



























