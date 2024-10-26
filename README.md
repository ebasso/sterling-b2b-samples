# sterling-b2b-samples
Sterling B2B Samples/Exemplos. Exemplos de BPs, Services, uso de APIs


# APIs

| APIs Name                       |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| cdws-restapi                    | Python code to submit a file using C:D WebServices (RestAPI)|
| code-lists                      | Python code to Create, Read, Update and Delete Code Lists using B2Bi API. Create Code List stored from CSV file|
| create-user-using-xapi          | Create user using XAPI in a business process |
| sfg-communities-apis            | Python code to create Communities using B2Bi API,           |
| sfg-routing-channel-api         | Python code to Creates a Routing Channel in Sterling File Gateway. |
| sfg-routing-channel-xapi        | Sample code that Creates a Routing Channel in Sterling File Gateway using XAPI. |
| trading-partners-apis           | Python code to Create, Read and Update Trading Partners using B2Bi API. List stored on CSV file|


# Business Process

| BPs Name                        |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| bp-parent-to-bp-child-samples   | Examples of BPs that exchange information between parent and child subprocess |
| bp-xml-json-transformation      | Examples of BPs that convert XML to Json format, using XML Json Transformer Service |
| bps-from-ibm-support-com        | IBM Support provide many solutions for Business problems. I will concentrate some of this solutions here for reference|
| check-sum-java-task             | Sample JavaTask that do a checksum of file |
| cmd-line-adapter-example-01     | Sample code that use Command Line Adapter 2 on Linux |
| [code-list-editor-web](business-process/code-list-editor-web) | The UI to manipulate Code List is poor. This solution helps to search and update codes in Code List |
| compress-files                  | Samples BPs to compress files using Compress Service and Zip with command line |
| connect-direct-requester-submit | Sample BP that submit a file on C:D |
| copy-from-filesystem-to-mailbox | Copy File(s) From File System to a Mailbox |
| file-folding                    | Samples BPs to put a new line character every N caracters. Use a Java Task |
| ftp-get-multiple-files          | Polling  Multiple files from a FTP Partner |
| generate-files                  | BP to generate files and write to a mailbox |
| generate-load-on-connect-direct | Business Process to do load on Connect:Direct |
| gzip-compress-java-task         | Compress file using Gzip with Java Task |
| hello-world-json-http-server-adapter| Hello World example on  HTTP Server Adapter |
| hello-world-xml-http-server-adapter| Hello World example on  HTTP Server Adapter |
| polling-file-from-sftp-parner   | Poll a file from a SFTP Partner and delivery it internally  |
| rename-with-regex-java-task     | Samples BP to rename files using Regular Expressions and Java Classes (Match and Pattern).  |
| send-smtp-email                 | Send Email from BP |
| sftp-get-multiple-files         | Polling  Multiple files from a SFTP Partner |
| using-kafka                     | Sample BPs to interact with Kafka, as a producer, consumer |



# Connect Direct

| BPs Name                        |            Description of Role                                          |
|---------------------------------|-------------------------------------------------------------------------|
| cd-check-process-queues-shell   | Sample Script that get output from "select process" command and generate files with quantity of process in queues HOLD and WAIT |
| cd-watch-shell                   | Sample Script that monitor Connect:Direct Unix |
| [copy-multiples-files-from-sfg](connect-direct/copy-multiples-files-from-sfg) | CD Process that copy multiples files FROM SFG |
| [copy-multiples-files-from-sfg-advanced](connect-direct/copy-multiples-files-from-sfg-advanced) | CD Process that copy multiples files FROM SFG and run a runtask to delete from mailbox |
| [copy-multiples-files-to-sfg](connect-direct/copy-multiples-files-to-sfg) | CD Process that copy multiples files TO SFG |
| [silent-install](connect-direct/silent-install) | C:D silent install for Windows |

# Filegateway Scenarios

Samples scenarios to be used on IBM Sterling FileGateway

| Scenarios                           |            Description of Role                                          |
|-------------------------------------|-------------------------------------------------------------------------|
| content-based-routing-01            | File routed based on content inside a CSV file. |
| content-based-routing-02            | File routed based on content inside a XML file. |
| custom-layer-execute-bp             | File layer type that run a Business Process |
| custom-layer-translation            | File layer type that use a Map to translate file |
| dynamic-rct-using-bp-01             | Deliver a file to a Consumer identified by a Business Process(BP)|
| extract-and-delivery-to-multiple-mailboxes | Extract files from a .zip file and delivery to multiple mailboxes defined by file extension|
| [filegateway-advanced-search-for-partners](filegateway-scenarios/filegateway-advanced-search-for-partners) | Web based solution to do Advanced  Search for File Gateway' Partners |
| multiples-consumers-broadcast       | Broadcast one file to multiple partners using a Group|
| multiples-consumers-broadcast-list  | Broadcast one file to multiple partners using a list of ConsumerName's generated by a Business Process|
| route-via-custom-ftp-protocol       | Put a file on FTP Partner using a custom FTP protocol on SFG |
| route-via-custom-protocol           | Sample of a custom protocol that write a file to a filesystem with a custom filename|
| route-via-custom-sftp-client-adapter| Put a file on SFTP Partner using a custom SFTP Client Adapter on Perimeter Server|
| route-via-file-system-adapter       | Sample of a custom protocol that write a file on network shared directory.|
| route-via-http-post                 | Sample of a custom protocol that send a file on HTTP Server.|
| route-via-kafka                     | Sample of a custom protocol that write a file in a Kafka topic|

# Sterling Map Editor

| Scenarios                           |            Description of Role                                          |
|-------------------------------------|-------------------------------------------------------------------------|
| content-based-routing-01            | Map that extract field from CSV file and put in Process Data |
| positional-to-csv-example-01        | Sample map that convert from a Positional file to CSV file |

# Sterling Secure Proxy

| Scenarios                           |            Description of Role                                          |
|-------------------------------------|-------------------------------------------------------------------------|
| secure-proxy-restapi                | Python scritps to configure IBM Sterling Secure Proxy (SSP) using RestAPI  |

# Tools

Samples using Tools provided by IBBM Sterling B2B

| Scenarios                           |            Description of Role                                          |
|-------------------------------------|-------------------------------------------------------------------------|
| import-code-list-using-command-line | Sample code that creates a Code List in Sterling B2B using import.cmd utility |
| create-local-users-for-connect-direct | Sample code that creates a Local Users at MS Windows. For use with Connect:Direct |

# Authors

* **Enio Basso** - [My Repository](https://github.com/ebasso) - [My Site](https://ebasso.net) - [My Wiki](https://ebasso.net/wiki)


# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
