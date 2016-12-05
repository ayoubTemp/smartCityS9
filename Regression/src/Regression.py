'''
Created on 29 nov. 2016

@author: ASUS
'''
from pyspark import SparkConf, SparkContext
from pyspark import SQLContext
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
sparkConf = SparkConf().setAppName("Test").setMaster("local")
sc = SparkContext(conf = sparkConf)
sqlContext=SQLContext(sc)
data=pd.read_csv(r'C:\Users\ASUS\Desktop\student.csv',sep=';')
#print(data.columns)
#print(data.shape)
#print data
#dataf=pd.DataFrame(data)
#dataf=pd.DataFrame(data,columns=['school','sex','age','address','famesize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3'])
#print dataf
corr = data.corr()['failures']
#print corr
columns = data.columns.tolist()
columns = [c for c in columns if c not in ["failures", "school", "address","sex","famsize","Pstatus","Mjob","Fjob","reason","guardian"]]
target = "failures"
#print target
#print(columns.shape)
train = data.sample(frac=0.8, random_state=1)
test = data.loc[~data.index.isin(train.index)]
#print(train.shape)
#print(test.shape)
#print(train.shape)
#print(test.shape)
#model = LinearRegression()
x=train[columns]
#print x
y=train[target]
#print y
#print x
#print x.shape
#print y
#print y.shape
#print y.shape
#print x.shape
#y.reshape(316,395)
#reg=model.fit(x, y)
#predictions = model.predict(test[columns])
#er=mean_squared_error(predictions, test[target])
#print er
#print reg
from sklearn.ensemble import RandomForestRegressor

# Initialize the model with some parameters.
model = RandomForestRegressor(n_estimators=100, min_samples_leaf=10, random_state=1)
# Fit the model to the data.
model.fit(train[columns], train[target])
# Make predictions.
predictions = model.predict(test[columns])
# Compute the error.
er=mean_squared_error(predictions, test[target])
#print er
predicted= model.predict([15,3,3,2,1,0,1,0,1,0,1,0,1,3,3,2,1,1,3,5,7,5,6])
print predicted
#plt.scatter(x,y,  color='black')
#plt.plot(x, model.predict(x), color='blue', linewidth=3)
#plt.xticks(())
#plt.yticks(())
#plt.show()



