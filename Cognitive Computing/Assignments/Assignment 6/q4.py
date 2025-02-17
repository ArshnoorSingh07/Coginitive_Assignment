import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/AnjulaMehto/MCA/main/company_sales_data.csv"
df = pd.read_csv(url)

# 1. Line plot for total profit of all months
plt.figure(figsize=(8, 5))
sns.lineplot(x="month_number", y="total_profit", data=df, marker="o", color="b")
plt.title("Total Profit Over Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# 2. Multi-line plot for product sales data
plt.figure(figsize=(10, 6))
for col in df.columns[1:-1]:  # Skip month_number and total_profit
    sns.lineplot(x=df["month_number"], y=df[col], label=col)

plt.title("Monthly Sales of Different Products")
plt.xlabel("Month Number")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# 3. Bar chart for all features/attributes
df.plot(kind="bar", figsize=(12, 6))
plt.title("Bar Chart for All Features")
plt.xlabel("Month")
plt.ylabel("Values")
plt.legend(loc="upper right")
plt.grid(True)
plt.show()