from imports import load_data, count_halftime_appearances
from matplotlib import pyplot as plt

# Load the data
super_bowls, tv, halftime_musicians = load_data()

# Use the count_halftime_appearances function
appearances = count_halftime_appearances(halftime_musicians)

plt.style.use('ggplot')

# Plot a histogram of combined points
plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the Super Bowls with the highest and lowest combined scores
print(super_bowls[super_bowls['combined_pts'] > 70])
print(super_bowls[super_bowls['combined_pts'] < 25])
