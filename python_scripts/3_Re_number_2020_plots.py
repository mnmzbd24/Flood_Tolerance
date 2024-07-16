#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[54]:


#read in and format field maps
field_maps = pd.read_excel("../Data/FieldImageR_2020/2020_C5A_C5B_Plot info for UAVs.xlsx", sheet_name="Maps", skiprows=4)
field_maps
c5b_map = field_maps.copy()
c5b_map = c5b_map.iloc[37:] #:62]
c5b_map.index = c5b_map["range"]
c5b_map.columns = c5b_map.loc["pass"]
c5b_map = c5b_map.iloc[:-4]
c5b_map = c5b_map[[x for x in range(1,31)]]

plot_data = pd.read_excel("../Data/FieldImageR_2020/2020_C5A_C5B_Plot info for UAVs.xlsx", sheet_name="Plot_data_Yield")
c5b_plot_data = plot_data[plot_data["FIELD"]=="C5b"].copy()
c5b_plot_data


# In[37]:


c5b_map


# In[69]:


#read in data from QGIS grids
qGIS_nums = pd.read_csv("../Data/FieldImageR_2020/200615_DE/200615_Indices.csv")

#add range and row numbers
qGIS_nums = qGIS_nums.sort_values("ID")
ranges = [[x]*30 for x in c5b_map.index]
ranges = [x for sublist in ranges for x in sublist]
qGIS_nums["QGIS_range"] = ranges
qGIS_nums["QGIS_rows"] = list(range(1,31)) * 25

#merge with field data
qGIS_nums = qGIS_nums.merge(c5b_plot_data[["Plot","Range","Pass", "Pedigree"]], left_on=["QGIS_range","QGIS_rows"],
                            right_on=["Range","Pass"], how="left")
qGIS_nums = qGIS_nums.rename(columns={"Plot": "corrected_plot"})
qGIS_nums = qGIS_nums.drop(columns=["Range","Pass"])
qGIS_nums.to_csv("../Data/FieldImageR_2020/200615_DE/200615_Indices_corrected_plots.csv")


# In[56]:





# In[63]:


#qGIS_nums.pivot_table(index=["QGIS_range"], columns=["QGIS_rows"], values = "PlotID").loc[c5b_map.index]


# In[64]:


#qGIS_nums.pivot_table(index=["QGIS_range"], columns=["QGIS_rows"], values = "Plot").loc[c5b_map.index]


# In[ ]:




