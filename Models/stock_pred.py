# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 18:52:59 2019

@author: mayank kumar
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

df=pd.read_csv('NSE-TATAGLOBAL11.csv')

df.head()


df['Date']=pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index=df['Date']

plt.figure(figsize=(16,8))
plt.plot(df['Close'],label='Closing price')

data=df.sort_index(ascending=True,axis=0)
new_data=pd.DataFrame(index=range(0,len(df)),columns=['Date','Close'])

for i in range (0,len(df)):
    new_data['Date'][i]=data['Date'][i]
    new_data['Close'][i]=data['Close'][i]
    
train=new_data[:987]
valid=new_data[987:]


#making predictions
preds=[]
for i in range(0,len(valid)):
    a=train['Close'][len(train)-248+i:].sum()
    b=a/248
    preds.append(b)
    
valid['preds']=preds

#plotting the train,close and preds
plt.plot(train['Close'])
plt.plot(valid[['Close','preds']])

