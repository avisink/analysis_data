from imports import load_data, count_halftime_appearances
from matplotlib import pyplot as plt

# Load the data
super_bowls, tv, halftime_musicians = load_data()

# Use the count_halftime_appearances function
appearances = count_halftime_appearances(halftime_musicians)

# Now you can use super_bowls, tv, and appearances in the current script


#  set plotting style
plt.style.use('ggplot')

# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()
plt.show()

# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
print(halftime_musicians[halftime_musicians.super_bowl <= 27])

# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
print(halftime_appearances[halftime_appearances.super_bowl > 1])
