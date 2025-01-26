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
