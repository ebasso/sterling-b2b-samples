# Hello World 2 example on  HTTP Server Adapter


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| hello-world-xml.bpml            | Business Process that do HTTP Response |
| hello-world-xml.xslt            | XSLT file to generate html output |
| restapi-client-xml.xslt         | Business Process that do RestAPI Get |


# Steps to Run:


**On B2Bi Dashboard**


1) Create a new Business Process: **HelloWorldXML**, using file **hello-world-xml.bpml** 

2) Create a new XSLT: **HelloWorldXML**, using file **hello-world.xslt** 

3) Add a new uri **/helloworldxml** on **HTTP Server Adapter**, and choose:

*  Business Process: **HelloWorldXML**
* Send Raw Messages: **No**
* Run BP in sync mode: **No**

Save

# Running

1) In a Browser, access you HTTP server adapter, in my case

```
http://localhost:5033/hello2
```

and see the output