# Copy Multiple Files FROM Sterling File Gateway


Currently Connect:Direct Protocol don't support copy multiple files when the partner is using Sterling File Gateway.

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

But in this example i show how to acomplish this

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

Every parameter must be on format var1=value;

Parameters:
* **os=windows;** : return \ in index.cdp. Default Value: /
* **os=unix;** : 
  * return / in index.cdp. Default Value: /
  * add a run task runecho in the case of no files to return
* **os=other;**" : return empty in index.cdp. Default Value: /
* **fi=xyz*;** : filter for filenames on mailox (Message Name Pattern). Default Value: *
* **mbx=@Inbox@SubMbx;** : define Mailbox Path. the character ~ was replaced with  /. Default Value: /Inbox

Deploy:

1. Create process **MAILBOX_GET_INDEX_CDP**, with content from mailbox-get-index-cdp-adv.bpml. You must check **Create Permission**

2. Create process **MAILBOX_DELETE_FILE_RUNTASK**, with content from mailbox-delete-file-runtask.bpml. You must check **Create Permission**
   
3. Create xslt **PullListCdpAdv**, with content file pull-list-cdp-adv.xslt

4. Define permission **MAILBOX_GET_INDEX_CDP** to the partner using copy-from-sfg-cdp-adv.cdp.

5. Define permission **MAILBOX_DELETE_FILE_RUNTASK** to the partner using copy-from-sfg-cdp-adv.cdp.

6. Define **MAILBOX_DELETE_FILE_RUNTASK** as run tasks on C:D Server Adapter.


