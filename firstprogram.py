import matplotlib.pyplot as plt

# Data
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]
colors = ['#f4ea2a', '#3299fa', '#f65cb6']

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(age_groups, population, color=colors)

# Add text labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f'{yval} Mn', ha='center', va='bottom')

# Title and labels
plt.title("India's Population Distribution by Age (2022)", fontsize=14)
plt.xlabel("Age Group")
plt.ylabel("Population (Millions)")
plt.ylim(0, max(population) + 100)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
