# IBM Sterling File Gateway Scenarios

In this scenario, I want to use the SFG to use FTP for Filetransfer between two Partners.

Remote FTP Server need to run Quote Command before send files. So i create a custom ftp protocol to do this.

Another feature is that, the adapter to use for FTP Protocol in SFG is hardcoded, i. e., the default value is **FTPClientAdapter**s.

This External Partner must be reached using a **External_FTP_ClientAdapter**, that is setup to run on Perimeter Server in a more secure Zone. Another option is if you need to setup transfer mode as ASCII.



# Files

| File name                       |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| route-via-custom-ftp.bpml      | Business Process that do use a custom ftp Client Adapter to delivery to partner |
| AFTExtensionsCustomer.xml       | Sample file AFTExtensionsCustomer.xml |
| AFTExtensionsCustomer.properties| Sample file AFTExtensionsCustomer.properties |


# Steps to Run:

**On Dashboard**

1) Create a new ftp Client Adapter **External_ftp_ClientAdapter**, and define Perimeter Server.

```
Service Type:              Ftp Client Adapter
System Name:               External_FTP_ClientAdapter
Description:               External FTP Client Adapter on Perimeter Server
Group Name:                None
Perimeter Server           node1 & PS01
Minimum Number of Threads: 3
Maximum Number of Threads: 6
Local Port Range:          None provided
Use Proxy Server:          No
Proxy Type:                HTTP
Transfer Mode:             BINARY
```


2) Create a new Business Process: **Demo_BP_RouteViaCustomFTP**, using file **route-via-custom-ftp.bpml** 

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


1) Enable **Custom FTP Protocol** on Community Protocols


**On Filegateway**

1) Create a Partner to Send Files: Demo_Producer_01

2) Create a Partner to Receive Files, choose **Custom FTP Protocol**, and specify Remote Folder Name

```
Partner Name:          Demo_Remote_FTP
Phone:                 55555
Email Address:         demo@demo.com
User Name:             Demo_Remote_FTP
Authentication Type:   Local
Session Timeout (min): 15
Given Name:            Demo_Remote
Surname:               ftp
Partner Role:          Producer of Data, Consumer of Data
Connection Direction:  Listen Connection
Transport Method:      Custom FTP
FTP Server Host Name(or IP address):  127.0.0.1 
FTP Listen Port        5021
Connection Type:       Passive
User Name:             Demo_Remote_FTP
Password:              ********
Base Directory:
Local Port Range:
Control Port Range:
Number of retries:     3
Interval between retries (in minutes): 1
Upload file under a temporary name first? No
Quote Command:
Does Demo_Remote_FTP require data to be signed by the Router: no
Does Demo_Remote_FTP require data to be encrypted by the Router : no
```

3) Create a Routing Channel Template.

```
 Routing Channel Template:
    Template Name: Demo_RouteFileViaCustomFTP
    Consumer Identification: Not Dynamic

    Special Character Handling: No special character handling is specified
    Provisioning Fact List:
    Group Permissions:
        Producer Group: All Partners
        Consumer Group: All Partners
    Producer Mailbox Path: /${ProducerName}/custom-ftp
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

* Routing Channel Template: Demo_RouteFileViaCustomftp
* Producer: Demo_Producer_01
* Consumer: Demo_Remote_ftp

# Running

1) Logon on Myfilegateway with user **Demo_Producer_01**, and upload any file to virtual directory **/custom-ftp**

2) After delivery, check files on mailboxes **Demo_Remote_FTP** and on remote FTP Server.



