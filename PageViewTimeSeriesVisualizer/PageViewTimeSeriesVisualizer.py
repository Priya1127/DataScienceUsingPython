import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df.set_index(df['date'])
df.index = pd.to_datetime(df.index)
df = df[(df['value']>= df['value'].quantile(0.025)) & (df['value']<= df['value'].quantile(0.975))]
df.drop(columns ='date', inplace = True)
df = df.astype(int)

def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
    fig, ax = plt.subplots()
    plt.plot(df_line.index, df_line['value'], color = 'r', linewidth = 1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.close()
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_br = df.copy()
    df_br['Year'] = df.index.year
    df_br['Month'] = df.index.month
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_br['Month'] = df_br['Month'].apply(lambda data: months[data-1])
    df_br['Month'] = pd.Categorical(df_br['Month'], categories = months)

    df_bar = pd.pivot_table(df_br, values ='value', index = 'Year',columns ='Month', aggfunc='mean')
    
    # Draw bar plot
    ax = df_bar.plot(kind = 'bar')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(months, title = 'Months')
    fig = ax.get_figure()
    fig.set_size_inches(7, 6)
    # Save image and return fig (don't change this part)
    plt.close()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (10,6))
    sns.boxplot(ax = ax1, x = df_box['year'], y = df_box['value'] )
    ax1.set(xlabel = 'Year', ylabel = 'Page Views', title = 'Year-wise Box Plot (Trend)')

    #fig, ax = plt.subplots((1,1,2), figsize=(12,6))
    sns.boxplot(ax = ax2, x= df_box['month'] , y = df_box['value'], order =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] )
    ax2.set(xlabel = 'Month', ylabel = 'Page Views', title = 'Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    plt.close()
    fig.savefig('box_plot.png')
    return fig
