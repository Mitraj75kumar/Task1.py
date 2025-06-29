import matplotlib.pyplot as plt
import numpy as np

# Data
age_groups = ['0-20 Years', '21-64 Years', '65+ Years']
population = [512, 807, 98]  # in millions
percentages = [36.1, 57.0, 6.9]  # in %

# Create figure and primary axis (for bars)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar Chart (Population)
bars = ax1.bar(age_groups, population, 
               color='skyblue', 
               edgecolor='black',
               label='Population (Millions)',
               width=0.5)

ax1.set_xlabel('Age Groups', fontsize=12)
ax1.set_ylabel('Population (Millions)', fontsize=12)
ax1.tick_params(axis='y')

# Add population labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}M',
             ha='center', va='bottom',
             fontsize=10, color='black')

# Create secondary axis (for percentages)
ax2 = ax1.twinx()
ax2.plot(age_groups, percentages, 
         color='red', 
         marker='o',
         linestyle='--',
         linewidth=2,
         markersize=8,
         label='Percentage (%)')

ax2.set_ylabel('Percentage (%)', fontsize=12)
ax2.tick_params(axis='y', colors='red')
ax2.set_ylim(0, 70)  # Adjust based on max percentage

# Add percentage labels on line points
for i, perc in enumerate(percentages):
    ax2.text(i, perc + 2,  # Offset for visibility
             f'{perc}%',
             ha='center', va='bottom',
             fontsize=10, color='red')

# Title and legends
plt.title('India Population: Age Distribution (Count vs %)', fontsize=14, pad=20)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Grid and layout
ax1.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Save: plt.savefig('india_age_combined.png', dpi=300)
