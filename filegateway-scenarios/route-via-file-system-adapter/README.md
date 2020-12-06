# IBM Sterling File Gateway Scenarios

In this scenario, we enable SFG to put a file on network shared directory to a Partner.

We need to add a Custom Protocol on SFG. And after need to define this protocol to a partner.



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

```
Service Type:            File System Adapter
System Name:             Generic_FSA_Adapter
Description:             Generic FSA Adapter used on SFG
Group Name:              None
Collection folder:       c:\
Filename filter          *.xyz
Collect files from sub folders within and including the collection folder? No
Use the absolute file path name for the document name? No
Start a business process once files are collected? No
Extraction folder:       c:\
Unobscure File Contents? No
Filenaming convention Use the original filename as the extracted filename 
```

2) Create a new Business Process: **Demo_BP_RouteViaFileSystem**, using file **route-via-filesystem.bpml** 

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


1) Enable **File System Adapter** on Community Protocols

**On Server machine - First Time Only**


1) Create a  directory on server machine MS Windows or Linux

My case SI is running on Limux, with user siuser

 mkdir -p /home/siuser/FSADemo

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files, choose **File System Adapter**, and specify Remote Folder Name

```
Partner Name:          Demo_Consumer_FSA_01
Phone:                 55555
Email Address:         demo@demo.com
User Name:             Demo_Consumer_FSA_01
Authentication Type:   Local
Session Timeout (min): 15
Given Name:            Demo_Consumer
Surname:               FSA_01
Partner Role:          Consumer of Data
Connection Direction:  Listen Connection
Transport Method:      File System Adapter
Remote Folder Name:    /home/siuser/FSADemo
Does Demo_Consumer_FSA_01 require data to be signed by the Router: no
Does Demo_Consumer_FSA_01 require data to be encrypted by the Router : no
```

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_RouteFileViaFSA
    Consumer Identification: Not Dynamic

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

4) Create a Route Channel.

* Routing Channel Template: Demo_RouteFileViaFSA
* Producer: Demo_Producer_01
* Consumer: Demo_Consumer_FSA_01

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload any file to virtual directory **/fsa**

2) After delivery, check files on mailboxes **Demo_Consumer_FSA_01s** and filesystem **/tmp/fsademo**.



