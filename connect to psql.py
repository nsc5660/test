#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install psycopg2')


# In[2]:


import psycopg2


# In[4]:


conn_string = "host='localhost' dbname='seoul_pop' user='postgres' password='nsc0203'"
conn = psycopg2.connect(conn_string)
cur=conn.cursor()


# In[12]:


# cur.execute("SELECT * FROM public.seoul_pop_test")
# result=cur.fetchall()
# result


# In[16]:


# import pandas as pd
df=pd.read_sql("SELECT * FROM public.seoul_pop_test",conn)
df


# In[25]:


df.describe()


# In[18]:


pd.read_sql("SELECT *  FROM public.seoul_pop_test where time=1",conn)


# In[20]:


pd.read_sql("SELECT *  FROM public.seoul_pop_test where total > 5",conn)


# In[ ]:




