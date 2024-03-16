#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mljar-supervised


# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt
import warnings
from supervised.automl import AutoML
warnings.filterwarnings("ignore")


# In[3]:


df_train = pd.read_csv("/kaggle/input/fyp-csv/CSV/3/train.csv", header = None)
df_test = pd.read_csv("/kaggle/input/fyp-csv/CSV/3/test.csv", header = None)


# In[4]:


y_test = df_test.iloc[:,0]
x_test = df_test.iloc[:,1:]

y_train = df_train.iloc[:,0]    
x_train = df_train.iloc[:,1:]


# In[5]:


from imblearn.over_sampling import SMOTE


# In[6]:


print("Before OverSampling, counts of label '1': {}".format(sum(y_train==1)))
print("Before OverSampling, counts of label '0': {} \n".format(sum(y_train==0)))

sm = SMOTE(random_state=2)
x_train_res, y_train_res = sm.fit_resample(x_train, y_train.ravel())

print('After OverSampling, the shape of train_X: {}'.format(x_train_res.shape))
print('After OverSampling, the shape of train_y: {} \n'.format(y_train_res.shape))

print("After OverSampling, counts of label '1': {}".format(sum(y_train_res==1)))
print("After OverSampling, counts of label '0': {}".format(sum(y_train_res==0)))


# In[7]:


automl = AutoML(
    mode="Compete", 
    ml_task='multiclass_classification',
    eval_metric='accuracy',
    features_selection=False # switch off feature selection
)
automl.fit(x_train_res, y_train_res)

predictions = automl.predict(x_test) 


# In[8]:


automl.report()


# In[ ]:




