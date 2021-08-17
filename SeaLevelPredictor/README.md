# Sea Level Predictor

# Run the code in Jupyter Notebook; Anaconda 3.X

# Analyzed a dataset of the global average sea level change since 1880. Used the data to predict the sea level change through year 2050.

*  The x label is "Year", the y label is "Sea Level (inches)", and the title is "Rise in Sea Level".
*  Used Pandas to import the data from epa-sea-level.csv.
*  Used matplotlib to create a scatter plot using the "Year" column as the x-axis and the "CSIRO Adjusted Sea Level" column as the y-axis.
*  Used the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit.
*  Ploted the line of best fit over the top of the scatter plot and made the line go through the year 2050 to predict the sea level rise in 2050.
*  Again plotted a new line of best fit just using the data from year 2000 through the most recent year in the dataset and made the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
