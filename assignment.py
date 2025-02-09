import numpy as np
import pandas as pd

def create_1d_array():
    array = np.array([1, 2, 3, 4, 5])
    print(array)

    

def create_2d_array():
    array = np.arange(1, 10).reshape((3, 3))
    print(array)
    

def array_operations(arr):
    array = np.array([1, 2, 3, 4, 5])
    # Calculate mean
    mean = np.mean(array)

    # Calculate standard deviation
    std_dev = np.std(array)

    # Find max value
    max_value = np.max(array)

    # Return the results as a tuple
    results = (mean, std_dev, max_value)
    print(results)


def read_csv_file(filepath):
   dataframe = pd.read_csv(filepath)
   return dataframe
filepath = 'C:\\Users\\K3LVIN BR0WN\\Documents\\test.csv'
df = read_csv_file(filepath)
print(df)



def handle_missing_values(df):
    missing_values_count = df.isnull().sum()
    print("Missing values in each column:\n", missing_values_count)
    
   #Fill missing values with the mean of the column
    df_cleaned = df.fillna(df.mean())
    return df_cleaned

data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, 3, 4]
}
df = pd.DataFrame(data)
df_cleaned = handle_missing_values(df)
print("Cleaned DataFrame:\n", df_cleaned)
    


def select_data(df):
   selected_data = df.loc[row_indices, col_names]
   return selected_data

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)
# Select rows with index 1 and 3, and columns 'A' and 'C'
row_indices = [1, 3]
col_names = ['A', 'C']
selected_df = select_data(df, row_indices, col_names)



def rename_columns(df):
    df_renamed = df.rename(columns=new_column_names)
    return df_renamed

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Dictionary of new column names
new_column_names = {'A': 'Juma', 'B': 'Rashid', 'C': 'Hamis'}
df_renamed = rename_columns(df, new_column_names)
print(df_renamed)

