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
path = (r"C:\Users\chrsm\Desktop\concatenatedDF(FinalExtendedNoJunkData).txt")
sys.stdout = Logger(path)

print("""############################################################################################################################
############################################################################################################################\n""")

print("""The functional purpose of this script is to Count - Find Null or NaN values - Print Number of Columns and any other 
necessary statistical information regarding the Dataframes under preprocessing. Also the same script will be used for the 
statistical analysis of the input .csv files that contribute to the ML experiments.\n""")

print("""############################################################################################################################
############################################################################################################################\n""")

# Importing the Dataset
# Read the original and labeled CSV file into the pandas 'df' dataframe
df = pd.read_csv((r"C:\Users\chrsm\Desktop\Extended PeX Lateral Movement Dataset [Base Files]\Final ConcatenatedDF [Normal - EoRS - EoHT]\2.3Μ Elements\concatenatedDF(FinalExtendedNoJunkData).csv"), encoding="ISO-8859-1", low_memory=False)
df.head()
print(df)

# Investigate the Label column with value_counts. The statement that follows will return the total 
# values representing each category in the 'Label' column.
print("The sum of the numerical representation of each feature of the 'Label' column has as follows:")
print(df['Label'].value_counts())

# Statements to check the soundness of each dataframe.
print(df.head())
print(df.columns[0])
print("The length of concatDF dataframe is: ", len(df))

# Statement that investigates df for null values.
obj = []
obj = df.isnull().sum()

for key,value in obj.iteritems():
    print(key,",",value)
