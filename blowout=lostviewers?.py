from imports import load_data, count_halftime_appearances
import pandas as pd
from matplotlib import pyplot as plt

# Load the data
super_bowls, tv, halftime_musicians = load_data()

# Use the count_halftime_appearances function
appearances = count_halftime_appearances(halftime_musicians)


plt.style.use('ggplot')

# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn
import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x='difference_pts', y='share_household', data=games_tv)
plt.show()
