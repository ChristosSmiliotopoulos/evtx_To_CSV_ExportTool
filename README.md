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

		- To run the script via terminal / cmd / PowerShell execute the following command depending your OS and your .evtx file location:
