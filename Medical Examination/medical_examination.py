import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df_estimate = df['weight']/np.square(df['height']/100)
df['overweight'] = np.where(df_estimate > 25, 1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol']>1,1,0)
df['gluc'] = np.where(df['gluc']>1,1,0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    cat_plot = pd.melt(
      df, id_vars = ['cardio'], value_vars = ['active','alco','cholesterol', 'gluc','overweight', 'smoke']
      )

    cat_plot = pd.DataFrame(
      cat_plot.groupby(
        ['variable', 'value', 'cardio'])['value'].count()).rename(columns={'value': 'total'}).reset_index()

    g = sns.catplot(x='variable', y='total', data=cat_plot, hue='value', col='cardio', kind='bar')
    fig = g.fig
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
  df = pd.read_csv('medical_examination.csv')

    # Add 'overweight' column
  df_estimate = df['weight']/np.square(df['height']/100)
  df['overweight'] = np.where(df_estimate > 25, 1,0)
  df['cholesterol'] = np.where(df['cholesterol']>1,1,0)
  df['gluc'] = np.where(df['gluc']>1,1,0)
# Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.zeros_like(corr)
  mask[np.triu_indices_from(mask)] = True

   # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(10, 12))
  #ax = sns.heatmap(corr, mask = mask, annot=True, vmax =0.24, vmin = -0.10, center = 0.09, square= True)
  ax = sns.heatmap(corr, annot=True, fmt='.1f',mask=mask, vmin=.16, vmax=.32, center=0, square=True,linewidths=.5,cbar_kws={'shrink':.45, 'format':'%.2f'})

  # Draw the heatmap with 'sns.heatmap()'
  plt.close()
  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig