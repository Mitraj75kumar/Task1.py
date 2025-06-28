import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# Data for Bar chart
# -------------------------
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]
colors = ['#f4ea2a', '#3299fa', '#f65cb6']

# -------------------------
# Data for Histogram
# -------------------------
np.random.seed(42)
ages = np.random.normal(loc=35, scale=15, size=1000)
ages = np.clip(ages, 0, 90)

# -------------------------
# Create subplot figure
# -------------------------
plt.figure(figsize=(14, 6))

# -------------------------
# Bar chart on left
# -------------------------
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
bars = plt.bar(age_groups, population, color=colors)

# Add text labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 10, f'{yval:,} Mn',
             ha='center', va='bottom')

plt.title("India's Population Distribution by Age (2022)")
plt.xlabel("Age Group")
plt.ylabel("Population (Millions)")
plt.ylim(0, max(population) + 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# -------------------------
# Histogram on right
# -------------------------
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.hist(ages, bins=15, color='#3299fa', edgecolor='black', alpha=0.7)

plt.title("Sample Age Distribution Histogram")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# -------------------------
# Final adjustments
# -------------------------
plt.tight_layout()
plt.show()
