# IBM Sterling File Gateway Scenarios

File routed based on content inside the file.

In this scenario where application will be sending two data files. Recipient information is in the content of the file. Business wants File Gateway to determine the delivery partners from the data rather than creating folders/sub folder for each partner

Looking at header of csv files, you can view the name of the partner that will determine the route.


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| content-based-routing-01.bpml   | Business Process that do Content Based Routing to partner |
| content-based-01.mxl            | Map that extract Partner name and define ConsumerName |
| testdata-01.csv                 | CSV file example file to Demo_InternalPartner_01|
| testdata-02.csv                 | CSV file example file to Demo_InternalPartner_02|


# Steps to Run:


**On B2Bi Dashboard**

1) Create a new Business Process: **Demo_BP_Content_Based_Routing**, using file **content-based-routing-01.bpml** 

2) Create a new Map file:  **Demo_Map_Content_Based_Routing** using  **content-based-01.mxl**  and **content-based-01.txo** 

You need to open content-based-01.mxl on Map Editor and generate .txo file.

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_CB_01

2) Create a Partner to Receive Files: Demo_Consumer_CB_01

3) Create a Partner to Receive Files: Demo_Consumer_CB_02

4) Create a Routing Channel Template. See example: 

```
Routing Channel Template:
    Template Name: Demo_Content_Based_Routing_01
    Consumer Identification: Dynamic
    Business Process Name: Demo_BP_Content_Based_Routing
    Process Data Element Name: ConsumerName
    
    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}
    Producer File Structures:
        Producer File Structure: Unknown{.+}
        Layer: Unknown
            File name pattern as regular expression: .+
            File name pattern group fact names, comma delimited:
    Delivery Channel Templates:
        Delivery Channel Template:
            Consumer Mailbox Path: /${ConsumerName}/Inbox
            Consumer Mailbox: Created at runtime
            Consumer Protocol: protocol or mailbox
            Consumer File Structure: Unknown{${ProducerFilename}}
            Layer: Unknown
                File name format: ${ProducerFileName}
```

5) Create a Route Channel.

* Routing Channel Template: Demo_Content_Based_Routing_01
* Producer: Demo_Producer_CB_01

**Running**

1) Logon on Myfilegateway with user **Demo_Producer_CB_01**, and upload files testdata-01.csv, testdata-02.csv.

2) After delivery, check files on mailbox:

* On Demo_Consumer_CB_01, file must be testdata-01.csv 
* On Demo_Consumer_CB_02, file must be testdata-02.csv 


