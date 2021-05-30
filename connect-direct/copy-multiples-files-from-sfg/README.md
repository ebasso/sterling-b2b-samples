# Copy Multiple Files FROM Sterling File Gateway


Currently Sterling File Gateway don't support copy multiple files using Connect:Direct Protocol

```
 COPYIDX COPY 
	FROM (
		FILE="/mailbox/Inbox/*"
		SNODE
	)
	TO (
		FILE="C:\Inbox"
		PNODEde
		DISP=RPL
	)
```

# Copy from SFG using CDP file

How it works:

1. **copy-from-sfg-cdp.cdp** call business process **MAILBOX_GET_INDEX_CDP**
   
2. **MAILBOX_GET_INDEX_CDP** checks /Inbox and generate file index.cdp using a xslt name **PullListCDP**
   
3. **copy-from-sfg-cdp.cdp** submit file **index.cdp**

Files:

* copy-from-sfg-cdp.cdp : CD process that call business process
* mailbox-get-index-cdp.bpml: business process MAILBOX_GET_INDEX_CDP
* pull-list-cdp.xslt: XSLT file to generate index.cdp

Deploy:

1. Create process **MAILBOX_GET_INDEX_CDP**, with content from mailbox-get-index-cdp.bpml. You must check **Create Permission**
   
2. Create xslt **PullListCDP**, with content file pull-list-cdp.xslt

3. Define permission **MAILBOX_GET_INDEX_CDP** to the partner using copy-from-sfg-cdp.cdp.



# Copy from SFG using CDP file and delete after download

How it works:

1. **copy-from-sfg-cdp-adv.cdp** call business process **MAILBOX_GET_INDEX_CDP_ADV**
   
2. **MAILBOX_GET_INDEX_CDP_ADV** checks /Inbox and generate file index.cdp using a xslt name **PullListCdpAdv**
   
3. **copy-from-sfg-cdp-adv.cdp** submit file **index.cdp**

4.  **index.cdp** run a runtask **MAILBOX_DELETE_FILE_RUNTASK** for each file to delete

Files:

* copy-from-sfg-cdp-adv.cdp : CD process that call business process
* mailbox-get-index-cdp-adv.bpml: business process MAILBOX_GET_INDEX_CDP_ADV
* pull-list-cdp-adv.xslt: XSLT file to generate index.cdp
* mailbox-delete-file-runtask.bpml: business process MAILBOX_DELETE_FILE_RUNTASK

Deploy:

1. Create process **MAILBOX_GET_INDEX_CDP**, with content from mailbox-get-index-cdp-adv.bpml. You must check **Create Permission**

2. Create process **MAILBOX_DELETE_FILE_RUNTASK**, with content from mailbox-delete-file-runtask.bpml. You must check **Create Permission**
   
2. Create xslt **PullListCdpAdv**, with content file pull-list-cdp-adv.xslt

3. Define permission **MAILBOX_GET_INDEX_CDP** to the partner using copy-from-sfg-cdp-adv.cdp.

4. Define permission **MAILBOX_DELETE_FILE_RUNTASK** to the partner using copy-from-sfg-cdp-adv.cdp.

5. Define **MAILBOX_DELETE_FILE_RUNTASK** as run tasks on C:D Server Adapter.



# Copy from SFG using TXT file

How it works:

1. **copy-from-sfg-txt.cdp** call business process **MAILBOX_GET_INDEX_TXT**
   
2. **MAILBOX_GET_INDEX_TXT** checks /Inbox and generate file index.txt using a xslt name **PullListTXT**
   
3. you can create a .sh/.bat to interact with this file

Files:

* copy-from-sfg-txt.cdp : CD process that call business process
* mailbox-get-index-txt.bpml: business process MAILBOX_GET_INDEX_TXT
* pull-list-txt.xslt: XSLT file to generate index.txt

Deploy:

1. Create process **MAILBOX_GET_INDEX_TXT**, with content from mailbox-get-index-txt.bpml. You must check **Create Permission**
   
2. Create xslt **PullListTXT**, with content file pull-list-txt.xslt

3. Define permission **MAILBOX_GET_INDEX_TXT** to the partner using copy-from-sfg-txt.cdp.





# Copy frm SFG using XML file

How it works:

1. **copy-from-sfg-xml.cdp** call business process **MAILBOX_GET_INDEX_XML**
   
2. **MAILBOX_GET_INDEX_XML** checks /Inbox and generate file index.xml
   
3. you can create a .sh/.bat to interact with this file

Files:

* copy-from-sfg-xml.cdp : CD process that call business process
* mailbox-get-index-xml.bpml: business process MAILBOX_GET_INDEX_XML


Deploy:

1. Create process **MAILBOX_GET_INDEX_XML**, with content from mailbox-get-index-xml.bpml. You must check **Create Permission**

2. Define permission **MAILBOX_GET_INDEX_XML** to the partner using copy-from-sfg-xml.cdp.
