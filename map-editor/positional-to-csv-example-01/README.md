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

| Field    | Description of Role  | Type   | Pos | Size | Default Value |
|----------|----------------------|--------|-----|------|---------------|
| Register | Register description | Number |   1 |    3 | 123 |
| NAME1    | Name                 | String |   4 |    7 | |
| NAME2    | Surname              | String |  11 |    7 | |
| AMOUNT   | Amount Value         | Number |  18 |   10 | |
| CODE     | Code (Sample)        | String |  28 |   10 | |


## Output File (Delimited File/CSV)

Record **Header** 

| Field    | Description of Role  | Type   | Default Value |
|----------|----------------------|--------|---------------|
| ID01     | Register description | String | 01 |
| TOTAL    | Number of Registers  | Number | |
| TODAY    | Current date         | Date | |
| ACCOUNT  | Ammout Value         | String | |
| IDN      | Constant             | String | N |

Record **Details** 

| Field    | Description of Role  | Type   | Default Value |
|----------|----------------------|--------|---------------|
| ID01     | Register description | String | 01 |
| CNT      | # of register        | Number | |
| FULL_NAME| Full Name            | String | |
| AMOUNT   | Amount Value         | Number | |
| CODE10   | Constant             | String | |
