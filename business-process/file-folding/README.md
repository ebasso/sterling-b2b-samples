# Rename using Regex with Java Task
 
Samples BPs to put a new line character every N caracters. Use a Java Task

Content of file

```
012345678901234567890123456789
```

Defining 

```XML
<assign to="LineFoldLength">10</assign>
```

```
0123456789
0123456789
0123456789
```


# Files

| File name                           |            Description of BP                                          |
|-------------------------------------|-----------------------------------------------------------------------|
| file-folding.bpml                   | Fold lines |


# Steps to Run:



**On Dashboard**

1) Login o Sterling B2B Console

2) Create a new Java Task Adapter: 

```
Service Type:            Java Task Adapter
System Name:             JavaTask
Description:             Generic Java Task Adapter used 
Group Name:              None
```

1) Create a new Business Process: **Demo_BP_LineFolding**, using file **file-folding.bpml** 

2) Run the BP, upload a file and check result on steps on B2Bi Dashboard.

