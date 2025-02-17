import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Subjects": ["Math", "Science", "English", "History", "Computers"],
    "Scores": [85, 90, 78, 88, 92]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot bar chart using Seaborn
plt.figure(figsize=(7, 5))
ax = sns.barplot(x="Subjects", y="Scores", data=df, palette="viridis")

# Annotate each bar
for index, row in df.iterrows():
    ax.text(index, row.Scores + 1, str(row.Scores), ha='center', fontsize=12)

# Customize
plt.title("Scores in Different Subjects")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()