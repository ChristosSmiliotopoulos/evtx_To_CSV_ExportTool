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
path = (r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\PreprocessingLogs\preprocessingLogsTest(221957JAN2023).txt")
sys.stdout = Logger(path)

# #################################################  dfToOHE_MinMax.py Script Part_01 ######################################################
# ###############################  Activate the commented area - Comment Part_02 of this script and execute. ###############################
# #####################  This script is responsible for the preprocessing of the finally concatenatedDF.csv logfile. #######################
# ##  The successful execution of the various statements leads to the creation of the final .csv file, that is comprised of 1872765 logs. ##

# Importing the Dataset
# Read the original and labeled CSV file, namely concatenatedDF.csv, into one newly created Pandas 
# dataframe, entitled concatDF dataframe.
# concatDF = pd.read_csv((r"C:\Users\chrsm\Desktop\Extensions to PeX Lateral Movement Dataset\concatenatedDF[Normal - EoRS - EoHT]\christoTest.csv"), encoding="ISO-8859-1", low_memory=False)
concatDF = pd.read_csv((r"C:\Users\chrsm\Desktop\pexLabeledDataset1.csv"), encoding="ISO-8859-1", low_memory=False)

# Statements to check the soundness of the dataframe, entitled concatDF.
print(concatDF.head())
print(concatDF.columns[0])
print("The length of concatDF dataframe is: ", len(concatDF))

# Drop the unwanted Unamed column of the concatDF dataframe, to avoid the existence of scrapted data, and create a new .csv file.
concatDF.drop(columns=concatDF.columns[0], 
        axis=1, 
        inplace=True)
print(concatDF.head())
print(concatDF.columns[0])
print("The length of concatDF dataframe is: ", len(concatDF))
# concatDF.to_csv(r'C:\Users\chrsm\Desktop\Extensions to PeX Lateral Movement Dataset\concatenatedDF[Normal - EoRS - EoHT]\christoTest(FinalExtendedNoJunkData).csv')
concatDF.to_csv(r'C:\Users\chrsm\Desktop\pexLabeledDataset1(NoJunkData).csv')

# #################################################  dfToOHE_MinMax.py Script Part_02 #################################################
# Re-importing the Dataset
# Read the processed and labeled CSV file, namely concatenatedDF(NoJunkData).csv, into one newly created Pandas 
# dataframe, entitled concatDFNoJunkData dataframe.
# concatDFNoJunkData = pd.read_csv((r"C:\Users\chrsm\Desktop\Extensions to PeX Lateral Movement Dataset\concatenatedDF[Normal - EoRS - EoHT]\christoTest(FinalExtendedNoJunkData).csv"), encoding="ISO-8859-1", low_memory=False)
concatDFNoJunkData = pd.read_csv((r"C:\Users\chrsm\Desktop\pexLabeledDataset1(NoJunkData).csv"), encoding="ISO-8859-1", low_memory=False)
print(concatDFNoJunkData.head())
print(concatDFNoJunkData.columns[0])
print("The length of concatDF dataframe is: ", len(concatDFNoJunkData))
print(concatDFNoJunkData.isnull().sum())

# Investigate the Label column with value_counts. The statement that follows will return the total 
# values representing each category in the 'Label' column.
print("The sum of the numerical representation of each feature of the 'Label' column has as follows:")
print(concatDFNoJunkData['Label'].value_counts())

# Creation of the 'df_selection' dataframe that is comprised of the 9 pre-selected features destinated for the upcoming ML experiments. 
df_selection = pd.DataFrame(concatDFNoJunkData, columns=['EventID', 'SystemTime', 'EventRecordID', 'Execution_ProcessID', 'Computer', 'ProcessId', 'Initiated', 'SourceIsIpv6', 'DestinationPortName', 'Label'])
# print(df_selection.head())
print(df_selection.columns[0])
print("The length of concatDF dataframe is: ", len(df_selection))

# Extraction to .csv file named 'selectedRawLabeledFeaturesNew.csv'
df_selection.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectedRawLabeledFeaturesNew.csv')
selectedRawLabeledFeaturesNewDF = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectedRawLabeledFeaturesNew.csv"), encoding="ISO-8859-1", low_memory=False)
# print(selectedRawLabeledFeaturesNewDF.head())
print(selectedRawLabeledFeaturesNewDF.columns[0])
print("The length of concatDF dataframe is: ", len(selectedRawLabeledFeaturesNewDF))
selectedRawLabeledFeaturesNewDF.drop(columns=selectedRawLabeledFeaturesNewDF.columns[0], 
        axis=1, 
        inplace=True)
print(selectedRawLabeledFeaturesNewDF.head())
print(selectedRawLabeledFeaturesNewDF.columns[0])

# Function which counts and prints the number of the dash '-' special characters within the 'DestinationPortName' column of the df_selection dataframe.
# ##################### SOS SOS SOS This line of code will throw an error in case there are no dash items to be recognised!!! ######################
print('Dash characters in DestinationPortName column: ', selectedRawLabeledFeaturesNewDF['DestinationPortName'].value_counts()['-'])

# isnull() check for the df_selection dataframe
selectedRawLabeledFeaturesNewDF.fillna("NaN", inplace = True)
print(selectedRawLabeledFeaturesNewDF.isnull().sum())
# Extraction to .csv file named 'selectedRawLabeledFeaturesNoNullNew.csv' 
selectedRawLabeledFeaturesNewDF.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectedRawLabeledFeaturesNoNullNew.csv")

# The code that follows will drop() all the lines with the dash ('-') value related to the 'DestinationPortName' feature.
selectedRawLabeledFeaturesNewDF.drop(selectedRawLabeledFeaturesNewDF[(selectedRawLabeledFeaturesNewDF['DestinationPortName'] == '-')].index, inplace=True)

# Extraction to .csv file named 'selectedRawLabeledFeaturesNoDashedFileNew.csv'. This file will be the final with no null values and no dash (-) values upon which 
# the OHE and MinMac techniques will be applied.
selectedRawLabeledFeaturesNewDF.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectedRawLabeledFeaturesNoNullNoDashedFileNew.csv")

# Selection of the df_selection dataframe with only the dash 'SystemTime' and 'UtcTime' columns of the df_selection dataframe being selected.
# To avoid the Pandas.to_datetime() warning 'A value is trying to be set on a copy of a slice from a DataFrame', the copy() function is used
# successfully.
df_timeDate = selectedRawLabeledFeaturesNewDF[['SystemTime', 'Label']].copy()
print(df_timeDate.head())
print(df_timeDate.columns[0])
print("The length of concatDF dataframe is: ", len(selectedRawLabeledFeaturesNewDF))

df_timeDate.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectionTimeDateSOSNew.csv")

# Manipulate the datetime columns by looking at the first 5 rows of SystemTime and UtcTime features.
print(df_timeDate['SystemTime'].head())

# The two lines of code that follow are responsible for the devide of 'SystemTime' feature, into two different elements, 
# namely the 'Date' and the 'Time' respectively. With the same line the two special characters 'T' and 'Z' are also eliminated.
df_timeDate['SystemTime'] = pd.to_datetime(df_timeDate['SystemTime'], format = '%Y-%m-%dT%H:%M:%S.%fZ', errors = 'coerce')
print(df_timeDate['SystemTime'])
print('###################### ALERT MESSAGE: The number of df_timeDate dataframe elements is: ', len(df_timeDate), ' ######################')

# The lines of code that follow deal with the reduction of the precision regarding pandas timestamp dataframe.
# # df_timeDate['SystemTime'] = pd.to_datetime(df_timeDate['SystemTime']).dt.floor('S')
df_timeDate['SystemTime'] = df_timeDate['SystemTime'].astype('datetime64[s]')
print(len(df_timeDate))
print('###################### ALERT MESSAGE: The number of df_timeDate dataframe elements is: ', len(df_timeDate), ' ######################')
print(df_timeDate['SystemTime'].head())

# One more time the df_timeDate['SystemTime'] dataframe is checked for the possibility of null elements. An assertion statement is also created.]
print('###### ALERT MESSAGE: The number of df_timeDate dataframe null or Nan elements is: ', df_timeDate.isnull().sum(), ' ######')
assert df_timeDate['SystemTime'].isnull().sum() == 0, 'missing SystemTime dates'

# The df_timeDate['SystemTime'] dataframe is then extracted to a more easily manipulated .csv format. 
df_timeDate.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectionTimeDateToTimeDateNew.csv")

# Basically you can break apart the date and get the year, month, week of year, day of month, 
# hour, minute, second, etc. You can also get the day of the week (Monday = 0, Sunday = 6). 
# Note be careful with week of year because the first few days of the year may be 53 if that week 
# begins in the prior year. Let’s apply some of these properties to both of our datetime columns.

df_timeDate['SystemTime_year'] = df_timeDate['SystemTime'].dt.year
df_timeDate['SystemTime_month'] = df_timeDate['SystemTime'].dt.month
df_timeDate['SystemTime_week'] = df_timeDate['SystemTime'].dt.week
df_timeDate['SystemTime_day'] = df_timeDate['SystemTime'].dt.day
df_timeDate['SystemTime_hour'] = df_timeDate['SystemTime'].dt.hour
df_timeDate['SystemTime_minute'] = df_timeDate['SystemTime'].dt.minute
df_timeDate['SystemTime_day_of_week'] = df_timeDate['SystemTime'].dt.day_of_week

print(df_timeDate[['SystemTime', 'SystemTime_year', 'SystemTime_month', 'SystemTime_week', 
'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute', 'SystemTime_day_of_week']].head())

print(df_timeDate.head())
# In df_timeDate_Limited the SystemTime column has been deleted.
df_timeDate_Limited = df_timeDate[['SystemTime_year', 'SystemTime_month', 'SystemTime_week', 
'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute', 'SystemTime_day_of_week', 'Label']].copy()

print(df_timeDate_Limited.head())

# The df_timeDate['SystemTime'] dataframe is then extracted to a more easily manipulated .csv format. 
df_timeDate_Limited.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectionTimeDateToTimeDateLimitedNew.csv")

# ###########################################################################################################################################################################
# Two new dataframes are created based on the two previously created selectedRawLabeledFeaturesNoNullNoDashedFileNew.csv and selectionTimeDateToTimeDateLimitedNew.csv files.
# The dataframes are named df3 and df5 respectively and will be used for their extraction the two files labeled as df3NoNullNoDushedFeaturesLabeledNew.csv and 
# df5NoNullNoDushedTimeFeaturesLabeledNew.csv respectively. Both .csv files will be concatenated in order to be finally processed with OHE and MinMax algorithms each.
# ###########################################################################################################################################################################

# # In the chunk of code that follows two new dataframe will be created in order to be used as elements to be merged into the final set of logs 
# # upon which the OHE and MinMax techniques will finally be applied.

df1_FeatureSelection = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectedRawLabeledFeaturesNoNullNoDashedFileNew.csv"), encoding="ISO-8859-1", low_memory=False)
print(df1_FeatureSelection.columns[0])
df3 = df1_FeatureSelection.iloc[: , 1:]
print("df1_FeatureSelection will be followed: ")
print(df3.head())
print(df3.columns[0])
df3.fillna("NaN", inplace = True)
print(df3.isnull().sum())
print(len(df3))
df3.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\df3NoNullNoDushedFeaturesLabeledNew.csv")

df2_TimeFeatures = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\selectionTimeDateToTimeDateLimitedNew.csv"), encoding="ISO-8859-1", low_memory=False)
print(df2_TimeFeatures.columns[0])
df5 = df2_TimeFeatures.iloc[: , 1:]
print("df2_TimeFeatures will be followed: ")
print(df5.head())
print(df5.columns[0])
df5.fillna("NaN", inplace = True)
print(df5.isnull().sum())
print(len(df5))
df5.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\df5NoNullNoDushedTimeFeaturesLabeledNew.csv")


# ###########################################################################################################################################################################
# The final part of this large script is responsible for the OHE and MinMax transformation of the two previously extracted with the same script .csv files, namely 
# df3NoNullNoDushedFeaturesLabeled.csv and df5NoNullNoDushedTimeFeaturesLabeled.csv respectively. The two files are firstly concatenated into one file and then each of the 
# desired features is manipulated as OHE or MinMax depending the authors perspective on the subject.
# ###########################################################################################################################################################################

# Importing the Dataset
# Read the two original and labeled CSV files, namely df3NoNullNoDushedFeaturesLabeled.csv and df5NoNullNoDushedTimeFeaturesLabeled.csv, into two newly created Pandas 
# dataframes, entitled df1Features and df2TimeFeatures dataframes respectively.
df1Features = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\df3NoNullNoDushedFeaturesLabeledNew.csv"), encoding="ISO-8859-1", low_memory=False)
df2TimeFeatures = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\df5NoNullNoDushedTimeFeaturesLabeledNew.csv"), encoding="ISO-8859-1", low_memory=False)

print(df1Features.columns[0])
print(df1Features.columns[1])
print(df2TimeFeatures.columns[0])
print(df2TimeFeatures.columns[1])

df1Features.drop(columns=df1Features.columns[0], 
        axis=1, 
        inplace=True)

df1Features.drop(columns=df1Features.columns[1], 
        axis=1, 
        inplace=True)

df2TimeFeatures.drop(columns=df2TimeFeatures.columns[0], 
        axis=1, 
        inplace=True)

print(df1Features.columns[0])
print(df1Features.columns[1])
print(df2TimeFeatures.columns[0])
print(df2TimeFeatures.columns[1])

# Statements to check the soundness of the two created dataframes, entitled df1Features and df2TimeFeatures dataframes respectively.
print(df1Features.head())
print(len(df1Features))
print(df2TimeFeatures.head())
print(len(df2TimeFeatures))

# The 'Label' and 'UtcTime' columns are dropped from the original df1Features dataframe.
df1Features = df1Features.drop(['Label'], axis=1)
print(df1Features)

# The two dataframes, entitled df1Features and df2TimeFeatures dataframes respectively, are concatenated with the pd.concat() function of the pandas framework. 
# A few test are printed on terminals screen to show the most relevant statistics.
result = pd.concat([df1Features, df2TimeFeatures], axis=1)
print(result)
print(len(result))
print(result.columns)
print('The new merged dataframe from df1Features and df2TimeFeatures dataframes has :', len(result.columns), ' column names.')
result.to_csv(r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\mergedDFConcatDerivedNew.csv")

# One Hot Encoding algorighm is applied upon the categorical features of the concatenated 'result' dataframe or 'mergedDFConcatDerived.csv' file. 
mergedDF3 = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\mergedDFConcatDerivedNew.csv"), encoding="ISO-8859-1", low_memory=False)
print(mergedDF3.isnull().sum())
# mergedDF3.fillna("NaN", inplace=True)
mergedDF3 = mergedDF3.fillna(0)
print(mergedDF3.isnull().sum())
ohe = pd.get_dummies(data=mergedDF3, columns=['EventID', 'Computer', 'Initiated', 'SourceIsIpv6', 'DestinationPortName', 'SystemTime_year', 'SystemTime_month', 'SystemTime_week', 'SystemTime_day_of_week'])
print(ohe)
print(ohe.columns)
print(ohe.isnull().sum())
ohe.drop(columns=ohe.columns[0], 
        axis=1, 
        inplace=True)
# ohe.drop(columns=ohe.columns[34], 
#         axis=1, 
#         inplace=True)
print(ohe.columns)
print(ohe.isnull().sum())
print("The ohe dataframe is comprised of ", len(ohe.columns), "features.")
# The pre-processed 'ohe' dataframe is then extracted to the 'ohePreProcessedDataset.csv' file.
ohe.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\ohePreProcessedDatasetNew.csv')

# MinMax Scaling algorighm is applied upon the numerical features of the concatenated 'result' dataframe or 'mergedDFConcatDerived.csv' file. 
scaler = MinMaxScaler()
minMaxScaled = ohe
minMaxScaled[['EventRecordID', 'Execution_ProcessID', 'ProcessId', 'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute']] = scaler.fit_transform(ohe[['EventRecordID', 'Execution_ProcessID', 'ProcessId', 'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute']])
print(minMaxScaled.columns)
print(len(minMaxScaled.columns))
print(minMaxScaled.isnull().sum())
print("The minMaxScaled dataframe is comprised of ", len(minMaxScaled.columns), "features.")
# The pre-processed 'ohe' dataframe is then extracted to the 'minMaxScaledPreProcessedDataset.csv' and the 'oheMinMaxPreProcessedDataset.csv' files.
minMaxScaled.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\minMaxScaledPreProcessedDatasetNew.csv')
minMaxScaled.to_csv(r'C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\newExtendedSchema\oheMinMaxPreProcessedDatasetNew.csv')