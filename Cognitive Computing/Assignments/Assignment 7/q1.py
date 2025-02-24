import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Part I: Randomized Sales Data Generation
roll_number = 102317161
np.random.seed(roll_number)

# Generate sales data (12 months, 4 categories)
sales_data = np.random.randint(1000, 5000, size=(12, 4))

# Convert to DataFrame
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports"]
df = pd.DataFrame(sales_data, columns=categories, index=months)

# Display first 5 rows and summary statistics
print(df.head())
print(df.describe())

# Total sales per category
total_sales_category = df.sum()
print("Total sales per category:\n", total_sales_category)

# Total sales per month
df["Total Sales"] = df.sum(axis=1)
print("Total sales per month:\n", df["Total Sales"])

# Average sales growth per category
df_growth = df[categories].pct_change().mean()
print("Average sales growth:\n", df_growth)

# Growth Rate column
df["Growth Rate"] = df["Total Sales"].pct_change() * 100

# Apply discount
if roll_number % 2 == 0:
    df["Electronics"] *= 0.9  # 10% discount
else:
    df["Clothing"] *= 0.85  # 15% discount

# Visualization
plt.figure(figsize=(10, 5))
sns.lineplot(data=df[categories], markers=True)
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(categories)
plt.show()

# Box Plot for Sales Distribution
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[categories])
plt.title("Sales Distribution by Category")
plt.show()
