# IBM Sterling File Gateway Scenarios

Polling multiple files from a SFTP Partner

In this scenario business needs to go out to a partner using SFTP Server and poll for a file with specific name or extension. Once file is found it needs to be delivered internally.

You can schedule this BP to run every 30 minutes to check for files.

# Files

| BP Name                           |            Description of Role                                          |
|-----------------------------------|-------------------------------------------------------------------------|
| sftp-get-multiple-small-files.bpml | Business Process that do a FTP get multiple small files on partner. In this BP, i do a FTP GET to bring all files |


# Steps to Run:

**On Remote FTP Server**

1) Create a user on remote SFTP server. Example: 

* Username: Demo_Remote_SFTP
* Password: passw0rd
   
2) Create a file **testdata1.txt**, with content **testdata1** on user's home directory

3) Create a file **testdata2.txt**, with content **testdata2** on user's home directory

4) Create a file **testdata3.txt**, with content **testdata3** on user's home directory
 

**On Filegateway**

1) Create a Local Partner/Mailbox to receive Files. Example: Demo_Local_SFTP

**On B2Bi Dashboard**

1) Import Remote SSH HostKey on B2Bi Dashboard. Menu **Administration > Trading Partner > SSH > Known Host Key**


2) Change parameters on file: **sftp-get-multiple-small-files.bpml** 

* KnownHostKeyId: Remote SSH HostKey
* RemoteHost:  remote sftp server
* RemotePort: remote sftp server port, default: 22
* RemoteUserId: remote username 
* RemotePasswd: remote password
* MAILBOX_PATH: /Inbox


```XML
  <assign to="KnownHostKeyId">442297176384f4ba2node1</assign>
  <assign to="RemoteHost">localhost</assign>
  ...
  <assign to="UsingRevealedPasswd">True</assign>
  <assign to="RemotePasswd">passw0rd</assign>
  <assign to="RemoteUserId">Demo_Remote_FTP</assign>
  <assign to="RemotePort">21</assign>
 ...
 <operation name="Mailbox Add Service">
   ...
   <assign to="MailboxPath">MAILBOX_PATH</assign>
```  


1) Create a new Business Process: **Demo_BP_SFTP_GetMultipleFiles**, using file **sftp-get-multiple-small-files.bpml** 


# Running

1) Logon on  B2Bi Dashboard and run Business Process: **Demo_BP_SFTP_GetMultipleFiles** with user **Demo_Local_SFTP**

2) Logon on Myfilegateway with user **Demo_Local_SFTP**, and check for file  **testdataNN.txt** on download tab
