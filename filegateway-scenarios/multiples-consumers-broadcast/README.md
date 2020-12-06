# IBM Sterling File Gateway Scenarios

Broadcast one file to multiple partners using a Group.

This support different protocols, only define on Demo_InternalPartner_NN.

# Steps to Run:


**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files: Demo_Consumer_01

3) Create a Partner to Receive Files: Demo_Consumer_02

3) Create a Group of Participants: Demo_BroadCastGroup 
 
and include partners: Demo_Consumer_01, Demo_Consumer_02.

1) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_Multiples_Consumers_Broadcast
    Consumer Identification: Dynamic

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
        Fact Name: ConsumerBroadcastGroup
        Display Label: Consumer Broadcast Group
        Description: Provide Name of the Broadcast Group
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/broadcast
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

* Routing Channel Template: Demo_Multiples_Consumers_Broadcast
* Producer: Demo_Producer_01
* Consumer Broadcast Group: Demo_BroadCastGroup

# Running

1) Logon on Myfilegateway with user **Demo_Operations_01**, and upload any file.

2) After delivery, check files on mailboxes:

* On Demo_Consumer_01
* On Demo_Consumer_02
