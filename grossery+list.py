
# coding: utf-8

# In[21]:


import pandas as pd
f= open("list.txt","w")
#data = ['banana','apple','fraise']
f.write("banana, apple")
f= open("list.txt","r")
print f.read()
f.close()
#print df

