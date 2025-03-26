import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = list(range(df['Year'].min(), 2051))  
    sea_level_predicted1 = [slope1 * year + intercept1 for year in years_extended1]
    plt.plot(years_extended1, sea_level_predicted1, color="red", label="Tendency 1880-2050")


    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    years_extended2 = list(range(2000,2051))
    sea_level_predicted2 = [slope2 * year + intercept2 for year in years_extended2]
    plt.plot(years_extended2, sea_level_predicted2, color="blue", linestyle="dashed", label="Tendency 2000-2050")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()