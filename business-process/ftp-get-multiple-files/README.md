# IBM Sterling File Gateway Scenarios

Polling  Multiple files from a FTP Partner

In this scenario business needs to go out to a partner using FTP Server and poll for a file with specific name or extension. Once file is found it needs to be delivered internally.

You can schedule this BP to run every 30 minutes to check for files.

# Files

| BP Name                           |            Description of Role                                          |
|-----------------------------------|-------------------------------------------------------------------------|
| ftp-get-multiple-files.bpml       | Business Process that do a FTP get multiple files on partner. In this BP, i do a FTP LIST and do a FTP GET for each file|
| ftp-get-multiple-small-files.bpml | Business Process that do a FTP get multiple small files on partner. In this BP, i do a FTP GET to bring all files |


# Steps to Run:

**On Remote FTP Server**

1) Create a user on remote FTP server. Example: 

* Username: Demo_Remote_FTP
* Password: passw0rd
   
2) Create a file **testdata1.txt**, with content **testdata1** on user's home directory

3) Create a file **testdata2.txt**, with content **testdata2** on user's home directory

4) Create a file **testdata3.txt**, with content **testdata3** on user's home directory
 

**On Filegateway**

1) Create a Local Partner/Mailbox to receive Files. Example: Demo_Local_FTP

**On B2Bi Dashboard**

1) Change parameters on file: **polling_using_sftp_get.bpml** 

* RemoteHost:  remote ftp server
* RemotePort: remote ftp server port, default: 22
* RemoteUserId: remote username 
* RemotePasswd: remote password
* MAILBOX_PATH: /Inbox


```XML
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


2) Create a new Business Process: **Demo_BP_FTP_GetMultipleSmallFiles**, using file **ftp-get-multiple-small-files.bpml** 

3) Create a new Business Process: **Demo_BP_FTP_GetMultipleFiles**, using file **ftp-get-multiple-files.bpml** 


# Running

1) Logon on  B2Bi Dashboard and run Business Process: **Demo_BP_FTP_GetMultipleFiles** with user **Demo_Local_FTP**

2) Logon on Myfilegateway with user **Demo_Local_FTP**, and check for file  **testdataNN.txt** on download tab
