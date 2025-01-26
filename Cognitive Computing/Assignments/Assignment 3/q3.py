import pandas as pd
data = {
    'Tid': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ' Refund': ['Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No'],
    ' Marital_Status': ['Single', 'Married', 'Single', 'Married', 'Divorced', 
                        'Married', 'Divorced', 'Single', 'Married', 'Single'],
    ' Taxable_Income': ['125K', '100K', '70K', '120K', '95K', 
                        '60K', '220K', '85K', '75K', '90K'],
    ' Cheat': ['No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes']
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)
# Select rows from index 3 to 7
rows_3_to_7 = df.iloc[3:8]
print("\nRows from index 3 to 7:")
print(rows_3_to_7)

#Select rows from index 4 to 8 and columns 2 to 4
rowfrom4to8_col2to4 = df.iloc[4:9, 2:5]
print("\nRows from index 4 to 8 and columns 2 to 4:")
print(rowfrom4to8_col2to4)

#Select all rows with columns 1 to 3 (including column 3)
rowcol_1to3 = df.iloc[:, 1:4]
print("\nAll rows with columns 1 to 3:")
print(rowcol_1to3)
