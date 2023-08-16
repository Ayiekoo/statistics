#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import matplotlib.pyplot as plt


# In[27]:


# Create separate datasets for hemoglobin levels and STO2
data = {
    "Time in hours": [0, 72, 96, 120],
    "Average Hemoglobin": [15.02, 15.94, 16.02, 16.94],
    "Mean Hemoglobin": [15.04, 15.95, 16, 16.95],
    "Average STO2": [62.68, 66.06, 68.13, 71.15],
    "Mean STO2": [62.72, 66.1, 68.3, 70.94]
}

df = pd.DataFrame(data)

# Set "Time in hours" as index
df.set_index("Time in hours", inplace=True)

# Visualize hemoglobin levels using a line graph
hemoglobin_df = df[["Average Hemoglobin", "Mean Hemoglobin"]]
hemoglobin_df.plot(kind="line", marker="o")
plt.title("Hemoglobin Levels Over Time")
plt.xlabel("Time in hours")
plt.ylabel("Hemoglobin Levels")
plt.grid(True)
plt.legend()
plt.show()

# Visualize STO2 levels using a bar graph
sto2_df = df[["Average STO2", "Mean STO2"]]
sto2_df.plot(kind="bar")
plt.title("STO2 Levels Over Time")
plt.xlabel("Time in hours")
plt.ylabel("STO2 Levels")
plt.grid(True)
plt.legend()
plt.show()


# In[28]:


import matplotlib.pyplot as plt


# In[29]:


# Data
pH = [7.15, 7.35, 7.22, 7.3, 7.1, 7.38, 7.28, 7.2, 7.42, 7.32,
      7.12, 7.25, 7.18, 7.4, 7.33, 7.28, 7.05, 7.3, 7.27, 7.39,
      7.19, 7.36, 7.17, 7.41, 7.33, 7.22, 7.05, 7.31, 7.16, 7.37,
      7.28, 7.08, 7.22, 7.33, 7.19, 7.34, 7.09, 7.4, 7.29, 7.12,
      7.35, 7.16, 7.24, 7.08, 7.36, 7.21, 7.28, 7.01, 7.31, 7.06,
      7.25, 7.29, 7.22, 7.4, 7.28, 7.18, 7.33, 7.35, 7.12, 7.3,
      7.08, 7.42, 7.32, 7.18, 7.2, 7.15, 7.38, 7.28, 7.1, 7.25,
      7.32, 7.12, 7.18, 7.3, 7.33, 7.05, 7.22, 7.4, 7.28, 7.08,
      7.36, 7.3, 7.33, 7.37, 7.24, 7.18, 7.35, 7.25, 7.42, 7.28,
      7.3, 7.08, 7.15, 7.32, 7.4, 7.25, 7.22, 7.18]

BOS = [60, 73, 80, 70, 65, 85, 73, 78, 88, 72, 68, 82, 74, 90, 77, 69, 55, 79, 71, 83,
       62, 87, 76, 84, 74, 59, 45, 70, 58, 82, 67, 50, 63, 72, 57, 76, 48, 86, 68,
       53, 80, 59, 67, 50, 78, 61, 70, 45, 73, 52, 80, 70, 75, 90, 68, 56, 81, 75,
       65, 72, 62, 88, 79, 59, 77, 60, 83, 69, 50, 82, 72, 53, 56, 85, 77, 45, 80,
       86, 73, 87, 87, 70, 74, 82, 67, 56, 75, 76, 92, 69, 79, 50, 60, 78, 90, 74,
       75, 56]

# Create a line graph
plt.figure(figsize=(10, 6))
plt.plot(pH, label='pH')
plt.plot(BOS, label='BOS')
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.title('pH and BOS Data')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




