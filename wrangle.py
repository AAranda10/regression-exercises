#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
from env import host, user, password


# In[2]:


def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[3]:


def wrangle_telco():
    sql_query = """SELECT customer_id, monthly_charges, tenure, total_charges FROM customers WHERE contract_type_id = 3"""
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df.to_csv('telco_churn.csv')
    df['total_charges'] = df.total_charges.str.replace(' ', '0')
    return df


# In[ ]:




