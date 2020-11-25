# IBM Sterling File Gateway Scenarios

File routed based on content inside the file.

In this scenario where application will be sending two data files. Recipient information is in the content of the file. Business wants File Gateway to determine the delivery partners from the data rather than creating folders/sub folder for each partner

Looking at header of csv files, you can view the name of the partner that will determine the route.


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| content_based_routing_01.bpml   | Business Process that do Content Based Routing to partner |
| content_based_01.mxl            | Map that extract Partner name and define ConsumerName |
| testdata-01.csv                 | CSV file example file to Demo_InternalPartner_01|
| testdata-02.csv                 | CSV file example file to Demo_InternalPartner_02|


# Steps to Run:


**On B2Bi Dashboard**

1) Create a new Business Process: **BP_Content_Based_Routing**, using file **content_based_routing_01.bpml** 

2) Create a new Map file:  **Map_Content_Based_Routing** using  **content_based_01.mxl**  and **content_based_01.txo** 

You need to open content_based_01.mxl on Map Editor and generate .txo file.

**On Filegateway**

1) Create a Partner to Send Files: Demo_ContentBased_01

2) Create a Partner to Receive Files: Demo_InternalPartner_01

3) Create a Partner to Receive Files: Demo_InternalPartner_02

4) Create a Routing Channel Template. See example: rct.txt

 Routing Channel Template:
    Template Name: Demo_Content_Based_Routing_01
    Consumer Identification: Dynamic
    Business Process Name: BP_Content_Based_Routing
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

5) Create a Route Channel.

    Routing Channel Template: Demo_Content_Based_Routing_01
    Producer: Demo_ContentBased_01

**Running**

1) Logon on Myfilegateway with user Demo_ContentBased_01, and upload files testdata-01.csv, testdata-02.csv.

2) After delivery, check files on mailbox:

* On Demo_InternalPartner_01, file must be testdata-01.csv 
* On Demo_InternalPartner_02, file must be testdata-02.csv 


