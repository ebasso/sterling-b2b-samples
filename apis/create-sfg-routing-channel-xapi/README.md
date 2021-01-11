# IBM Sterling B2B: Criando Canais no Sterling File Gateway usando o XAPI

Sample code that Creates a Routing Channel in Sterling File Gateway using XAPI.

For more example the **<IBM SB2Bi install>/xapidocs** directory contains input/output xml example files, code examples, and class/api information.


Pre-Steps:

1) Get **ORGANIZATION_KEY** for Producer and Consumer, using SQL statement:

```SQL
select * from YFS_ORGANIZATION where MODIFYPROGID = 'filegateway'
```

2) Get **ROUTCHAN_TMPL_KEY**, using SQL statement:

```SQL
select * from FG_ROUTCHAN_TMPL
```

With these values you must change **createRC_input.xml** file.


Steps:


1) Login o Sterling B2B Console

2) Create a BP named **XAPI_CreateRoutingChannel** and use code from *XAPI_CreateRoutingChannel.bpml*

3) Run the BP and provide **createRC_input.xml** as input

4) Check if BP run successfully.

5) Check the new created user in User Accounts.
