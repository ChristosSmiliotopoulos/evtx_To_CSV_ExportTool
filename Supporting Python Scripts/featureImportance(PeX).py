# The code that follows is responsible for the following procedures:
# Library imports
import numpy as np
import pandas
import pandas as pd
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from matplotlib import rcParams

import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from datetime import datetime as dt
import time
import sys
import seaborn as sns

from matplotlib.ticker import FormatStrFormatter

from sklearn.decomposition import PCA

# rcParams is only here for plot stylings
rcParams['figure.figsize'] = 18, 10
rcParams['axes.spines.top'] = False
rcParams['axes.spines.right'] = False

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

start_time = time.time()

# The path of the destination folder on which the logs.txt file will be created.
# path = (r"C:\Users\chrsm\Desktop\ExtractedFiles [18 Jan 2023]\Swallow_Classification_Results\DecisionTree\2nd Set of Experiments [ExtendedDF]\dtfullLogs.txt")
path = (r"C:\Users\chrsm\Desktop\Feature Imptances Final\PCA.txt")
sys.stdout = Logger(path)

# Print the version of the sklearn library, for reasons of compatibility.
sklearn_version = sklearn.__version__
print(sklearn_version)

# Importing the Dataset
# Read the original and labeled CSV file into the pandas 'df' dataframe
df = pd.read_csv((r"D:\Personal Projects\University of the Aegean\PhD\Paper_no2\Current Work Fld [April 2023]\ExtractedFiles [07 March 2023]\newExtendedSchema [From Jan 23]\Preprocessing_Dataframes [Final Extraction]\1.75M_FinallySelected\full-csv(Evaluated Titles).csv"), encoding="ISO-8859-1", low_memory=False)
df.head()
print(df)
print('Each Label within the oheMinMaxPreProcessedDataset.csv is comprised from the following elements: ')
print(df['Label'].value_counts())

# Prepare the dataset
# Split into training and testing subsets
X = df.drop('Label', axis=1)
y = df['Label']

# Divide dataframe into training and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
print('The length of the X_train set is: ', len(X_train))
print('The length of the X_test set is: ', len(X_test))
print('The length of the y_train set is: ', len(y_train))
print('The length of the y_test set is: ', len(y_test))

# Scale features
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# # Method #1 - Get importance from coefficients
# print("""###########################################################################################################
# ////////////////////////////// # Method #1 - Get importance from coefficients /////////////////////////////
# ###########################################################################################################""")
# model = LogisticRegression()
# model.fit(X_train_scaled, y_train)
# importances = pd.DataFrame(data={
#     'Attribute': X_train.columns,
#     'Importance': model.coef_[0]
# })
# importances = importances.sort_values(by='Importance', ascending=False)

# # The statement that follows are responsible for the replacement of the negative 'Importance' and NaN values with 0.
# print(importances['Importance'])
# # importances['Importance'] = importances['Importance'].clip(lower=0).fillna(0)
# # print(importances['Importance'])

# # The statement that follows selects only the positive and 0 values and excludes the negative. 
# print(importances[importances.select_dtypes(include=[np.number]).ge(0).all(1)])
# importances = importances[importances.select_dtypes(include=[np.number]).ge(0).all(1)]

# plt.bar(x=importances['Attribute'], height=importances['Importance'], color='#087E8B')
# plt.title('Feature importances obtained from coefficients', size=18)
# plt.subplots_adjust(bottom=0.25)
# plt.margins(0.002)
# # plt.ylim(bottom=-1.5, top=1.2)
# plt.xticks(rotation = 35, fontsize=8, ha='right')
# plt.show()

# # Method #2 — Obtain importances from a tree-based model
# model = XGBClassifier(verbosity = 3)
# # model = DecisionTreeClassifier()
# # model = RandomForestClassifier(verbose=2)
# model.fit(X_train_scaled, y_train)
# importances = pd.DataFrame(data={
#     'Attribute': X_train.columns,
#     'Importance': model.feature_importances_
# })
# importances = importances.sort_values(by='Importance', ascending=False)
# print(importances['Importance'])
# importances.replace(0, np.nan, inplace=True)

# plt.bar(x=importances['Attribute'], height=importances['Importance'], color='#087E8B')
# plt.title('Feature importances obtained from XGBC classifier model.', size=18)
# plt.subplots_adjust(bottom=0.25)
# plt.margins(0.002)
# # plt.ylim(bottom=-1.5, top=1.2)
# plt.xticks(rotation = 35, fontsize=8, ha='right')
# plt.show()

pca = PCA().fit(X_train_scaled)

plt.plot(pca.explained_variance_ratio_.cumsum(), lw=3, color='#087E8B')
plt.title('Cumulative explained variance by number of principal components (PCA)', size=20)
plt.show()

loadings = pd.DataFrame(
    data=pca.components_.T * np.sqrt(pca.explained_variance_), 
    columns=[f'PC{i}' for i in range(1, len(X_train.columns) + 1)],
    index=X_train.columns
)
loadings.head()

pc1_loadings = loadings.sort_values(by='PC1', ascending=False)[['PC1']]
# display all the  rows
pandas.set_option('display.max_rows', None)
print(pc1_loadings['PC1'])
pc1_loadings = pc1_loadings[pc1_loadings.select_dtypes(include=[np.number]).ge(0.1).all(1)]
pc1_loadings = pc1_loadings.reset_index()
pc1_loadings.columns = ['Attribute', 'CorrelationWithPC1']

plt.bar(x=pc1_loadings['Attribute'], height=pc1_loadings['CorrelationWithPC1'], color='#087E8B')
plt.title('PCA loading scores (first principal component)', size=20)
plt.subplots_adjust(bottom=0.25)
plt.margins(0.002)
# plt.ylim(bottom=-1.5, top=1.2)
plt.xticks(rotation = 35, fontsize=8, ha='right')
# plt.xticks(rotation='vertical')
plt.show()