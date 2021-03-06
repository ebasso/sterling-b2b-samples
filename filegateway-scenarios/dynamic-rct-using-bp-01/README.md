# IBM Sterling File Gateway Scenarios

Deliver a file to a Consumer identified by a Business Process(BP), inside Dynamic Routing Channel Template (RCT), 


# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| dynamic-consumername.bpml       |  Business Process that generate a ConsumerName|


# Steps to Run:


1) Create a new Business Process: **Demo_BP_Dynamic_ConsumerName**, using file **dynamic-consumername.bpml** 

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_DR_01

2) Create a Partner to Receive Files: Demo_Consumer_DR_01

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_Dynamic_RCT_using_BP 
    Consumer Identification: Dynamic
    Business Process Name: Demo_BP_Dynamic_ConsumerName
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
* Producer: Demo_Producer_DR_01

# Running

1) Logon on Myfilegateway with user **Demo_Producer_DR_01**, and upload any file.

2) After delivery, check files on mailboxes:

* On Demo_Consumer_DR_01
