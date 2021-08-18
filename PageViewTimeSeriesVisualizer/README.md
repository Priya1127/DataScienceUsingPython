# Page View Time Series Visualizer

# Run the code in Jupyter Notebook; Anaconda 3.X

# For this project you will visualize time series data using a line chart, bar chart, and box plots. 

* You will see the use of Pandas, Matplotlib, and Seaborn to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03. The data visualizations will help you understand the patterns in visits and identify yearly and monthly growth.

	* Used Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the "date" column.
	* Cleaned the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
	* Created a draw_line_plot function that uses Matplotlib to draw a line chart.
	* The title is "Daily freeCodeCamp Forum Page Views 5/2016-12/2019". The label on the x axis is "Date" and the label on the y axis is "Page Views".

	* Created a draw_bar_plot function that draws a bar chart. It shows average daily page views for each month grouped by year.
	* The legend shows month labels and has a title of "Months". On the chart, the label on the x axis is "Years" and the label on the y axis is "Average Page Views".
	* Created a draw_box_plot function that uses Searborn to draw two adjacent box plots. These box plots show how the values are distributed within a given year or month and how it compares over time.
	* The title of the first chart is "Year-wise Box Plot (Trend)" and the title of the second chart is "Month-wise Box Plot (Seasonality)". The month label on bottom start at "Jan".