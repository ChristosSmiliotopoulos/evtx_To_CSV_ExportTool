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
path = (r'C:\Users\chrsm\Desktop\ExtractedFiles\christosLogs.txt')
sys.stdout = Logger(path)

# Importing the Dataset
# Read the original and labeled CSV file into the pandas 'df' dataframe
df = pd.read_csv((r"C:\Users\chrsm\Desktop\fullsetLabeled.csv"), encoding="ISO-8859-1", low_memory=False)
df.head()
# print(df)

# Investigate the Label column with value_counts. The statement that follows will return the total 
# values representing each category in the 'Label' column.
print("The sum of the numerical representation of each feature of the 'Label' column has as follows:")
print(df['Label'].value_counts())

# Creation of the 'df_selection' dataframe that is comprised of the 10 pre-selected features destinated for the upcoming ML experiments. 
df_selection = pd.DataFrame(df, columns=['EventID', 'SystemTime', 'EventRecordID', 'Execution_ProcessID', 'Computer', 'UtcTime', 'ProcessId', 'Initiated', 'SourceIsIpv6', 'DestinationPortName', 'Label'])
# print(df_selection)

# Extraction to .csv file named 'selectedRawLabeledFeatures.csv'
df_selection.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\selectedRawLabeledFeatures.csv")

# Function which counts and prints the number of the dash '-' special characters within the 'DestinationPortName' column of the df_selection dataframe.
# ##################### SOS SOS SOS This line of code will through an error in case there are no dash items to be recognised!!! ######################
# print('Dash characters in DestinationPortName column: ', df_selection['DestinationPortName'].value_counts()['-'])

# isnull() check for the df_selection dataframe
print(df_selection.isnull().sum())
df_selection['UtcTime'] = df_selection['UtcTime'].fillna(method="ffill")
df_selection['ProcessId'] = df_selection['ProcessId'].fillna(method="ffill")
df_selection['Initiated'] = df_selection['Initiated'].fillna(method="ffill")
df_selection['SourceIsIpv6'] = df_selection['SourceIsIpv6'].fillna(method="ffill")
df_selection['DestinationPortName'] = df_selection['DestinationPortName'].fillna(method="ffill")
print(df_selection.isnull().sum())

# Extraction to .csv file named 'selectedRawLabeledFeaturesNoNull.csv'
df_selection.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\selectedRawLabeledFeaturesNoNull.csv")


# The code that follows will drop() all the lines with the dash ('-') value related to the 'DestinationPortName' feature.
df_selection.drop(df_selection[(df_selection['DestinationPortName'] == '-')].index, inplace=True)
df_selection.head()
# Extraction to .csv file named 'selectedRawLabeledFeaturesNoDashedFile.csv'. This file will be the final with no null values and no dash (-) values upon which 
# the OHE and MinMac techniques will be applied.
df_selection.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\selectedRawLabeledFeaturesNoNullNoDashedFile.csv")


# Selection of the df_selection dataframe with only the dash 'SystemTime' and 'UtcTime' columns of the df_selection dataframe being selected.
# To avoid the Pandas.to_datetime() warning 'A value is trying to be set on a copy of a slice from a DataFrame', the copy() function is used
# successfully.
df_timeDate = df_selection[['SystemTime', 'Label']].copy()
print(df_timeDate)
df_timeDate.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\selectionTimeDateSOS.csv")

# Manipulate the datetime columns by looking at the first 5 rows of SystemTime and UtcTime features.
# print(df_timeDate['SystemTime'].head())

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
df_timeDate.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\selectionTimeDateToTimeDate.csv")

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

# print(df_timeDate[['SystemTime', 'SystemTime_year', 'SystemTime_month', 'SystemTime_week', 
# 'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute', 'SystemTime_day_of_week']].head())

# print(df_timeDate)
# In df_timeDate_Limited the SystemTime column has been deleted.
df_timeDate_Limited = df_timeDate[['SystemTime_year', 'SystemTime_month', 'SystemTime_week', 
'SystemTime_day', 'SystemTime_hour', 'SystemTime_minute', 'SystemTime_day_of_week', 'Label']].copy()

print(df_timeDate_Limited)

# The df_timeDate['SystemTime'] dataframe is then extracted to a more easily manipulated .csv format. 
df_timeDate_Limited.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\selectionTimeDateToTimeDateLimited.csv")

# In the chunk of code that follows two new dataframe will be created in order to be used as elements to be merged into the final set of logs 
# upon which the OHE and MinMax techniques will finally be applied.

df1_FeatureSelection = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles\selectedRawLabeledFeaturesNoNullNoDashedFile.csv"), encoding="ISO-8859-1", low_memory=False)
df3 = df1_FeatureSelection.iloc[: , 1:]
print("df1_FeatureSelection will be followed: ")
print(df3.head())
print(df3.isnull().sum())
print(len(df3))
df3.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\Files_to_be_Merged\df3NoNullNoDushedFeaturesLabeled.csv")

df2_TimeFeatures = pd.read_csv((r"C:\Users\chrsm\Desktop\ExtractedFiles\selectionTimeDateToTimeDateLimited.csv"), encoding="ISO-8859-1", low_memory=False)
df5 = df2_TimeFeatures.iloc[: , 1:]
print("df2_TimeFeatures will be followed: ")
print(df2_TimeFeatures.head())
print(df2_TimeFeatures.isnull().sum())
print(len(df2_TimeFeatures))
df5.to_csv("C:\Users\chrsm\Desktop\ExtractedFiles\Files_to_be_Merged\df5NoNullNoDushedTimeFeaturesLabeled.csv")

# ohe = pd.get_dummies(data=df_selection, columns=['EventID', 'Computer', 'Initiated', 'SourceIsIpv6', 'DestinationPortName'])
# print(ohe)


# # ohe.to_csv('oheSelectedFeatures.csv')

# # scaler = MinMaxScaler()
# # minMaxScaled = scaler.fit_transform(df_selection1)
# # print(minMaxScaled)