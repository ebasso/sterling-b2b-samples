# IBM Sterling File Gateway Scenarios

In this scenario, I want to use the SFG to use sftp for Filetransfer between two Partners. Currently the adapter to use for SFTP Protocol in SFG is hardcoded, i. e., the default value is **SFTPClientAdapter**s.

This External Partner must be reached using a **External_SFTP_ClientAdapter**, that is setup to run on Perimeter Server in a more secure Zone. 

Another option is if you need to setup transfer mode as ASCII on 

Another Op

# Important 

How to configure a File System Adapter to write to a shared network drive within a cluster (SCI90402)
https://www.ibm.com/support/pages/how-configure-file-system-adapter-write-shared-network-drive-within-cluster-sci90402


# Files

| File name                       |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| route-via-custom-sftp.bpml      | Business Process that do use a custom SFTP Client Adapter to delivery to partner |
| AFTExtensionsCustomer.xml       | Sample file AFTExtensionsCustomer.xml |
| AFTExtensionsCustomer.properties| Sample file AFTExtensionsCustomer.properties |


# Steps to Run:

**On Dashboard**

1) Create a new SFTP Client Adapter **External_SFTP_ClientAdapter**, and define Perimeter Server.

```
Service Type:              SFTP Client Adapter
System Name:               External_SFTP_ClientAdapter
Description:               External SFTP Client Adapter on Perimeter Server
Group Name:                None
Perimeter Server           node1 & PS01
Minimum Number of Threads: 3
Maximum Number of Threads: 6
Local Port Range:          None provided
Use Proxy Server:          No
Proxy Type:                HTTP
Transfer Mode:             BINARY
```
 
2) Import Remote SSH HostKey on B2Bi Dashboard. 
 
Menu **Administration > Trading Partner > SSH > Known Host Key**

In my case i named as **MyLocalhost**

1) Create a Remote SSH Profile on B2Bi Dashboard. 
 
Menu **Administration > Trading Partner > SSH > Remote Profiles**

```
Profile Name:         Demo_Remote_SFTP_Profile
Remote Host:          127.0.0.1
Remote Port:          22
Known Host Key:       MyLocalhost
Remote User:          Demo_Remote_SFTP
Preferred Authentication Type: password
SSH Password:         ********
```
			

1) Create a new Business Process: **Demo_BP_RouteViaCustomSFTP**, using file **route-via-custom-sftp.bpml** 

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


1) Enable **Custom SFTP Protocol** on Community Protocols

**On Server machine - First Time Only**


1) Create a  directory on server machine MS Windows or Linux

My case SI is running on Limux, with user siuser

 mkdir -p /home/siuser/FSADemo

**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files, choose **Custom SFTP Protocol**, and specify Remote Folder Name

```
Partner Name:          Demo_Remote_SFTP
Phone:                 55555
Email Address:         demo@demo.com
User Name:             Demo_Remote_SFTP
Authentication Type:   Local
Session Timeout (min): 15
Given Name:            Demo_Remote
Surname:               SFTP
Partner Role:          Producer of Data, Consumer of Data
Connection Direction:  Listen Connection
Transport Method:      Custom SFTP Protocol
SSH Remote Profile:    Demo_Remote_SFTP_Profile 
SFTP Client Adapter:   External_SFTP_ClientAdapter
Does Demo_Remote_SFTP require data to be signed by the Router: no
Does Demo_Remote_SFTP require data to be encrypted by the Router : no
```

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_RouteFileViaCustomSFTP
    Consumer Identification: Not Dynamic

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/custom-sftp
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

* Routing Channel Template: Demo_RouteFileViaCustomSFTP
* Producer: Demo_Producer_01
* Consumer: Demo_Remote_SFTP

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload any file to virtual directory **/fsa**

2) After delivery, check files on mailboxes **Demo_Consumer_FSA_01s** and filesystem **/tmp/fsademo**.



