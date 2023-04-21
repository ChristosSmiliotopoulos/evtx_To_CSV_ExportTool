# Importing Libraries
import pandas as pd
import sklearn
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime as dt

import sys

# The class Logger() is responsible for recording the terminal's screen in the pre-defined with the
# path variable destination folder. The format of the file will be .txt.

class Logger:
 
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')
 
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
 
    def flush(self):
        self.console.flush()
        self.file.flush()

# ################  This script is responsible for the concatenation of the various dataframes of Normal, EoRS, EoHT logs. #################
# ###  The successful execution of the concat() function leads to the creation of the final .csv file, the is comprised of 1872765 logs. ###

# The path of the destination folder on which the logs.txt file will be created.
path = (r"C:\Users\chrsm\Desktop\1.8M_ExtendedLabel2\full.txt")
sys.stdout = Logger(path)

# Importing the Dataset
# Read the two original and labeled CSV files, namely df3NoNullNoDushedFeaturesLabeled.csv and df5NoNullNoDushedTimeFeaturesLabeled.csv, into two newly created Pandas 
# dataframes, entitled df1Features and df2TimeFeatures dataframes respectively.
concat1 = pd.read_csv((r"C:\Users\chrsm\Desktop\1.8M_ExtendedLabel2\0.csv"), encoding="ISO-8859-1", low_memory=False)
concat2 = pd.read_csv((r"C:\Users\chrsm\Desktop\1.8M_ExtendedLabel2\1.csv"), encoding="ISO-8859-1", low_memory=False)
# concat3 = pd.read_csv((r"C:\Users\chrsm\Desktop\Extensions to PeX Lateral Movement Dataset\T1021 [Exploitation of Remote Services]\T1021 [Malicious LM_Concat].csv"), encoding="ISO-8859-1", low_memory=False)
concat4 = pd.read_csv((r"C:\Users\chrsm\Desktop\1.8M_ExtendedLabel2\2.csv"), encoding="ISO-8859-1", low_memory=False)

# Statements to check the soundness of the two created dataframes, entitled df1Features and df2TimeFeatures dataframes respectively.
print(concat1.head())
print(concat1.columns[0])
print("The length of concat1 dataframe is: ", len(concat1))
print(concat1.isnull().sum())
# concat1.fillna("NaN", inplace=True)
concat1 = concat1.fillna(0)
print(concat1.isnull().sum())
print(concat2.head())
print(concat2.columns[0])
print("The length of concat2 dataframe is: ", len(concat2))
print(concat2.isnull().sum())
# concat2.fillna("NaN", inplace=True)
concat2 = concat2.fillna(0)
print(concat2.isnull().sum())
# print(concat3.head())
# print(concat3.columns[0])
# print("The length of concat3 dataframe is: ", len(concat3))
# print(concat3.isnull().sum())
# # concat3.fillna("NaN", inplace=True)
# concat3 = concat3.fillna(0)
# print(concat3.isnull().sum())
print(concat4.head())
print(concat4.columns[0])
print("The length of concat4 dataframe is: ", len(concat4))
print(concat4.isnull().sum())
# concat4.fillna("NaN", inplace=True)
concat4 = concat4.fillna(0)
print(concat4.isnull().sum())

# The two dataframes, entitled df1Features and df2TimeFeatures dataframes respectively, are concatenated with the pd.concat() function of the pandas framework. 
# A few test are printed on terminals screen to show the most relevant statistics. Usefull link: https://stackoverflow.com/questions/41181779/merging-2-dataframes-vertically.
result = pd.concat([concat1, concat2, concat4], ignore_index=True)
print(result)
print(len(result))
print(result.columns)
print('The new merged dataframe from concat1 and concat2 dataframes has :', len(result.columns), ' column names.')

print(result.isnull().sum())

result.to_csv(r"C:\Users\chrsm\Desktop\1.8M_ExtendedLabel2\full.csv")