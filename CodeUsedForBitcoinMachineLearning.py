#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd  # reading in data
import numpy as np #needed for machine learning random seeds and such
import category_encoders as ce # just in case i need to use catagorical data
import warnings #warnings
import matplotlib.pyplot as plt # plots and visual analysis
from sklearn.model_selection import train_test_split # training and test split import
from sklearn.ensemble import RandomForestRegressor #needed to use random forest
from sklearn import metrics  #metrics for RMSE MAE and MSE


# In[3]:


Bitcoin_data = pd.read_csv('BitNas.csv') #read in the data file
Bitcoin_data=Bitcoin_data[['NasDaqopen','NasDaqClose','NasdaqLow','NasdaqHigh','NasdaqVolume','Open','High','Low','Volume','MarketCap',
'Close']] #choose the columns you want
Bitcoin_data.drop(Bitcoin_data.tail(1).index,
        inplace = True) #the nasdaq file has an empty line therefore with the nasdaq file drop the last line
X = Bitcoin_data.iloc[:,:10].values # split the data into features for learning and features for predicting
#X is used for prediction
Y = Bitcoin_data.iloc[:, 10].values #Y is the closing price of bitcoin (this is our goal to predict) 


# In[7]:


#these 3 arrays will hold each numerical average for 100 test runs for each set of trees
RMSEAVG=[]
MAEAVG=[]
MSEAVG=[]
#change this line if you want to use more or less trees this will run a set of 75 trees to a set of 250 trees
for i in range(75,251):
    print(i)
    #set the totals for each to 0
    RMSETotal=0 
    MAETotal=0
    MSETotal=0
    #this will run each set of trees for example the set of 75 trees 100 times
    for j in range (1,101):
        #split the data into training and split sets using random seed none to keep getting random splits test size is 20%
        #test_size controls the testing/training split use .3 for a 7030 split
        #random_state=np.random.seed(NONE) is used to create a random split in the data and order the data randomly each time
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state=np.random.seed(None))
        regressor = RandomForestRegressor(n_estimators=i)
        regressor.fit(X_train, Y_train)
        Y_pred = regressor.predict(X_test)
        # these three lines are used to add each metric to the total sum of each measured metric
        RMSETotal=RMSETotal+np.sqrt(metrics.mean_squared_error(Y_test, Y_pred))
        MAETotal=MAETotal+metrics.mean_absolute_error(Y_test, Y_pred)
        MSETotal=MSETotal+metrics.mean_squared_error(Y_test, Y_pred)
    #after the 100 runs each total will be divided by 100 to get the average then pushed on the array for our total averages   
    RMSEAVG.append(RMSETotal/100)
    MAEAVG.append(MAETotal/100)
    MSEAVG.append(MSETotal/100)


# In[10]:


# this example for how i get the minimum value for each array using a simple for loop
#sets the minimum to the first value in the array
min=MAEAVG[0]
n=0 # n is used as an accumulator for our minnum
sum=0 #sum is the sum of each number in MAEAVG
minnum=0 #min num is the location of the tree with the smallest  MAE for example if minnum is 2 since our tree set goes from 75 to 250
#the tree with the smallest MAE will be at 76

for i in MAEAVG:# for each result
    sum=sum+i #add the result to the sum
    n=n+1  # add 1 to the tree count
    if i < min: #if i is < 
        min=i # set the new minimum
        minnum=n
        
print(sum/176) #prints the average
print(minnum) #prints the minimum maeavg
print(min) #prints the location of the set


# In[11]:


numtrees=[]
#this for loop simply makes an array each number representing the number of trees in each set
for i in range(75,251):
    numtrees.append(i)
plt.scatter(numtrees, MAEAVG, c=RMSEAVG, cmap='Spectral') # plot the number of trees as the x axis and each MAEAvg for each 
#each corresponding set of trees
plt.colorbar()
plt.title('RMSE AVG for Each Tree')
plt.xlabel('# of trees')
plt.ylabel('RMSE AVG')
plt.show()


# In[ ]:




