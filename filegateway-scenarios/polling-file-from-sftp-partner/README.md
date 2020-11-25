# IBM Sterling File Gateway Scenarios

Polling a file from a SFTP Partner

In this scenario business needs to go out to a partner using SFTP Server and poll for a file with specific name or extension. Once file is found it needs to be delivered internally, putting the retrieved file in a Mailbox.

You can schedule this BP to run every 30 minutes to check for files.

# Files

| BP Name                         |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| polling_using_sftp_get.bpml      | Business Process that do a SFTP get on partner |


# Steps to Run:

On Remote SSH Server

 1) Create a user on remote SSH server
   
 2) Create a file. Example **example_sftp.txt**
 
 3) Import Remote SSH HostKey on B2Bi Dashboard

On Filegateway

 4) Create a Local Partner/Mailbox to receive Files. Example: Demo_SFTP_Partner

On B2Bi Dashboard

 5) Change parameters on file: **polling_using_sftp_get.bpml** 

* REMOTE_SFTP_SERVER
* REMOTE_SFTP_SERVER_PORT
* REMOTE_SFTP_PARTNER_NAME
* REMOTE_SFTP_PARTNER_PASSWORD
* REMOTE_SFTP_PARTNER_HOSTKEY
* Demo_SFTP_Partner

 6) Create a new Business Process: Demo_Polling_Using_SFTP_Get, using file **polling_using_sftp_get.bpml** 

 7) Run BP.

