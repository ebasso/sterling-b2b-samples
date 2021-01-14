# Hello World 2 example on  HTTP Server Adapter


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| hello-world2.bpml               | Business Process that do HTTP Response |
| hello-world2.xslt               | XSLT file to generate html output |


# Steps to Run:


**On B2Bi Dashboard**


1) Create a new Business Process: **HelloWorld2**, using file **hello-world2.bpml** 

2) Create a new XSLT: **HelloWorld2**, using file **hello-world2.xslt** 

3) Add a new uri **/hello2** on **HTTP Server Adapter**, and choose Business Process  **HelloWorld2**


# Running

1) In a Browser, access you HTTP server adapter, in my case

```
http://localhost:5033/hello2
```

and see the output