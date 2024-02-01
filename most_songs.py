from imports import load_data, count_halftime_appearances
from matplotlib import pyplot as plt

# Load the data
super_bowls, tv, halftime_musicians = load_data()

# Use the count_halftime_appearances function
appearances = count_halftime_appearances(halftime_musicians)

# Now you can use super_bowls, tv, and appearances in the current script



# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
print((no_bands.head(15)))