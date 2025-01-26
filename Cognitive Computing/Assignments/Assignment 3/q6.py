import pandas as pd

employees_data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward'],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Sales'],
    'Age': [29, 34, 41, 28, 38],
    'Salary': [50000, 70000, 65000, 55000, 60000],
    'Years_of_Experience': [4, 8, 10, 3, 12],
    'Joining_Date': ['2020-03-15', '2017-07-19', '2013-06-01', '2021-02-10', '2010-11-25'],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'Bonus': [5000, 7000, 6000, 4500, 5000],
    'Rating': [4.5, 4.0, 3.8, 4.7, 3.5],
}
employees_df = pd.DataFrame(employees_data)

# a) Shape of the DataFrame
print("\n(a) Shape of employees dataset:", employees_df.shape)

# b) Summary of the DataFrame
print("\n(b) Summary of employees dataset:")
print(employees_df.info())

# c) Descriptive statistics
print("\n(c) Descriptive statistics:")
print(employees_df.describe())

# d) Display the first 5 and last 3 rows
print("\n(d) First 5 rows of employees dataset:")
print(employees_df.head())
print("\n(d) Last 3 rows of employees dataset:")
print(employees_df.tail(3))

# e) Calculations
avg_salary = employees_df['Salary'].mean()
total_bonus = employees_df['Bonus'].sum()
youngest_age = employees_df['Age'].min()
highest_rating = employees_df['Rating'].max()
print("\n(e) Average Salary:", avg_salary)
print("(e) Total Bonus:", total_bonus)
print("(e) Youngest Age:", youngest_age)
print("(e) Highest Rating:", highest_rating)

# f) Sort by Salary in descending order
sorted_df = employees_df.sort_values(by='Salary', ascending=False)
print("\n(f) Employees sorted by Salary (descending):")
print(sorted_df)

# g) Add Performance Category column
employees_df['Performance'] = employees_df['Rating'].apply(
    lambda x: 'Excellent' if x >= 4.5 else 'Good' if x >= 4.0 else 'Average'
)
print("\n(g) Employees dataset with Performance category:")
print(employees_df)

# h) Identify missing values
print("\n(h) Missing values in employees dataset:")
print(employees_df.isnull().sum())

# i) Rename Employee_ID column to ID
employees_df.rename(columns={'Employee_ID': 'ID'}, inplace=True)
print("\n(i) Employees dataset with renamed column:")
print(employees_df)

# j) Filter employees with more than 5 years of experience and in IT department
experienced = employees_df[employees_df['Years_of_Experience'] > 5]
it_department = employees_df[employees_df['Department'] == 'IT']
print("\n(j) Employees with more than 5 years of experience:")
print(experienced)
print("\n(j) Employees in IT department:")
print(it_department)

# k) Add Tax column
employees_df['Tax'] = employees_df['Salary'] * 0.1
print("\n(k) Employees dataset with Tax column:")
print(employees_df)

# l) Save the modified DataFrame to a new CSV file
output_path = ("D:\Cognitive Computing\Cognitive Assignments\Assignments\Assignment 3\modified_employees.csv")
employees_df.to_csv(output_path, index=False)
print(f"\n(l) Modified employees dataset saved to '{output_path}'")
