import pandas as pd
file_path = ("D:\Cognitive Computing\Cognitive Assignments\Assignments\Assignment 3\iris.csv")
iris_df = pd.read_csv(file_path)

# Delete row 4 and column 3 (column index is 2 in zero-based indexing)
iris_df_modified = iris_df.drop(index=4).drop(columns=iris_df.columns[2])

print("\nIris dataset after deleting row 4 and column 3:")
print(iris_df_modified)