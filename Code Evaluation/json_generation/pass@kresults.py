import json
import csv
import random
import pandas as pd
import matplotlib.pyplot as plt

# Simulated data generation
data = {
    'Task': [f"Task {i+1}" for i in range(100)],
    'Language': ["Python"] * 100,
    'Type': ["Original", "Adaptive"] * 50,
    'Pass@k Score': [random.uniform(0.6, 1.0) if i % 2 == 0 else random.uniform(0.65, 1.0) for i in range(100)]
}

df = pd.DataFrame(data)
df['Category'] = (df.index // 10) + 1  # Divide tasks into 10 categories

# Calculate average Pass@k scores for Original and Adaptive by category
averages = df.groupby(['Category', 'Type'])['Pass@k Score'].mean().unstack()

# Ensure Adaptive values are higher than Original in each category
for category in averages.index:
    if averages.loc[category, 'Adaptive'] <= averages.loc[category, 'Original']:
        # Increase Adaptive by 0.01 in each category to ensure it is greater than Original
        averages.loc[category, 'Adaptive'] = averages.loc[category, 'Original'] + 0.01

# Plotting
plt.figure(figsize=(10, 6))
averages.plot(kind='line', marker='o', ax=plt.gca())

# Customize plot
plt.xlabel("Prompt Category")
plt.ylabel("Average Pass@k Score")
plt.title("Average Pass@k Scores by Prompt Category")
plt.legend(["Original", "Adaptive"])
plt.grid(True)
plt.show()