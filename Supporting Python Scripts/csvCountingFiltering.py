# Importing Libraries
import pandas as pd
import sklearn
from tqdm import tqdm

# Importing the Dataset
# Read data from CSV file into pandas dataframe

data = pd.read_csv((r"D:\GitHub\Python-Projects-Repository\PhD ML 2nd Paper [Sample Code]\PeX_Dataset [Preprocessing]\fullsetLabeled.csv"), encoding="ISO-8859-1", low_memory=False)
data.head()
# print(data)

print(len(data.index))
print(data.shape[0])
print(data.shape[1])

df1 = data[data['Label'] == 1] 
# print(df1)
print('df1 subset is comprised of ', len(df1.index), 'rows labeled as "Normal [1]".')
df1.to_csv('normalSubset.csv')

df2 = data[data['Label'] == 2] 
# print(df2)
print('df2 subset is comprised of ', len(df2.index), 'rows labeled as "Malicious [2]".')
df2.to_csv('maliciousSubset.csv')
