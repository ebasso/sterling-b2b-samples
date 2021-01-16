# Advanced Search for Sterling File Gateway
 
Create a Web Page to Search for File Gateway' Partners using these fields:

* Partner Name
* Partner Code
* Login ID
* First Name
* Last Name

Screenshot from web page:

![Result](/readme_images/sfg-advanced-search.png)

# Files

| File name                          |            Description of BP                                          |
|------------------------------------|-------------------------------------------------------------------------|
| sfg-advanced-search-web.bpml       | Business Process to generate a HTML page for Search |
| sfg-advanced-search.xslt           | XSLT to generate a HTML page for Search |



# Steps to Run:


**On Dashboard**

1) Login o Sterling B2B Console


2) Create a new XSLT: **SFGAdvancedSearchWeb**, using file **sfg-advanced-search.xslt** 

3) Create a new Business Process: **SFGAdvancedSearchWeb**, using file **sfg-advanced-search-web.bpml** 

**Important**: You must change the pool for your environment, at line 103 of bpml, my database is DB2 so my pool is db2Pool. For oracle, the default value is oraclePool

```XML
<assign to="pool">db2Pool</assign>
```

4) Create a new  URI on **HTTP Server Adapter**

* field **URI**: /search
* field **Business Process**: SFGAdvancedSearchWeb



# Running

1) Open a Browser and access the url of HTTP Server adapter

```
http://localhost:5033/search
```
