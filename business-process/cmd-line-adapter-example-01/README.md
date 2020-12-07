# IBM Sterling B2B: Criando Usuários no B2Bi usando o XAPI

Sample code that use Command Line Adapter 2 on Linux

# APIs

| BP Name                         | filename                     |            Description of Role                                          |
|---------------------------------|------------------------------|-------------------------------------------|
| Demo_BP_CLA_Example_01          | cmd-line-example-01.bpml     | Command line example |
|                                 | myscript.sh                  | shell script to test cla |


Steps to Run:

1) Login o Linux Box

2) Copy file  **myscript.sh** on SI home directory. In my case  **/home/siuser/myscript.sh**

3) Give the permissions
   
```bash
chmod a+x /home/siuser/myscript.sh
```

4) Login o Sterling B2B Console

5) Create a BP named **Demo_BP_CLA_Example_01** and use code from **<cmd-line-example-01.bpml**

6) Run the BP and check by the steps on B2Bi Dashboard.
