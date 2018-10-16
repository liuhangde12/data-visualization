
# coding: utf-8

# # Data Visualization
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Toronto, Ontario, Canada**, or **Canada** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Toronto, Ontario, Canada** to Ann Arbor, USA. In that case at least one source file must be about **Toronto, Ontario, Canada**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Toronto, Ontario, Canada** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.

# In[127]:


import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'notebook')
plt.style.use('seaborn-colorblind')

data1 = pd.read_csv('emission.csv',skiprows=4)
data1 = data1[data1['Country Name']=='Canada']
emission = data1.drop(['Country Code','Indicator Name','Indicator Code','2015','2016','2017','Unnamed: 62'],axis = 1)
emission = emission.set_index('Country Name')
emission = emission.transpose()


data2 = pd.read_csv('gdp.csv',skiprows=4)
data2 = data2[data2['Country Name']=='Canada']
gdp = data2.drop(['Country Code','Indicator Name','Indicator Code','2015','2016','2017','Unnamed: 62'],axis = 1)
gdp = gdp.set_index('Country Name')
gdp = gdp/1e12
gdp = gdp.transpose()



plt.figure()

plt.subplot(2,1,1)
plt.title('Relationship between CO2 emissions and GDP in Canada',fontsize=9)
plt.plot(emission['Canada'],label='$CO_2$ emission')
plt.legend(loc=4,frameon=False,fontsize=9)
plt.gca().axis([1960,2014,10,20])
plt.ylabel('$CO_2$ emissions (tons per capita)', fontsize=9)
plt.xticks(range(1960,2015,5),emission.index[range(0,len(emission),5)],rotation='45',fontsize=9)
plt.yticks(fontsize=9)
plt.setp(plt.gca().get_xticklabels(),visible=False)
plt.subplot(2,1,2
plt.plot(gdp['Canada'],color='r',label='GDP')
plt.legend(loc=4,frameon=False,fontsize=9)
plt.gca().axis([1960,2014,0,2])
plt.xlabel('Year 1960 - 2014', fontsize=9)
plt.ylabel('GDP (trillion US$)', fontsize=9)
plt.xticks(range(1960,2015,5),gdp.index[range(0,len(emission),5)],rotation='45',fontsize=9)
plt.yticks(fontsize=9)

plt.tight_layout()

