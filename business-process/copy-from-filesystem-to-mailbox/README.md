# Copy File(s) From File System to a Mailbox
 
Samples BPs to copy file(s) from server or from a network share to IBM Sterling B2Bi Mailbox.



# Important 

[How to configure a File System Adapter to write to a shared network drive within a cluster (SCI90402)](https://www.ibm.com/support/pages/how-configure-file-system-adapter-write-shared-network-drive-within-cluster-sci90402)


# Files

| File name                          |            Description of BP                                          |
|------------------------------------|-------------------------------------------------------------------------|
| copy-file-from-fsa-to-mbx.bpml     | Copy one file from File System to Mailbox |
| copy-multiplefiles-fsa-to-mbx.bpml | Copy multiple files from File System to Mailbox |



# Steps to Run:

**On Server**

1) Create a directory  

```
C:\Temp\
```
In this directory

2) Create a file testdata1.txt with content "testdata1"

3) Create a file testdata2.txt with content "testdata2"

4) Create a file testdata3.txt with content "testdata3"

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

3) Create a new Business Process: **Demo_BP_CopyFileFromFSA2MBX**, using file **copy-file-from-fsa-to-mbx.bpml** 

4) Run the BP and check by the steps on B2Bi Dashboard.

5) Check Virtual Directory "/Inbox" from user that run the BP.

6) Create a new Business Process: **Demo_BP_CopyMultipleFilesFromFSA2MBX**, using file **copy-mutiplefiles-from-fsa-to-mbx.bpml** 

7) Run the BP and check by the steps on B2Bi Dashboard.

8) Check Virtual Directory "/Inbox" from user that run the BP.