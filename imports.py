import pandas as pd
from matplotlib import pyplot as plt

def load_data():
    # Load the CSV data into DataFrames
    super_bowls = pd.read_csv('datasets/super_bowls.csv')
    tv = pd.read_csv('datasets/tv.csv')
    halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')
    return super_bowls, tv, halftime_musicians

def count_halftime_appearances(halftime_musicians):
    # Count halftime show appearances for each musician and sort them from most to least
    halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
    halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)
    return halftime_appearances
