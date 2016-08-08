#Topic 1  : Apply Function
#Topic 2  : Boolean Reference
#Topic 3  : get the count of missing values, and fill the missing value with the return from mode

import tushare as ts
import pandas as pd
import numpy as np

#practice the usual techniques used in Pandas

#get data set from ts

#data = ts.get_hist_data('510900', start = '2016-01-01',end='2016-08-08')
#data.to_csv('/Users/panjunwang/PycharmProjects/PythonWork/PythonLibrary/data.csv')

data = pd.read_csv('/Users/panjunwang/PycharmProjects/PythonWork/PythonLibrary/data.csv')

#Topic 1: Apply function
#get any NaN values in the data set
#print 'number of missing values percolumn'
#def num_missing(s):
#    return sum(s.isnull())
#print data.apply(num_missing,axis=0) #axis defines the method applied on each column

#Topic 2: Boolean Reference in Pandas
#selec data rows with columns values 'p_change' < 0.05 and 'close' > 0.9
#test_boolean_reference = data.loc[(data['p_change'] < 0.05) & (data['close']>0.9),:]
#print test_boolean_reference

#Topic 3: Fill in missing values
new_data = pd.read_csv('/Users/panjunwang/PycharmProjects/PythonWork/PythonLibrary/data.csv')
for i in range(1,5):
    new_data.iloc[i,2:5] = np.NaN #set high, close, low 4 np.NaN values

def num_missing(s):
    return sum(s.isnull())
#print new_data.apply(num_missing,axis=0) #axis defines the method applied on each column

print sum(new_data['close'].isnull()) #get number of missing values

#use scipy mode
from scipy.stats import mode
#mode[0] gets the most frequent number , and mode[1] gets the number count
#print mode(data['close'])[0], mode(data['close'])[1]
#fill the missing values with mode[0]

new_data['close'].fillna( mode(new_data['close'])[0][0], inplace=True)
new_data['high'].fillna( mode(new_data['high'])[0][0], inplace=True)
new_data['low'].fillna( mode(new_data['low'])[0][0], inplace=True)

print new_data.apply(num_missing, axis =0) #test whether the missing values get filled up in
