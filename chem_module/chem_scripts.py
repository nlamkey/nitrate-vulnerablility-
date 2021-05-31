#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib as plt

def split_clean_df(df,
                   begin_date,
                   end_date,
                   col):
    """Splits df at a date less than input date and drops NA values of a limiting column.

    Parameters
    -----------
    df : Pandas dataframe to be worked on
        A pandas dataframe indexed by datetime
    date: Tuple of 'yyyy','mm','dd'
        A tuple containing the end date for the split
    col: String
        name of limiting column to drop na values.
    


    Returns
    -----------
    split_df : Pandas dataframe
        A pandas dataframe containing all values less than end date 
        with na values from specified column dropped
    """
    
    
    split_begin_date=pd.datetime(begin_date[0],begin_date[1],begin_date[2])
    split_end_date = pd.datetime(end_date[0],end_date[1],end_date[2])
    split_df = df.loc[df.index>=split_begin_date]
    split_df = split_df.loc[split_df.index<=split_end_date]
    
    split_df = split_df[split_df[col].notnull()]

    return split_df

def plot_dis_nit(df,year,x,y):
    """Plots an x and a y variable against each other.
    Parameters
    ----------
    df: Pandas dataframe containing x and y variables
        A pandas dataframe to be plotted.
    year: string
          The year of the data that is plotted. The title in the funtion
          is specific to discharge and nitrate variables.
    x: string
        The name of the column to be plotted on xaxis
    y: string
       The name of the column to be plotted on y axis
       
    Returns
    -------
    f: matplotlib plot 
    """
    
     
    f, ax = plt.subplots(figsize=(15, 10))

    colors = {'1':'cyan','2':'lightblue',
         '3':'steelblue','4':'darkorange','5':'darkgoldenrod',
          '6':'lightcoral','7':'brown','8':'red',
         '9':'deeppink','10':'blueviolet','11':'gray','12':'blue'}


    for i, k in df.groupby('groups'):
        k.groupby('groups').plot(x=x,
                             y=y,
                             ax=ax,
                             kind='scatter',
                             color=colors[i],
                             label=i)

    ax.set_title(year+' Nitrate-Nitrite vs Discharge\nBig Sioux River Near Dell Rapids',fontsize=20)
    ax.set_xlabel('Discharge(CFS)',fontsize=15)
    ax.set_ylabel('Nitrate-Nitrite (mg/l)',fontsize=15)

#     handles, labels = ax.get_legend_handles_labels()
#     handles, labels
#     handles=[handles[1],handles[2],handles[3],handles[4],
#          handles[5],handles[6],handles[0]]
#     labels = [labels[1],labels[2],labels[3],labels[4],
#           labels[5],labels[6],labels[0]]

    ax.legend(handles, labels)
    plt.show()
    return f



