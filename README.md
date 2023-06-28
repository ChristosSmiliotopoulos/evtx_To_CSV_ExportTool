# evtx_To_CSV_ExportTool (ETCExp - v1)

The enclosed script in this Github repository, is a python analyzing scripting tool dubbed "evtx_To_CSV_ExportTool" (ETCExp - v1), which caters for the parsing of voluminous Sysmon logs in .evtx format, and therefore contributes to the convertion of Windows system monitor logs to turnkey datasets, ready to be fed in .csv format into ML models. 

ETCExp - v1 was developed as part of the pre-printed paper entitled "On the detection of lateral movement through supervised machine learning and an open-source tool to create turnkey datasets from Sysmon logs" (Christos Smiliotopoulos, Georgios Kambourakis, Konstantia Barbatsalou et al. On the detection of lateral movement through supervised machine learning and an open-source tool to create turnkey datasets from Sysmon logs, 24 April 2023, PREPRINT (Version 1) available at Research Square [https://doi.org/10.21203/rs.3.rs-2845318/v1]). This portable and versatile chunk of code, is designed to overcome all the hurdles involved in the creation of turnkey unlabeled or labeled datasets in CSV format through the manipulation of EVTX Sysmon logs, as it consists a software solution able to automatize this task. This contribution is key to the Lateral Movement (LM) community given that, no pertinent Sysmon derived datasets exist, obstructing research on ML-oriented LM detection.

More specifically, Sysmon is a multipurpose service of the MS Windows OS environment and a system’s driver too. It is not included as pre-installed with any Windows OS version, and when imported it remains omnipresent with all Windows internal tasks. Sysmon monitors and gathers detailed event-oriented information that is organized in 27 distinct types of case-sensitive EventIDs, as presented in Microsoft's dedicated webpage https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon. Sysmon is by default capable of simultaneously organizing and extracting the collected logs, through the Windows Event Viewer (WEV) application, in a variety of files of multiple types, including EVTX, .xml, CSV and .txt formats respectively. Nevertheless, due to the core structure of the EVTX format files all these export formats are cumbersome to manage and abundantly unsuitable for ML techniques.

The essence of ETCExp is to provide a lightweight, portable, easily configurable and above all OS-independent command line (of IDE executable) tool that helps incident response teams and researchers to parse and make massive EVTX log files compatible to be implemented into ML algorithms. The tool can process large EVTX files very quickly; for instance, the conversion of a 1.41 GB (2.7M samples) corpus takes around 30 min.

From an OS version’s perspective, ETCExp can be executed on any mainstream platform, namely Windows 11, macOS Ventana v13.0 and Ubuntu v22.04 LTS.

The source code, along with the following: 

		- Supporting Python Scripts, 
		
		- intializationFile, 
		
		- Demo Exported .csv Files, 
		
		- LMD Datasets Collection.rar, 
		
		- Large .xml files manipulation Windows Tool.rar,

		- RBPolicy.rar and

		- README.md

can be downloaded from the tool's Github link, https://github.com/ChristosSmiliotopoulos/evtx_To_CSV_ExportTool/blob/master/ETCExp_Tool-V1.py.

# Setup

In order to re-build the source code contained in this repository there are two possible ways:

- Load it to the IDE of your choice (PyCharm or VSCode are recommended, due to their undeniable characteristics that could not be ommitted, including among the many benefits smart code completion, on-the-fly error inspection with highlighting and code refactoring). Import according to your IDE manual the referenced libraries in the main.py file, choose the relevant to your system Python version (Python 3.9.1 was the version upon which ETCExp was created) and try the tool to the .evtx file of your choice.

- On the other hand, if no IDE is chose and the reproduction of the script is going to be done via terminal, cmd or PowerShell then keep in mind the steps that follow:
  
		- python setup.py install
		
		- pip install importlib

		- pip install xml.etree.ElementTree

  		- pip install pandas

  		- pip install statistics

  		- pip install numpy

		- To run the script via terminal / cmd / PowerShell execute the following command depending your OS and your ETCExp_Tool-V1.py script location:

  			- Windows/macOS/Linux: python3 ETCExp_Tool-V1.py

- It should be noted that with this initial version of the ETCExp_Tool-V1.py, the user needs to execute two pre-processing steps regarding .evtx files. Those steps are thoroughly presented as comments within the ETCExp_Tool-V1.py script, however they are also presented in bried below and within the attached video at the bottom of this page:
 
	- At first extract the .evtx file, in the Windows-based .xml format that is provided with the utilities of Windows Event Viewer.
 
	- The .xml file extracted through Sysmon via the .evtx original file is not recognised as a native xml tree that's why actions needed in order to be comptatible with this chunk of code, as follows:

		- At first visit, https://codebeautify.org/xmlviewer#copy, upload or copy the contents of the .xml file on it and add the tree-based structure in your file. When finished extract and download the file.

		- Especially when the .xml file is rather large (>21Mb) the online tree-based structure  implementation with https://codebeautify.org/xmlviewer#copy is not recommended as this will end into "Import file Error!!".

		- Sublime Text 3 should be used as follows:
			- i. With the Sublime Text 3 opened, hit #ctrl+shift+p and search for "Package Control: Install Package" utility.

			- ii. In the new window that follows type "Indent XML" to install the dedicated package.

			- iii. After that with ctrl+k,f buttons the desired tree view is achieved.

	- PAY ATTENTION!!! There is however an easier and versatile way to add the tree structure to the extracted .xml file if you are Windows user. Download the enclosed in this repository Large .xml files manipulation Windows Tool.rar. Load the file, hit the appropriate tree-structure command and you file is ready to be parsed to the .csv equivalent.
 
	- Before you import the .xml file to be parsed into a Pandas dataframe with this script, the tags that follow need to be deleted (so that to be in the right level of the xml's `"family"` hierarchy). The tags are `<?xml version="1.0" encoding="utf-8" standalone="yes"?>`, `<Events>`, `</Events>`, `<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event>` and  `</Event>`.

	- Pay Attention!!! Only the first `<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">` and the last `</Event>` tags should be retained to the .xml file, for the script to produce the right .csv file.

 	- Pay Attention!!! Just after the first `<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">` of the manipulated - extracted .xml file, the 574 lines included in the enclosed with this repository initializationFile.xml, should be added in order to initialize the ETCExp_Tool-V1.py to create from the first lines of the .xml parsing all the necessaries for the whole process column ids. (The necessity of this step is obvious in the enclosed .mp4 video.)

	- Also the tags `<Data Name='Version'>` should be replace with `<Data Name='Version2'>` and `</EventData><System>`, should be replace with:
 
		`</EventData>`

   		`<System>`, without the quotes included. 

	- and `/f [D [D [D` lines should be deleted too.

 	- After that minor changes the script is ready and fully functional to produce the desired Panda's dataframe.
 
https://github.com/ChristosSmiliotopoulos/evtx_To_CSV_ExportTool/assets/46369046/960e2ace-bda0-4c19-a6bc-7053077302da

https://github.com/ChristosSmiliotopoulos/evtx_To_CSV_ExportTool/assets/46369046/ff201840-53e3-458d-ad27-23cb41d4dd67

https://github.com/ChristosSmiliotopoulos/evtx_To_CSV_ExportTool/assets/46369046/79ef3c2d-f3c5-49f5-8d05-35600cc4676e


