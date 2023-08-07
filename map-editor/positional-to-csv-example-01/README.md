# IBM Map Editor - Example 01

In this scenario, 

* input.txt -- Source file
* output.txt -- Result file
* MapPos2CsvSample01.mxl -- Map Source Code
* MapPos2CsvSample01.txo -- Map Compiled Version

## Map Configuration

![Current Map](map-pos-to-csv-ex01-main.png)


## Input File (Positional file)

Records **123**

| Field       | Description of Role  | Pos | Size | 
|-------------|----------------------|-----|------|
| Id          | Register description |   1 |    3 | 
| NAME1       | Name                 |   4 |    7 | 
| NAME2       | Surname              |  11 |    7 |
| AMOUNT      | Amount Value         |  18 |   10 | 
| CODE        | Code (Sample)        |  28 |   10 |


## Output File (Delimited File/CSV)

Record **Header** 

| Field    | Description of Role  | 
|----------|----------------------|
| ID01     | Register description |
| TOTAL    | Number of Registers  |
| TODAY    | Current date         | 
| ACCOUNT  | Ammout Value         |
| IDN      | Constant             | 

Record **Details** 

| Field    | Description of Role  | 
|----------|----------------------|
| ID01     | Register description | 
| CNT      | # of register        | 
| FULL_NAME| Full Name            | 
| AMOUNT   | Amount Value         | 
| CODE10   | Constant             | 


## INPUT Map

### Extended Rule - Before Loop:

```
integer cnt;
cnt = 1; 
```

### Extended Rule - After Loop:

```
#TempTotal = cnt - 1;
```

### Records **DETAILS** - 0 to 999

Tag: 123, Pos=1, Size= 3

| Field       | Description of Role  | Type   | Pos | Size | Details |
|-------------|----------------------|--------|-----|------|---------------|
| NAME1       | Name                 | String |   4 |    7 | |
| NAME2       | Surname              | String |  11 |    7 | |
| AMOUNT      | Amount Value         | Number |  18 |   10 | |
| CODE        | Code (Sample)        | String |  28 |   10 | |
| * CNT       | computed counter     | NUMBER |  38 |   5  | #CNT = cnt; cnt = cnt + 1;   |
| * FULL_NAME | computed full name   | String |  43 |   20 | #FULL_NAME = #NAME1 + " " + #NAME2|

Important: computed fields must be put in the end of record in positional files

### Records Temp - 0 to 1

Tag: **$$$**, used to create a temporary register

| Field    | Description of Role  | Type   | Pos | Size | Value |
|----------|----------------------|--------|-----|------|---------------|
| * TempID | computed ID | String |   1    |    **0** |  |
| * TempTotal | computed # of records | Number |   4 |    **0** | |


## Output Map

### Record **Header** - 0 to 999

| Field    | Description of Role  | Type   | Default Value | Details |
|----------|----------------------|--------|---------------|---------------|
| ID01     | Register description | String | "01"          | Standard Rule - constant|
| TOTAL    | Number of Registers  | Number | TempTotal     |  |
| TODAY    | Current date         | Date   |               | Standard Rule - use system variables|
| ACCOUNT  | Ammout Value         | String | "123456"      | Standard Rule - constant|
| IDN      | Constant             | String | #IDN = "N";   | Extend Rule|

Record **Details** - 0 to 1

| Field    | Description of Role  | Type   | Source Value  | 
|----------|----------------------|--------|---------------|
| ID01     | Register description | String | "01"          | 
| CNT      | # of register        | Number |               |
| FULL_NAME| Full Name            | String | FULL_NAME     |
| AMOUNT   | Amount Value         | Number | AMOUNT        |
| CODE10   | Constant             | String | CODE          |
