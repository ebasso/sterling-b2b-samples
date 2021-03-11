# Code List Editor Web
 
Allow you to search a Code list and update a record. Solved a problem when Code List has multiples pages.

Screenshot from web page:

## Code List Editor Web - List
![Code List Editor Web - List](/readme_images/code-list-editor-web-01.png)

## Code List Editor Web - Update Code list
![Code List Editor Web - Update Code list](/readme_images/code-list-editor-web-02.png)

# Files

| File name                          |            Description of BP                                          |
|------------------------------------|-------------------------------------------------------------------------|
| code-list-editor-web.bpml          | Business Process to generate a HTML page for Search |
| code-list-editor-web.xslt          | XSLT to generate a HTML page for Search |



# Steps to Run:


**On Dashboard**

1) Login o Sterling B2B Console


2) Create a new XSLT: **CodeListEditorWeb**, using file **code-list-editor-web.xslt** 

3) Create a new Business Process: **CodeListEditorWeb**, using file **code-list-editor-web.bpml** 

**Important**: You must change the pool for your environment, at line 103 of bpml, my database is DB2 so my pool is db2Pool. For oracle, the default value is oraclePool

```XML
<assign to="pool">db2Pool</assign>
```

4) Create a new  URI on **HTTP Server Adapter**

* field **URI**: /codelisteditor
* field **Business Process**: CodeListEditorWeb



# Running

1) Open a Browser and access the url of HTTP Server adapter

```
http://localhost:5033/codelisteditor
```
