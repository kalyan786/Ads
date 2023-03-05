#!/usr/bin/env python
# coding: utf-8

# In[13]:


# import python libaries for ge
import pandas as pd1
import matplotlib.pyplot as plt1
import plotly.express as px1
#import plotly.graph_objs as plg


# In[2]:


# load data with skip unnecessary rows
dt1 = pd1.read_csv("API_SH.DTH.1519_DS2_en_csv_v2_4772354.csv",skiprows = 3 )
dt1


# In[3]:


#pre-processing process
# drop unnecessary columns 
# use Drop fun for delet unnecessary columns 
dt1 = dt1.drop(columns = ["1960","1961","1962","1963","1964",'1965',"1966","1967","1968",'1969',"1970",'1971',"1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1991","1992","1993",'1994',"1996","1997","1998","1999","2001","2002","2003","2004","2006","2007","2008","2009","2011","2012","2013","2014","2016","2017","2018","2019","2021","Unnamed: 66"])
dt1.head()# print top 5 rows 


# In[4]:


#pre-processing process
# replace null values with 0
dt1.fillna(0, inplace=True) # use fill function for replace null to zero

# after replace Null values print the modified dataframe
dt1


# In[34]:


import matplotlib

dtname = dt1.groupby("Country Name")["1990"].mean().sort_values(ascending=False).index[:11]
myax = dt1.groupby("Country Name")["1990"].mean().sort_values(ascending=False).round()[:11]

dt1.plot.kde(y = ['1990','1995','2000','2005'],figsize = (10,2))
plt1.title("Death rate in these years (% of death)")
plt1.show()


# In[ ]:





# In[31]:


# Analysis from 2010, 2015, 2020 death value and create a fun 
def plt():
    '''
    parameter:null
    
    Result: using line plot for generate highest death on 2010, 2015, 2020 from overall country. 
    when apply the lineplot on x-axis and y-aixs then return the top 6 country name,
    which is highest death on these years.
    Blue colour line shows the 2010, orange colour line shows the 2015, 
    gree colour line shows the 2020 that is highest in other years. 
    
    '''
    dt1.plot(x= "Country Name", y=['2010','2015','2020'],figsize = (20,10)) # x-axis country name, y-aixs 2010,2015,2020
    plt1.suptitle("15-19 age Death in 2010,2015,2020 (in overall world)")
    plt1.xlabel("Country Name")   # Country lable name  
    plt1.ylabel("2010 , 2015 , 2020")  #Years lable name
    plt1.xticks(rotation=-30)
    plt1.yticks(rotation=-30)
    plt1.legend()

plt()# call fun


# In[30]:


#import pandas as pd
#import matplotlib.pyplot as plt

# Compute total deaths by country
dt2 =dt1.sample(5)

dt2['Total Deaths'] = dt2['1990'] + dt2['1995'] + dt2['2000'] + dt2['2005'] + dt2['2010'] + dt2['2015'] + dt2['2020']

# Create pie chart
# fig, ax = plt.figure(figsize = (7,5))
fig = plt1.figure(figsize =(10, 7))
plt1.pie(dt2['Total Deaths'], labels=dt2['Country Name'], autopct='%1.1f%%', startangle=110)
plt1.axis('equal')
plt1.title("Total death % with five sample data")

# Display chart
plt1.show()


# In[ ]:





# In[ ]:




