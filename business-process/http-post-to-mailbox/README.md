# HTTP Post to a mailbox
 
Samples BPs to write a file to a mailbox, from a HTTP Post


# Files

| File name                           |            Description of BP                                          |
|-------------------------------------|-----------------------------------------------------------------------|
| http-post-to-mailbox.bpml.          | From a HTTP Post, write a file to a mailbox |



 Steps to Run:

**On Dashboard**

1) Login o Sterling B2B Console

2) Create a new Business Process: **HttpPostToMailbox**, using file **http-post-to-mailbox.bpml** 

**Important**: You must change the mailbox where you write the file

```XML
<assign to="MAILBOX_PATH">/Sistema_ftp/Inbox</assign>
```

3) Open the HTTP Server Adapter

4) Create a new  URI on **HTTP Server Adapter**

* field **URI**: /http2mailbox
* field **Business Process**: HttpPostToMailbox


# Running

1) Run command 


```bash
 curl -kv -X POST "http://localhost:5033/http2mailbox?MessageName=filename3.json" -H "Content-Type: application/json" --data @exemplo.txt
 ```

I use MessageName on query to write the filename on mailbox.