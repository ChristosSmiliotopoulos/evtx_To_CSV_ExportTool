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

# The path of the destination folder on which the logs.txt file will be created.
path = (r"C:\Users\chrsm\Desktop\ExtractedFiles\mergeCSVFilesLogs.txt")
sys.stdout = Logger(path)

# Importing the Dataset
# Read the two original and labeled CSV files, namely df3NoNullNoDushedFeaturesLabeled.csv and df5NoNullNoDushedTimeFeaturesLabeled.csv, into two newly created Pandas 
# dataframes, entitled df1Features and df2TimeFeatures dataframes respectively.
df1Features = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles\Files_to_be_Merged\df3NoNullNoDushedFeaturesLabeled.csv"), encoding="ISO-8859-1", low_memory=False)
df2TimeFeatures = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles\Files_to_be_Merged\df5NoNullNoDushedTimeFeaturesLabeled.csv"), encoding="ISO-8859-1", low_memory=False)

df1Features.drop(columns=df1Features.columns[0], 
        axis=1, 
        inplace=True)

df1Features.drop(columns=df1Features.columns[1], 
        axis=1, 
        inplace=True)

df2TimeFeatures.drop(columns=df2TimeFeatures.columns[0], 
        axis=1, 
        inplace=True)

# Statements to check the soundness of the two created dataframes, entitled df1Features and df2TimeFeatures dataframes respectively.
print(df1Features.head())
print(len(df1Features))
print(df2TimeFeatures.head())
print(len(df2TimeFeatures))

# The 'Label' and 'UtcTime' columns are dropped from the original df1Features dataframe.
df1Features = df1Features.drop(['Label', 'UtcTime'], axis=1)
print(df1Features)

# The two dataframes, entitled df1Features and df2TimeFeatures dataframes respectively, are concatenated with the pd.concat() function of the pandas framework. 
# A few test are printed on terminals screen to show the most relevant statistics.
result = pd.concat([df1Features, df2TimeFeatures], axis=1)
print(result)
print(len(result))
print(result.columns)
print('The new merged dataframe from df1Features and df2TimeFeatures dataframes has :', len(result.columns), ' column names.')
result.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles\Files_to_be_Merged\mergedDFConcatDerived.csv")

# One Hot Encoding algorighm is applied upon the categorical features of the concatenated 'result' dataframe or 'mergedDFConcatDerived.csv' file. 
# mergedDF3 = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles\Files_to_be_Merged\mergedDF3.csv"), encoding="ISO-8859-1", low_memory=False)
ohe = pd.get_dummies(data=result, columns=['EventID', 'Computer', 'Initiated', 'SourceIsIpv6', 'DestinationPortName', 'SystemTime_year', 'SystemTime_month', 'SystemTime_week', 'SystemTime_day_of_week'])
print(ohe)
print(ohe.columns)
print(len(ohe.columns))
# The pre-processed 'ohe' dataframe is then extracted to the 'ohePreProcessedDataset.csv' file.
ohe.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles\Finally_Processed_Dataset\ohePreProcessedDataset.csv')

# MinMax Scaling algorighm is applied upon the numerical features of the concatenated 'result' dataframe or 'mergedDFConcatDerived.csv' file. 
scaler = MinMaxScaler()
minMaxScaled = ohe
minMaxScaled[['EventRecordID', 'Execution_ProcessID', 'ProcessId', 'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute']] = scaler.fit_transform(ohe[['EventRecordID', 'Execution_ProcessID', 'ProcessId', 'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute']])
print(minMaxScaled.columns)
print(len(minMaxScaled.columns))
# The pre-processed 'ohe' dataframe is then extracted to the 'minMaxScaledPreProcessedDataset.csv' and the 'oheMinMaxPreProcessedDataset.csv' files.
minMaxScaled.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles\Finally_Processed_Dataset\minMaxScaledPreProcessedDataset.csv')
minMaxScaled.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles\Finally_Processed_Dataset\oheMinMaxPreProcessedDataset.csv')