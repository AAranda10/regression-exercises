#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


def plot_variable_pairs(df):
    g = sns.PairGrid(df)
    g.map_diag(sns.distplot)
    g.map_offdiag(sns.regplot, scatter_kws={"color": "dodgerblue"}, line_kws={"color": "orange"})
    return g


def months_to_years(df):
    df['months_to_years'] = (df.tenure / 12).round()
    df['is_tenured'] = df.months_to_years >= 1
    return df


def plot_categorical_and_continuous_vars(df , x, y):
    sns.heatmap(df.corr(), cmap = 'Purples', annot = True)
    plt.show()
    sns.swarmplot(data= df, x = x, y = y)
    plt.show()
    sns.barplot(data= df, x = x, y = y)
    plt.show()
    return x, y


# In[ ]:




