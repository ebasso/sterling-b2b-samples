# IBM Sterling File Gateway Scenarios

In this scenario, i create a custom protocol that write a file to a filesystem **/home/siuser/CustomProtocol** with a custom filename **PRD.ABC.2020-12-07.14-03-19-803.txt**.

## Suggestions for this example

* Use **Timestamp Util Service** to create a customized timestamp to use as filename
* Use **Translation** service to translate file content
* Use **Translation** service to get content on file to use as part of filename
* Use **xmljsontransformer** service to convert content of file from xml to json, and vice versa.

# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| route-via-custom-protocol.bpml  | Business Process that do File System Adapter delivery to partner |
| AFTExtensionsCustomer.xml       | Sample file AFTExtensionsCustomer.xml |
| AFTExtensionsCustomer.properties| Sample file AFTExtensionsCustomer.properties |


# Steps to Run:

**On Dashboard**

1) Create a new File System Adapter: **Generic_FSA_Adapter**. It is not necessary to create a new one if already exists.

2) Create a new Business Process: **Demo_BP_RouteViaCustomProtocol**, using file **route-via-custom-protocol.bpml** 

**On Dashboard Customizations**

3) Open B2Bi Dashboard

4) Select **Customization > Customization**. 

5) Click the **Click Here To Access** link. 

6) In the Customization login screen, enter the User Name and Password and click Login.

```
YOU MUST HAVE APIUser Permission
```

7) Click **CustomSFGExtensions**. The CustomSFGExtensions list page is displayed.
   
8) Click the **AFTExtensions Customer file** link. On the **General** tab, click **Edit**.

9) Click **Browse** to select ***AFTExtensionsCustomer.xml*** file and ***AFTExtensionsCustomer.properties*** file and click **SaveCustomSFGExtensions**.

10) Run <install_dir>/bin/setupfiles.sh.

11) Run <install_dir>/bin/deployer.sh.

12) Restart B2Bi


**On Filegateway - First Time Only**

 Enable **Custom Protocol** on Community Protocols


**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files, choose **Custom Protocol**

```
Partner Name:          Demo_Consumer_CP_01
Phone:                 55555
Email Address:         demo@demo.com
User Name:             Demo_Consumer_CP_01
Authentication Type:   Local
Session Timeout (min): 15
Given Name:            Demo_Consumer
Surname:               CP_01
Partner Role:          Consumer of Data
Connection Direction:  Listen Connection
Transport Method:      Custom Protocol
Does Demo_Consumer_FSA_01 require data to be signed by the Router: no
Does Demo_Consumer_FSA_01 require data to be encrypted by the Router : no
```

**Important**: I put some parameters on this scenario, but you can ignore.

1) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_RouteFileViaCustomProtocol
    Consumer Identification: Static

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/custom-protocol
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
            Consumer File Structure: Unknown{${ProducerFileName}}
            Layer: Unknown
                File name format: ${ProducerFileName}
```

6) Create a Route Channel.

* Routing Channel Template: Demo_RouteFile
* Producer: Demo_Producer_01
* Consumer: Demo_Consumer_CP_01

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload any file to virtual directory **/custom-protocol**

2) After delivery, check files on mailboxes **Demo_Consumer_CP_01** and filesystem **/home/siuser/CustomProtocol** for a custom filename:

* **PRD.ABC.YYYY-mm-dd.HH-MM-ss-SSS.txt**. Example: **PRD.ABC.2020-12-07.14-03-19-803.txt**.

