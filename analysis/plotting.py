import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def get_histograms(df):
    last_week = df[df['period']=='last week']
    previous_week = df[df['period']=='previous week']
    max_last = last_week.groupby('rating')['period'].count().max()
    max_previous = previous_week.groupby('rating')['period'].count().max()
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))
    plt.suptitle('Histograms of the ratings for the last 2 weeks')
    sns.set(style='ticks')
    sns.distplot(previous_week.rating, bins=np.arange(1,12)-0.5, kde=False, ax=ax1)
    sns.distplot(last_week.rating, bins=np.arange(1,12)-0.5, kde=False, ax=ax2)
    ax1.set(title = 'Previous week', yticks = range(max_previous+1))
    ax2.set(title = 'Last week', yticks = range(max_last+1))
    for ax in ax1, ax2:
        ax.set(xticks = range(1,12), xticklabels=np.arange(1,11), ylabel='count')

def get_boxplot(df):
    boxplot_data = df[df.period.notnull()]
    sns.boxplot(x=boxplot_data.period, y=boxplot_data.rating)
    plt.title('Summary statistics of rating for last two weeks')