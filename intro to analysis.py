from imports import load_data, count_halftime_appearances

# Load the data
super_bowls, tv, halftime_musicians = load_data()

# Use the count_halftime_appearances function
appearances = count_halftime_appearances(halftime_musicians)

# Display the first five rows of each DataFrame
print(super_bowls.head())

print(tv.head())

print(halftime_musicians.head())

# 2. Taking note of data set issues
# Summary of the TV data to inspect
tv.info()

print('\n')

# Summary of the halftime musician data to inspect
halftime_musicians.info()

from matplotlib import pyplot as plt

plt.style.use('ggplot')

# Plot a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Display the closest game(s) and biggest blowouts
print(super_bowls[super_bowls['difference_pts'] == 1])
print(super_bowls[super_bowls['difference_pts'] >= 35])

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn
import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts' , y='share_household', data=games_tv)

# Add labels and title
plt.xlabel('Point Difference')
plt.ylabel('Share of Household Watching')
plt.title('Scatter Plot with Linear Regression Fit')

# Show the plot
plt.show()
