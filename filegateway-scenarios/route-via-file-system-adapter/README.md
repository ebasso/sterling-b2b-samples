# IBM Sterling File Gateway Scenarios

Put a file on network shared directory


# Important 

How to configure a File System Adapter to write to a shared network drive within a cluster (SCI90402)
https://www.ibm.com/support/pages/how-configure-file-system-adapter-write-shared-network-drive-within-cluster-sci90402


# Files

| File name                       |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| route-via-filesystem.bpml       | Business Process that do File System Adapter delivery to partner |
| AFTExtensionsCustomer.xml       | Sample file AFTExtensionsCustomer.xml |
| AFTExtensionsCustomer.properties| Sample file AFTExtensionsCustomer.properties |


# Steps to Run:

**On Dashboard**

1) Create a new File System Adapter: **Generic_FSA_Adapter**


2) Create a new Business Process: **Demo_RouteViaFileSystem**, using file **route-via-filesystem.bpml** 

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

```
Enable **File System Adapter** on Community Protocols
```

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files: Demo_Consumer_FSA_01

choose **File System Adapter**, and specify

* Remote Folder Name: \\<HOSTNAME>\<network_shared_drive>

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_RouteFile
    Consumer Identification: Static

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/fsa
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
* Consumer: Demo_Consumer_FSA_01

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload any file to virtual directory **/fsa**

2) After delivery, check files on mailboxes:

* On Demo_Consumer_FSA_01s



