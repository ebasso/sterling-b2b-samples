# IBM Sterling File Gateway Scenarios

SFG comes use file layer types to describe producer and consumer file structures

If you have additional requirements, like:

* Use a Map to translate file

add custom file layer types. When they are added, the new file layer types will be available when you create new routing channel templates.


# Files

| File                            |            Description of File                                          |
|---------------------------------|-------------------------------------------------------------------------|
| fgcustomlayer-translation.bpml  | Business Process that do the translation using a defined Map |
| Demo_Map_TranslationLayer.mxl   | Sample source Map that do the translation of CSV file |
| Demo_Map_TranslationLayer.txo   | Sample compiled Map that do the translation of CSV file |
| xapi-translation-layer-input.xml| Input file with required parameters to configure Translation Layer  |
| xapi-import-bp.bpml             | Business Process to read input file and run XAPI  |
| testdata-01.csv                 | CSV file example file|
| testdata-02.csv                 | CSV file example file|


# Steps to Run:


**On B2Bi Dashboard**

1) Create a new Business Process: **FGCustomLayer_Translation**, using file **fgcustomlayer-translation.bpml** 

2) Create a new Map file:  **Demo_Map_TranslationLayer** using  **Demo_Map_TranslationLayer.mxl**  and **Demo_Map_TranslationLayer.txo** 

You need to open Demo_Map_TranslationLayer.mxl on Map Editor to generate a new .txo file.

3) Create a new Business Process: **FileGatewayCustomLayerXAPI**, using file **xapi-import-bp.bpml** 

4) Run Business Process: **FileGatewayCustomLayerXAPI**, and provide **xapi-translation-layer-input.xml** as input

5) Restart Sterling  B2Bi environment

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Routing Channel Template. See example:

```
Routing Channel Template:
    Template Name: Demo_Translation
    Consumer Identification: not Dynamic
    
    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/translation
    Producer File Structures:
        Producer File Structure: Translation{.+}
        Layer: Translation
            File name pattern as regular expression: .+
            File name pattern group fact names, comma delimited:
    Delivery Channel Templates:
        Delivery Channel Template:
            Consumer Mailbox Path: /${ConsumerName}/translation-result
            Consumer Mailbox: Created at runtime
            Consumer Protocol: protocol or mailbox
            Consumer File Structure: Translation{${ProducerFilename}}
            Layer: Translation
                File name format: ${ProducerFileName}
                Map Name: Demo_Map_TranslationLayer
```

5) Create a Route Channel.

* Routing Channel Template: Demo_Translation
* Producer: Demo_Producer_01
* Consumer: Demo_Producer_01

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload files testdata-01.csv, testdata-02.csv.

2) After delivery, check the content of files on mailbox /Demo_Producer_01/result:




