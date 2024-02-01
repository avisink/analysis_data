from imports import load_data, count_halftime_appearances
from matplotlib import pyplot as plt

# Load the data
super_bowls, tv, halftime_musicians = load_data()

# Use the count_halftime_appearances function
appearances = count_halftime_appearances(halftime_musicians)



plt.style.use('ggplot')

plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls['difference_pts'] == 1])
print(super_bowls[super_bowls['difference_pts'] >= 35])
