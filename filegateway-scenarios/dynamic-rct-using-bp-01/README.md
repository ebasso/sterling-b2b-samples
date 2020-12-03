# IBM Sterling File Gateway Scenarios

Deliver a file to a Consumer identified by a Business Process(BP), inside Dynamic Routing Channel Template (RCT), 


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| dynamic-consumername.bpml       |  Business Process that generate a ConsumerName|
| dynamic-consumername-pd.bpml    |  Business Process that generate a ConsumerName from PrimaryDocument|


# Steps to Run:


**On Filegateway**

1) Create a Partner to Send Files: Demo_Operations_01

2) Create a Partner to Receive Files: Demo_InternalPartner_01

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_Dynamic_RCT_using_BP 
    Consumer Identification: Dynamic
    Business Process Name: BP_Dynamic_ConsumerName
    Process Data Element Name: ConsumerName

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/dynrct
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

6) Create a Route Channel.

* Routing Channel Template: Demo_Dynamic_RCT_using_BP
* Producer: Demo_Operations_01s

**Running**

1) Logon on Myfilegateway with user **Demo_Operations_01**, and upload any file.

2) After delivery, check files on mailboxes:

* On Demo_InternalPartner_01


**Second example**


1) Create a file 

2) Delete the Channel: Demo_Dynamic_RCT_using_BP

3) Change the Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_Dynamic_RCT_using_BP 
    Consumer Identification: Dynamic
    Business Process Name: BP_Dynamic_ConsumerName_PrimaryDoc
    Process Data Element Name: ConsumerName
```

4) Create a Route Channel.

* Routing Channel Template: Demo_Dynamic_RCT_using_BP
* Producer: Demo_Operations_01s
    