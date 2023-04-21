# Importing Libraries
import pandas as pd
import sklearn
from tqdm import tqdm
import numpy as np  

# The lines of code up to variable list_of_lists are responsible for reading the rule-based policy's filters in 
# .txt form, that is included in labelling.py scripts project folder. The filters are enumerated, the lines are splitted and after 
# the file reading is closed the manipulated filtering info is stored into list_of_lists variable and printed on cmd 
# terminal's screen. 

# *.txt file opening.
a_file1 = open("D:\GitHub\Python-Projects-Repository\PhD ML 2nd Paper [Sample Code]\RBPolicy\EoRSPolicy.txt", "r")
a_file2 = open("D:\GitHub\Python-Projects-Repository\PhD ML 2nd Paper [Sample Code]\RBPolicy\EoHTPolicy.txt", "r")

# *.txt file's reading of lines and storing them in the list_of_lists variable.
lines = a_file1.read()
list_of_lists1 = lines.splitlines()

lines = a_file2.read()
list_of_lists2 = lines.splitlines()
        
# The open() .txt file is closed. 
a_file2.close()

# The contents of the list_of_lists variable are printed on terminal.
print(list_of_lists1)
print(list_of_lists2)
# print(lines)

# Importing the Dataset
# Read data from CSV file into pandas dataframe

data = pd.read_csv((r"C:\Users\chrsm\Desktop\Stefania .csv\stefaniaLogs.csv"), encoding="ISO-8859-1", low_memory=False)
data.head()

# print(data)
# print(data['CommandLine'])
# print(data['Image'])

# for loop to add a conditional label in order to label the dataset's rows based on the conditions in the rule-based policy's filters included in the 'EoRSPolicy.txt' and 'EoHTPolicy.txt'
# as "Normal [0]", "EoRS [1]" and "EoHT [2]" traffic.
count = 0 # Variable to count every row that is labeled as "1"
count1 = 0 # Variable that stores the content of the count variable and is printed in the terminal screen.
count2 = 0 # Variable to count every row that is labeled as "0"
count3 = 0 # Variable that stores the content of the count2 variable and is printed in the terminal screen.
count4 = 0 # Variable to count every row that is labeled as "2"
count5 = 0 # Variable that stores the content of the count4 variable and is printed in the terminal screen.

print(len(data.index))
print(data.shape[0])
print(data.shape[1])

for index, row in tqdm(data.iterrows(), total=data.shape[0]):
    if str(row['Image']) in list_of_lists1:
        # data.loc[index, 'Label'] = "Mal"
        data.loc[index, 'Label'] = "1"
        count +=1
        count1 = count
    elif str(row['CommandLine']) in list_of_lists1:
        # data.loc[index, 'Label'] = "Mal"
        data.loc[index, 'Label'] = "1"
        count +=1
        count1 = count
    elif str(row['Image']) in list_of_lists2:
        # data.loc[index, 'Label'] = "Mal"
        data.loc[index, 'Label'] = "2"
        count4 +=1
        count5 = count4
    elif str(row['CommandLine']) in list_of_lists2:
        # data.loc[index, 'Label'] = "Mal"
        data.loc[index, 'Label'] = "2"
        count4 +=1
        count5 = count4
    else:
        # data.loc[index, 'Label'] = "Normal"
        data.loc[index, 'Label'] = "0"
        count2 +=1
        count3 = count2

print(data)
print(count5, " malicious files have been labelled with number '2' in total!!!")
print(count1, " malicious files have been labelled with number '1' in total!!!")
print(count3, " normal files have been labelled with number '0' in total!!!")

df = pd.DataFrame(data)
# df.replace('', np.nan, inplace=True)
# df2=df.mask(df == '')
df.fillna("NaN", inplace = True)
df.to_csv('stefaniaLogsLabelled.csv')
