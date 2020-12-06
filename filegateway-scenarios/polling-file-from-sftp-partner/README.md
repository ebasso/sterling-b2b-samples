# IBM Sterling File Gateway Scenarios

Polling a file from a SFTP Partner

In this scenario business needs to go out to a partner using SFTP Server and poll for a file with specific name or extension. Once file is found it needs to be delivered internally.

You can schedule this BP to run every 30 minutes to check for files.

# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| polling_using_sftp_get.bpml      | Business Process that do a SFTP get on partner |


# Steps to Run:

**On Remote SSH Server**

 1) Create a user on remote SSH server. Example: Demo_Remote_SFTP
   
 2) Create a file on user's home directory . Example **example_sftp.txt**
 
 3) Import Remote SSH HostKey on B2Bi Dashboard

**On Filegateway**

 1) Create a Local Partner/Mailbox to receive Files. Example: Demo_Local_SFTP

**On B2Bi Dashboard**

 5) Change parameters on file: **polling_using_sftp_get.bpml** 

* REMOTE_SFTP_SERVER:  remote sftp server
* REMOTE_SFTP_SERVER_PORT: remote sftp server port, default: 22
* REMOTE_SFTP_PARTNER_NAME: remote username 
* REMOTE_SFTP_PARTNER_PASSWORD: remote password
* REMOTE_SFTP_PARTNER_HOSTKEY: remote SSH hostkey 
* MAILBOX_PATH: /Demo_Local_SFTP

 6) Create a new Business Process: **Demo_BP_Polling_Using_SFTP_Get**, using file **polling_using_sftp_get.bpml** 

 7) Run BP.

