#!/usr/bin/env python
# coding: utf-8

# In[1]:


#method 1
import pandas as pd
import glob
import csv
import json
path = 'C:/Users/tanju/Desktop/3/json/test/1/*.json'
files = glob.glob(path)
output = []
output1 = []
for file in files:
    output = pd.read_json(file)
    df1 = pd.json_normalize(output['people'])
    df1['label'] = '1'
    output1.append(df1)
# now write
final = pd.concat(output1)
final.to_csv('C:/Users/tanju/Desktop/testing.csv', mode='a', index=False, header=False)


# In[292]:


# separate columns 
import pandas as pd 

#f = open("C:/Users/tanju/Desktop/2/json/test/1/00000000_keypoints.json")
df = pd.read_json(f)

df1 = pd.json_normalize(df['people'])

print(df1)
df1.to_csv('C:/Users/tanju/Desktop/2/test.csv', index=False)


# In[21]:


from glob import glob
import pandas as pd 

for filename in glob('C:/Users/tanju/Desktop/2/json/test/1/*.json'):
    f = open(filename, 'r')
    contents = pd.read_json(f)
    contents['person_id'] = 1
    f.close()
    f = open(filename, 'w')
    f.write(contents)
    f.close()


# In[114]:


import pandas as pd
import glob
import csv
import json

path = 'C:/Users/tanju/Desktop/2/json/test/1/*.json'
files = glob.glob(path)

output = []

for file in files:
    output = pd.read_json(file)
print(output)
output.to_csv('C:/Users/tanju/Desktop/2/test.csv', index=False)


# In[32]:


import json
import csv
with open('C:/Users/tanju/Desktop/2/test.csv', 'w') as file:
    with open('C:/Users/tanju/Desktop/2/json/test/1/00000000_keypoints.json', 'r') as files:
        data = json.loads(files.read())
        print(data)

        csv_file = csv.writer(file)
        for item in data:
            fields = list(item)
            csv_file.writerow(fields)


# In[82]:


import pandas as pd

#with open('C:/Users/tanju/Desktop/2/json/test/1/00000000_keypoints.json', 'r') as inputfile:
df = pd.read_json(r'C:/Users/tanju/Desktop/2/json/test/1/00000000_keypoints.json', lines=True)
print(df)
#df.to_csv('C:/Users/tanju/Desktop/2/test.csv', index=False)


    """import json
    with open('gdb.json', 'r') as datafile:
        data = json.load(datafile)
    retail = pd.DataFrame(data)"""


# In[ ]:


#method 3
# Python program to read
# json file


import json


# JSON string
a = '{"name": "Bob", "languages": "English"}'

# deserializes into dict
# and returns dict.
y = json.loads(a)

print("JSON string = ", y)
print()



# JSON file
f = open ('data.json', "r")

# Reading from file
data = json.loads(f.read())

# Iterating through the json
# list
for i in data['emp_details']:
	print(i)

# Closing file
f.close()

