# Compress Files in IBM Sterling B2Bi
 
Samples BPs to compress files (Zip).





# Files

| File name                           |            Description of BP                                          |
|-------------------------------------|-----------------------------------------------------------------------|
| compress-files-from-filesystem.bpml | Compress files using Compress Service and File System Adapter |
| compress-files-using-cla.bpml       | Compress files using Command Line Adapter 2 and zip utility from Operating System |



# Steps to Run:

**On Server**

1) Create a directory  

```
/tmp/files2compress
```

In this directory

2) Create a file testdata1.csv with some content to compress

3) Create a file testdata2.csv with some content to compress


**On Dashboard**

1) Login o Sterling B2B Console

2) Create a new File System Adapter: **Generic_FSA_Adapter**

```
Service Type:            File System Adapter
System Name:             Generic_FSA_Adapter
Description:             Generic FSA Adapter used on SFG
Group Name:              None
Collection folder:       c:\
Filename filter          *.xyz
Collect files from sub folders within and including the collection folder? No
Use the absolute file path name for the document name? No
Start a business process once files are collected? No
Extraction folder:       c:\
Unobscure File Contents? No
Filenaming convention Use the original filename as the extracted filename 
```

3) Create a new Business Process: **Demo_BP_CompressFilesFromFS**, using file **compress-files-from-filesystem.bpml** 

4) Run the BP and check by the steps on B2Bi Dashboard.

5) Create a new Business Process: **Demo_BP_CompressFilesUsingCLA**, using file **compress-files-using-cla.bpml** 

6) Run the BP and check by the steps on B2Bi Dashboard.

