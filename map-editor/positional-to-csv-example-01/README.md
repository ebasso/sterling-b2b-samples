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

| Field       | Description of Role  | Type   | Pos | Size | Value |
|-------------|----------------------|--------|-----|------|---------------|
| Tag         | Register description | Number |   1 |    3 | "123" |
| NAME1       | Name                 | String |   4 |    7 | |
| NAME2       | Surname              | String |  11 |    7 | |
| AMOUNT      | Amount Value         | Number |  18 |   10 | |
| CODE        | Code (Sample)        | String |  28 |   10 | |
| * CNT       | computed counter     | NUMBER |  55 |   5  | #CNT = cnt; cnt = cnt + 1;   |
| * FULL_NAME | computed full name   | String |  60 |   20 | #FULL_NAME = #NAME1 + " " + #NAME2|

Important: computed fields must be put in the end of map

## Output File (Delimited File/CSV)

Record **Header** 

| Field    | Description of Role  | Type   | Default Value | Details |
|----------|----------------------|--------|---------------|---------------|
| ID01     | Register description | String | "01"          | Standard Rule - constant|
| TOTAL    | Number of Registers  | Number | TempTotal     |  |
| TODAY    | Current date         | Date   |               | Standard Rule - use system variables|
| ACCOUNT  | Ammout Value         | String | "123456"      | Standard Rule - constant|
| IDN      | Constant             | String | #IDN = "N";   | Extend Rule|

Record **Details** 

| Field    | Description of Role  | Type   | Source Value  | 
|----------|----------------------|--------|---------------|
| ID01     | Register description | String | "01"          | 
| CNT      | # of register        | Number |               |
| FULL_NAME| Full Name            | String | FULL_NAME     |
| AMOUNT   | Amount Value         | Number | AMOUNT        |
| CODE10   | Constant             | String | CODE          |


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

### Records Temp

Tag: **$$$**, used to create a temporary register

| Field    | Description of Role  | Type   | Pos | Size | Value |
|----------|----------------------|--------|-----|------|---------------|
| * TempID | computed ID | String |   1    |    **0** |  |
| * TempTotal | computed # of records | Number |   4 |    **0** | |

