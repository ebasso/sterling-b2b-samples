# Rename using Regex with Java Task
 
Samples BPs to rename files using Regular Expressions and Java Classes (Match and Pattern).

**Tip**: you can use a code list to store matchPattern and replacePattern to your BP be more dynamic. 

**Note**: Java Task is compiled every time it is executed and can affect performance. Using the code as part of Custom Service is much better from performance point of view.

## Sample 1: Rename file **XYZ_AB_0193_20012021_001594.TXT** to **CB_202101220_594.TXT**

```XML
<assign to="fileName">XYZ_AB_0193_20012021_001594.TXT</assign>
<assign to="matchPattern">XYZ_(.+)_(\d{4})_(\d{2})(\d{2})(\d{4})_(\d{3})(\d{3}).TXT</assign>
<assign to="replacePattern">CB_$5$4$3_$7.TXT</assign>
```

## Sample 2: Rename file **ABC_0194_20012021_001594.TXT** to **WTW-20012021.0193**

```XML
<assign to="fileName">ABC_0194_20012021_001594.TXT</assign>
<assign to="matchPattern">ABC_(\d{4})_(\d{8})_(\d{6}).TXT</assign>
<assign to="replacePattern">WTW-$2.$1</assign>
```

## Sample 3: Rename file diferent size:

* from **ABC_0195_20012021_001594.TXT** to **CCC_0195_20012021_594.TXT**
* from **ABC_0195_20012021_94.TXT** to **CCC_0195_20012021_94.TXT**

```XML
<assign to="matchPattern">ABC_(\d{4})_(\d{8})_(\d{0,3})(\d{2,3}).TXT</assign>
<assign to="replacePattern">CCC_$1_$2_$4.TXT</assign>
```


# Files

| File name                           |            Description of BP                                          |
|-------------------------------------|-----------------------------------------------------------------------|
| demo-rename-regex-java-task.bpml    | Rename using Regex with Java Task |


# Steps to Run:



**On Dashboard**

1) Login o Sterling B2B Console

2) Create a new Java Task Adapter: **Generic_FSA_Adapter**

```
Service Type:            Java Task Adapter
System Name:             JavaTask
Description:             Generic Java Task Adapter used 
Group Name:              None
```

3) Create a new Business Process: **Demo_BP_RenameRegexJavaTask**, using file **demo-rename-regex-java-task.bpml** 

4) Run the BP and check result on steps on B2Bi Dashboard.

