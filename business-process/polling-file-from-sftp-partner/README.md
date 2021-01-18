# IBM Sterling File Gateway Scenarios

Polling a file from a SFTP Partner

In this scenario business needs to go out to a partner using SFTP Server and poll for a file with specific name or extension. Once file is found it needs to be delivered internally.

You can schedule this BP to run every 30 minutes to check for files.

# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| polling_using_sftp_get.bpml     | Business Process that do a SFTP get on partner |


# Steps to Run:

**On Remote SSH Server**

1) Create a user on remote SSH server. Example: 

* Username: Demo_Remote_SFTP
* Password: passw0rd
   
2) Create a file on user's home directory . Example **example_sftp.txt**
 
3) Import Remote SSH HostKey on B2Bi Dashboard. Menu **Administration > Trading Partner > SSH > Known Host Key**

4) Open the key, and take note of value **Key ID**

**On Filegateway**

1) Create a Local Partner/Mailbox to receive Files. Example: Demo_Local_SFTP

**On B2Bi Dashboard**

1) Change parameters on file: **polling_using_sftp_get.bpml** 

* REMOTE_SFTP_SERVER:  remote sftp server
* REMOTE_SFTP_SERVER_PORT: remote sftp server port, default: 22
* REMOTE_SFTP_PARTNER_NAME: remote username 
* REMOTE_SFTP_PARTNER_PASSWORD: remote password
* REMOTE_SFTP_PARTNER_HOSTKEY: remote SSH hostkey Key ID
* REMOTE_FILENAME:  Filename to get
* MAILBOX_PATH: /Demo_Local_SFTP


From:
```XML
 <assign to="RemoteHost">REMOTE_SFTP_SERVER</assign>
 <assign to="RemotePort">REMOTE_SFTP_SERVER_PORT</assign>
 <assign to="RemoteUserId">REMOTE_SFTP_PARTNER_NAME</assign>
 <assign to="RemotePasswd">REMOTE_SFTP_PARTNER_PASSWORD</assign> 
 <assign to="KnownHostKeyId">REMOTE_SFTP_PARTNER_HOSTKEY</assign>
 ...
 <assign to="RemoteFileName">REMOTE_FILENAME</assign>
 ...
 <operation name="Mailbox Add Service">
   ...
   <assign to="MailboxPath">MAILBOX_PATH</assign>
```  

To My Example:
```XML
 <assign to="RemoteHost">127.0.0.1</assign>
 <assign to="RemotePort">22</assign>
 <assign to="RemoteUserId">Demo_Remote_SFTP</assign>
 <assign to="RemotePasswd">passw0rd</assign> 
 <assign to="KnownHostKeyId">442297176384f4ba2node1</assign>
 ...
 <assign to="RemoteFileName">example_sftp.txt</assign>
 ...
 <operation name="Mailbox Add Service">
   ...
   <assign to="MailboxPath">/Demo_Local_SFTP</assign>
```  

1) Create a new Business Process: **Demo_BP_Polling_Using_SFTP_Get**, using file **polling_using_sftp_get.bpml** 


# Running

1) Logon on  B2Bi Dashboard and run Business Process: **Demo_BP_Polling_Using_SFTP_Get**,

2) Logon on Myfilegateway with user **Demo_Local_SFTP**, and check for file  **example_sftp.txt** on download tab
