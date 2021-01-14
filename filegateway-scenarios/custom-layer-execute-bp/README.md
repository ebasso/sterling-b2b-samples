# IBM Sterling File Gateway Scenarios

SFG comes use file layer types to describe producer and consumer file structures

If you have additional requirements, like:

* Use a custom BP

add custom file layer types. When they are added, the new file layer types will be available when you create new routing channel templates.


# Files

| File                            |            Description of File                                          |
|---------------------------------|-------------------------------------------------------------------------|
| fgcustomlayer-executeprocess.bpml  | Business Process that do the translation using a defined Map |
| xapi-custom-layer-input.xml     | Input file with required parameters to configure Translation Layer  |
| xapi-import-bp.bpml             | Business Process to read input file and run XAPI  |
| testdata-01.csv                 | CSV file example file|
| testdata-02.csv                 | CSV file example file|


# Steps to Run:


**On B2Bi Dashboard**

1) Create a new Business Process: **FGCustomLayer_ExecuteProcess**, using file **fgcustomlayer-executeprocess.bpml** 

2) Create a new Business Process: **FileGatewayCustomLayerXAPI**, using file **xapi-import-bp.bpml** 

3) Create a new Business Process: **Demo_BP_CustomLayer_Producer**, using file **demo-bp-customlayer-producer.bpml** 

4) Create a new Business Process: **Demo_BP_CustomLayer_Consumer**, using file **demo-bp-customlayer-consumer.bpml** 

5) Run Business Process: **FileGatewayCustomLayerXAPI**, and provide **xapi-custom-layer-input.xml** as input

6) Restart Sterling  B2Bi environment

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Routing Channel Template. 
 
Example with Consumer Layer Only

```
Routing Channel Template:
    Template Name: Demo_CustomLayer
    Consumer Identification: not Dynamic
    
    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/custom-layer
    Producer File Structures:
        Producer File Structure: Unknown{.+}
        Layer: Unknown
            File name pattern as regular expression: .+
            File name pattern group fact names, comma delimited:
    Delivery Channel Templates:
        Delivery Channel Template:
            Consumer Mailbox Path: /${ConsumerName}/custom-layer-result
            Consumer Mailbox: Created at runtime
            Consumer Protocol: protocol or mailbox
            Consumer File Structure: Consumer Execute Process{${ProducerFilename}}
            Layer: Consumer Execute Process
                File name format: ${ProducerFileName}
                Business Process to  Execute: Demo_BP_CustomLayer_Consumer
            Layer: Unknown
                File name format: ${ProducerFileName}
```

Example with Producer and Consumer Layer

```
Routing Channel Template:
    Template Name: Demo_CustomLayer
    Consumer Identification: not Dynamic
    
    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/custom-layer
    Producer File Structures:
        Producer File Structure: Consumer Execute Process{.+}
        Layer: Produccer Execute Process
                File name format: .+
                Business Process to  Execute: Demo_BP_CustomLayer_Producer
        Layer: Unknown
            File name pattern as regular expression: .+
            File name pattern group fact names, comma delimited:
    Delivery Channel Templates:
        Delivery Channel Template:
            Consumer Mailbox Path: /${ConsumerName}/custom-layer-result
            Consumer Mailbox: Created at runtime
            Consumer Protocol: protocol or mailbox
            Consumer File Structure: Consumer Execute Process{${ProducerFilename}}
            Layer: Consumer Execute Process
                File name format: ${ProducerFileName}
                Business Process to  Execute: Demo_BP_CustomLayer_Consumer
            Layer: Unknown
                File name format: ${ProducerFileName}
```

1) Create a Route Channel.

* Routing Channel Template: Demo_CustomLayer
* Producer: Demo_Producer_01
* Consumer: Demo_Producer_01

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload files testdata-01.csv, testdata-02.csv.

2) After delivery, check the content of files on mailbox /Demo_Producer_01/custom-layer-result:




