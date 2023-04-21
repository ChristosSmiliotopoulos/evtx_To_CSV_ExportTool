# Import the necessary packages and libraries:
from array import array
from cgitb import text
import importlib
from logging import root
from operator import irshift
from tkinter.tix import Tree
import xml.etree.ElementTree as et
# from lxml import etree
import pandas as pd
import statistics as st
import numpy as np
# ################################# Pay Attention!!! #################################
# ################################# Useful Notes!!! ##################################

# The .xml file extracted through Sysmon via the .evtx original file is not recognised as
# a native xml tree that's why actions needed in order to be comptatible with this chunk
# of code, as follows: 
# - At first visit, https://codebeautify.org/xmlviewer#copy and add the tree-based structure
# in your file. When finished extract and download the file. 
# - The same transformation can be done with VSCode, notepad++, Ultraedit and SublimeText.
# - Especially when the .xml file is rather large (>21Mb) the online tree-based structure 
# implementation with https://codebeautify.org/xmlviewer#copy is not recommended as this will 
# end into "Import file Error!!".
# Sublime Text 3 should be used as follows:
#   i. With the Sublime Text 3 opened, hit ctrl+shift+p and search for "Package Control: 
#   Install Package" utility.
#   ii. In the new window that follows type "Indent XML" to install the dedicated package.
#   iii. After that with ctrl+k,f buttons the desired tree view is achieved.
# - Before you import the .xml file to be parsed into a Pandas dataframe with this script,
# the tags that follow need to be deleted (so that to be in the right level of the xml's "family"
# hierarchy). The tags are "<?xml version="1.0" encoding="utf-8" standalone="yes"?>", "<Events>", 
# "</Events>", "<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">" and  "</Event>".

# ################################# Pay Attention!!! #################################

# Only the first "<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">" and the 
# last "</Event>" tags should be retained to the .xml file, for the script to produce the right .csv file.

# Also the tags <Data Name='Version'> should be replace with <Data Name='Version2'> and 
# "</EventData><System>""
# , should be replace with:
# "</EventData>
		# <System>", without the quotes included. 
# and
# "/f[D[D[D" lines should be deleted too.

# - After that minor changes the script is ready and fully functional to produce the desired 
# Panda's dataframe.

# Enter the .xml file you want to parse into Pandas dataframe. In case, that you hit 
# enter without any input written then the newXML.xml is selected by default. The file
# is located in the projects parent folder: 
inputFile = input("Please enter your desired .xml file: ")
if len(inputFile) < 1 : inputFile = 'merged.xml'
# print(type(inputFile))

# pretty_xml() function that is included with the lxml package (Similar to xml.etree.ElementTree 
# and Minidom.):
# x = etree.parse(inputFile)
# pretty_xml = etree.tostring(x, pretty_print=True, encoding=str)
# print(pretty_xml)

# We can import this data by reading from a file:
xtree = et.parse(inputFile)
# print(type(xtree))
xroot = xtree.getroot()

# Or pass it in a variable with tostring() function:
xmlstr = et.tostring(xroot)
# print(xmlstr)

# And take it directly from a string:
root = et.fromstring(xmlstr)

# As an Element, root has a tag and a dictionary of attributes:
# print(root.tag)
# print(root.attrib)

# Test code to figure out what is the right format of a root.tag. In our case we
# have to use the '{http://schemas..../event}Event' as follows:
# if root.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}Event':
#     print("Evreka....")
# else:
#     print('Not so good effort....')

# Declaration of the my_dict dictionary that will be used as a deposit for .xml files
# numerous keys, values pairs.
my_dict = dict()
keyList1 = ['Name', 'Guid', 'EventID', 'Version', 'Level', 'Task', 'Opcode', 'Keywords', 'SystemTime', 'EventRecordID', 'Correlation', 'ProcessID', 'ThreadID', 'Channel', 'Computer', 'UserID', 'RuleName', 'UtcTime', 'ProcessGuid', 'ProcessId', 'Image', 'FileVersion', 'Description', 'Product', 'Company', 'OriginalFileName', 'CommandLine', 'CurrentDirectory', 'User', 'LogonGuid', 'LogonId', 'TerminalSessionId', 'IntegrityLevel', 'Hashes', 'ParentProcessGuid', 'ParentProcessId', 'ParentImage', 'ParentCommandLine']
# 'ChristosssCommandLine'
# for i in keyList1:
#     my_dict[i] = ['0', 'NaNNaN']

for v in my_dict.values():
    print(len(v))

# The fuction that follows adds a key-value pair to the dictionary.
# If the key already exists in the dictionary, it will associate 
# multiple values with that key instead of overwritting its value.:
def add_value(dict_obj, key, value = None):
    ''' Adds a key-value pair to the dictionary.
        If the key already exists in the dictionary, 
        it will associate multiple values with that 
        key instead of overwritting its value'''
    if key not in dict_obj:
        if value is not None:
            # dict_obj[key] = value
            # This is a draft attempt to initialize a new key with the zero value and append eventually the imported value.
            # dict_obj[key] = '0'
            # dict_obj[key].append(value)
            # SOS SOS SOS SOS SOS SOS SOS the problem with pandas is when there is only one value on the key-value set it is not
            # recognised as a dictionary list. Here we correct this bug with this little chunk of code and finally we get the result we 
            # want even for new column names.
            dict_obj[key]   = ['0', 'Chris', value]
            # dict_obj[key] = [value]
        else:
            dict_obj[key] = ['0', 'NaN']
    elif isinstance(dict_obj[key], list):
        if value is not None:
            dict_obj[key].append(value)
        else:
            dict_obj[key].append('NaN')
    else:
            if value is not None:
                dict_obj[key] = [dict_obj[key], value]
            else:
                dict_obj[key] = value

# This is the core of the scripts parsing function. At first we iterate over the root and 
# print the tag, attrib and text for each "child". The the "ch" of each root's "child" is 
# re-parsed to reveal the included in the .xml file values. For that reason, various if, elif, 
# else and for loops are utilized to reveal the "key, value" pairs that will be stored in the 
# "my_dict" dictionary.
# The ElementTree also has children nodes over which we can iterate:
for child in root:
    # print(child.tag, child.attrib, child.text)
    for ch in child:
        # print(ch.tag, ch.attrib, ch.text)
        attribDictValue = 0
        attribDictValue1 = 0
        attribDictValue2 = 0
        # The "childs" of the "System" root.tag are iterated:
        if ch.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}Data': 
            for k, v in (ch.attrib).items(): # "ch.attrib" produces an object of type dict().
                # print(k, v)
                attribDictValue = v # Due to the nature of this "ch.attrib" we choose the value "v" as column name.
                # print(attribDictValue)
                # print(ch.text) # "ch.text" is stored and printed as the actual value of each column in the Pandas Dataframe.
                add_value(my_dict, attribDictValue, ch.text) # Each value is imported through the add_value() function in my_dict.
        elif ch.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}TimeCreated' or ch.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}Security' or ch.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}Execution' or ch.tag == '{http://schemas.microsoft.com/win/2004/08/events/event}Provider':
            for k, v in (ch.attrib).items(): # "ch.attrib" produces an object of type dict().
                # print(v)
                attribDictValue1 = k # Due to the nature of this "ch.attrib" we choose the key "k" as column name.
                add_value(my_dict, attribDictValue1, v) # "ch.text" is stored and printed as the actual value of each column in the Pandas Dataframe. 
                                                        # Each value is imported through the add_value() function in my_dict.
                                                        # The "childs" of the "EventData" root.tag are iterated:
        else:
            attribDictValue2 = ch.tag
            attribDictValue2 = attribDictValue2.replace('{http://schemas.microsoft.com/win/2004/08/events/event}', '')
            add_value(my_dict, attribDictValue2, ch.text)
        max_len = max(len(l) if isinstance(l, list) else 1 for l in my_dict.values())
        print('The Max length is: ', max_len)
    for key in my_dict.keys():
        while len(my_dict[key]) < max_len - 1:
            my_dict[key].append('NaN')

# The completed "my_dict" dictionary is printed on the terminal's screen:
# print(my_dict)
keysList = list(my_dict.keys())
print(keysList)
print(my_dict)

for v in my_dict.values():
    print(len(v))

# Finally "my_dict" is formatted into a Panda's dataframe (df) and exported in a ".csv" format:
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in my_dict.items()]))

print(df)

# computing number of rows
rows = len(df.axes[0])
 
# computing number of columns
cols = len(df.axes[1])
 
print("Number of Rows: ", rows)
print("Number of Columns: ", cols)

df.to_csv('stefaniaLogs.csv')