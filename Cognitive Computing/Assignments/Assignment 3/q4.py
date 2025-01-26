import pandas as pd
file_path = 'iris.csv' 
try:
    iris_df = pd.read_csv("D:\Cognitive Computing\Cognitive Assignments\Assignments\Assignment 3\iris.csv")
    # Display the first 5 rows
    print("First five rows of the Iris dataset:")
    print(iris_df.head())
except FileNotFoundError:
    print("Error: The file 'iris.csv' was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
