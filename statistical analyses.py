#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


data1 = pd.read_csv("C:/Users/Ayieko/Desktop/BOS.csv")
print(data1)


# In[7]:


descriptive_stats = data1.describe()
print(descriptive_stats)


# In[8]:


from scipy.stats import f_oneway
from scipy.stats import ttest_rel


# In[13]:


# Perform repeated measures ANOVA
anova_results = f_oneway(data1['0 hours'], data1['72 HOURS'], data1['96 HOURS'], data1['120 HOURS'])
print("Repeated Measures ANOVA Results:")
print("F-statistic:", anova_results.statistic)
print("p-value:", anova_results.pvalue)

# Perform pairwise t-tests
ttest_0_72 = ttest_rel(data1['0 hours'], data1['72 HOURS'])
ttest_0_96 = ttest_rel(data1['0 hours'], data1['96 HOURS'])
ttest_0_120 = ttest_rel(data1['0 hours'], data1['120 HOURS'])
ttest_72_96 = ttest_rel(data1['72 HOURS'], data1['96 HOURS'])
ttest_72_120 = ttest_rel(data1['72 HOURS'], data1['120 HOURS'])
ttest_96_120 = ttest_rel(data1['96 HOURS'], data1['120 HOURS'])

print("\nPairwise T-Test Results:")
print("0 hours vs 72 HOURS:", ttest_0_72)
print("0 hours vs 96 HOURS:", ttest_0_96)
print("0 hours vs 120 HOURS:", ttest_0_120)
print("72 HOURS vs 96 HOURS:", ttest_72_96)
print("72 HOURS vs 120 HOURS:", ttest_72_120)
print("96 HOURS vs 120 HOURS:", ttest_96_120)


# In[20]:


data2 = pd.read_csv("C:/Users/Ayieko/Desktop/stata.csv")
print(data2)


# In[21]:


descriptive_stats = data2.describe()
print(descriptive_stats)


# In[22]:


# Perform repeated measures ANOVA
anova_results = f_oneway(data2['0 hours'], data2['72 hours'], data2['96 hours'], data2['120 hours'])
print("Repeated Measures ANOVA Results:")
print("F-statistic:", anova_results.statistic)
print("p-value:", anova_results.pvalue)

# Perform pairwise t-tests
ttest_0_72 = ttest_rel(data2['0 hours'], data2['72 hours'])
ttest_0_96 = ttest_rel(data2['0 hours'], data2['96 hours'])
ttest_0_120 = ttest_rel(data2['0 hours'], data2['120 hours'])
ttest_72_96 = ttest_rel(data2['72 hours'], data2['96 hours'])
ttest_72_120 = ttest_rel(data2['72 hours'], data2['120 hours'])
ttest_96_120 = ttest_rel(data2['96 hours'], data2['120 hours'])

print("\nPairwise T-Test Results:")
print("0 hours vs 72 HOURS:", ttest_0_72)
print("0 hours vs 96 HOURS:", ttest_0_96)
print("0 hours vs 120 HOURS:", ttest_0_120)
print("72 HOURS vs 96 HOURS:", ttest_72_96)
print("72 HOURS vs 120 HOURS:", ttest_72_120)
print("96 HOURS vs 120 HOURS:", ttest_96_120)


# In[ ]:




