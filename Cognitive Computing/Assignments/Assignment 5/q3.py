# using NumPy broadcasting. 
# a) Generate your unique sales dataset: 
#  Take the sum of the ASCII values of the initials of your first and last 
# name. Call this value X. (If your initials are A B → ASCII sum = 65 
# + 66 = 131 → sales = [131, 181, 231, 281, 331].) 
#  Create a NumPy array sales with values [X, X+50, X+100, X+150, 
# X+200]. 
# b) Compute your personalized tax rate as ((X % 5) + 5) / 100. 
#  Use broadcasting to apply this tax rate to each sales value. 
# c) Adjust sales based on discount: 
#  If sales < X+100, apply a 5% discount. 
#  If sales >= X+100, apply a 10% discount. 
# d) Expand sales data for multiple weeks: 
#  Create a 3×5 matrix representing three weeks of sales by stacking 
# sales three times using broadcasting. 
#  Increase sales by 2% per week using element-wise broadcasting. 

import numpy as np
first_initial=ord('A')
last_initial=ord('S')
X = first_initial+last_initial
sales = np.linspace(X, X+200, num=5, dtype=int)

tax_rate = ((X%5)+5)/100
sales_after_tax = sales*(1 - tax_rate)
print("Sales after tax:",sales_after_tax)

sales_discounted = np.where(sales < X+100, sales * 0.95, sales * 0.90)
print("Sales after discount:",sales_discounted)

sales_matrix = np.tile(sales, (3, 1)) * (1.02 ** np.arange(3).reshape(-1, 1))
print("Expanded sales data for multiple weeks:",sales_matrix)
