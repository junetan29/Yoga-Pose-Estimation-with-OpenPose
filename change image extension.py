#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
os.getcwd()

collection = 'C:/Users/tanju/Desktop/Original Yoga-82/3/'
path = 'C:/Users/tanju/Desktop/3/'

for i, filename in enumerate(os.listdir(collection)):
    os.rename(collection + filename, path + str(i) + ".jpg")


# In[33]:


from PIL import Image

for i in range(354, 354):
    img = Image.open('C:/Users/tanju/Desktop/Original Yoga-82/3/'+ str(i) +'.png')
    img = img.convert('RGB')
    img.save('C:/Users/tanju/Desktop/3/'+ str(i) +'.jpg')


# In[ ]:




