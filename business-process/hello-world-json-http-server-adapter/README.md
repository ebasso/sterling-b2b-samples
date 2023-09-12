# Hello World JSON example on  HTTP Server Adapter


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| hello-world-json.bpml           | Business Process that do HTTP Response |



# Steps to Run:


**On B2Bi Dashboard**


1) Create a new Business Process: **HelloWorldJSON**, using file **hello-world-json.bpml** 

2) Add a new uri **/helloworldjson** on **HTTP Server Adapter**, and choose

*  Business Process  **HelloWorldJSON**
* Send Raw Messages: **No**
* Run BP in sync mode: **No**

Save


# Running

1) In a Browser, access you HTTP server adapter, in my case

```
http://localhost:5033/helloworldjson
```

and see the output