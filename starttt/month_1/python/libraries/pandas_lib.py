import numpy as np 
import pandas as pd
dict={
    "name":['A','B','C','D'],
    "marks":[8,6,10,9],
    "city":['abda','babda','cabda','dabda']
    }
df=pd.DataFrame(dict)
print(df)
df.to_csv('friends.csv')   #to convert a dataframe into CSV file
df.to_csv('friends_without_index.csv', index=False)