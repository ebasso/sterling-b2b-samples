# IBM Sterling File Gateway Scenarios

Extract files from a .zip file and delivery to multiple mailboxes defined by file extension


# Steps to Run:

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files: Demo_Consumer_01

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_Unzip_Multiple_Mailboxes 
    Consumer Identification: Not Dynamic

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/Zip
    Producer File Structures:
        Producer File Structure: Zip{.+[.]zip}/Unknown{(.+)[.](.+)}
        Layer: Zip
            File name pattern as regular expression: .+[.]zip
            File name pattern group fact names, comma delimited:
        Layer: Unknown
            File name pattern as regular expression: (.+)[.](.+)
            File name pattern group fact names, comma delimited: myzipname,myextension
    Delivery Channel Templates:
        Delivery Channel Template:
            Consumer Mailbox Path: /${ConsumerName}/Inbox/${myextension}
            Consumer Mailbox: Created at runtime
            Consumer Protocol: protocol or mailbox
            Consumer File Structure: Unknown{${myzipname}.${myextension}.${RoutingTimestamp}}
            Layer: Unknown
                File name format: ${myzipname}.${myextension}.${RoutingTimestamp}
```

6) Create a Route Channel.

* Routing Channel Template: Demo_Unzip_Multiple_Mailboxes
* Producer: Demo_Producer_01
* Consumer: Demo_Consumer_01

# Running

1) Create a Zip file and add to it a .doc file, a .txt file and .xml file.

2) Logon on Myfilegateway with user **Demo_Producer_01**, and upload the zip file

3) After delivery, check files on mailboxes:

* On Demo_Consumer_01
