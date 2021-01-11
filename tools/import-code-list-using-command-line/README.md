# IBM Sterling B2B: Criando Code Lists no B2Bi usando o comando import.cmd

Sample code that creates a Code List in Sterling B2B using import.cmd utility.

Steps:


1) Run the import.cmd utility and provide **codelist-input.xml** as input

```
cd <SB2Bi_install>\bin

import.cmd -update -passphrase <passphrase> -input c:\codelist-input.xml
```

2) Check if command run successfully.

3) Check the new created Code List in SB2Bi Dashboard.


Tips:

To use a Code List in your BP, you must add a **Lightweight JDBC Adapter**, and use below query:

```SQL
SELECT CODELIST_XREF_ITEM.RECEIVER_ITEM
FROM CODELIST_XREF_ITEM 
WHERE CODELIST_XREF_ITEM.LIST_NAME = 'Mobile Suppliers' 
AND CODELIST_XREF_ITEM.LIST_VERSION = (SELECT DEFAULT_VERSION FROM CODELIST_XREF_VERS WHERE CODELIST_XREF_VERS.LIST_NAME = 'Mobile Suppliers') 
AND CODELIST_XREF_ITEM.SENDER_ITEM = 'Android Device'
```

In my example i will get a Supplier that i need to send files in SFG.