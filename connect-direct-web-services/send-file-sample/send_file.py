#!/usr/local/bin/python3.11
# encoding: utf-8

# Necessary libraries:
#
# > pip install requests
#
#
import time, json, re
import requests,urllib
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth

#json_process_file = {'processFile': "/home/cdadmin01/copy.cdp" }
#json_process_file = {'processFile': "COPY2CD PROCESS SNODE=CDNODE03 CPY0 COPY FROM (FILE=/home/cdadmin02/sample1.txt PNODE) TO (FILE=/home/cdadmin02/sample1.txt SNODE DISP=RPL) PEND" }
json_process_file = {
    'processFile': 'COPY2CD PROCESS SNODE=&DST_NODE CPY0 COPY FROM (FILE="&SRC_FILE" PNODE) TO (FILE="&DST_FILE" SNODE DISP=RPL) PEND',
    '&DST_NODE': 'CDNODE03',
    '&SRC_FILE': '/home/cdadmin01/sample1.txt',
    '&DST_FILE': '/home/cdadmin02/sample1.txt'
}

# # Example of copy-cd2-cdx-param.cdp
# CopyCD2CDX PROCESS
# 	 SNODE=&DST_NODE
#  CPY0  COPY
#  FROM  (
# 	 FILE="&SRC_FILE"
# 	 PNODE
#  )
#  TO (
# 	 FILE="&DST_FILE"
# 	 DISP=rpl
# 	 SNODE
#  )
#  PEND


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CDWSSendFile:

    def __init__(self):
        self.hostname = 'https://127.0.0.1:9443'
        self.loginname = '<cd admin>'
        self.password = '<password>'
        self.cdnode_address = '127.0.0.1'
        self.cdnode_port = 1363
        self.cdnode_protocol = 'TLS1.2'
        self.authorization = None
        self.x_xsrf_token = None
        self.cookie = None
        self.signon()

    def signon(self):
        url = self.hostname + '/cdwebconsole/svc/signon'
        plain_credentials = self.loginname + ":" + self.password
        encoded_credentials = base64.b64encode(plain_credentials.encode()).decode()

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json; charset=utf-8",
            "X-XSRF-TOKEN": "Y2hlY2tpdA==", # do not change, fixed for the first time
            "Cache-Control": "no-cache"
        }

        json = {
            "ipAddress": self.cdnode_address,
            "port": int(self.cdnode_port),
            "protocol": self.cdnode_protocol,  # Change to "TLS1.2" or "TLS1.3" as needed
        }

        response = requests.post(url, headers=headers, json=json, verify=False)

        if (response.status_code != 200):
            print('signon: Failed = ', response.json())
            return None

        print('signon: OK')
        
        self.authorization = response.headers.get('Authorization')
        self.cookie = response.headers.get('Set-Cookie')
        if self.cookie:
            cookies = self.cookie.split(';')
            for cookie in cookies:
                if cookie.strip().startswith('XSRF-TOKEN='):
                    self.x_xsrf_token = cookie.split('=')[1]
                    break


    def submit_process(self):
        url = self.hostname + '/cdwebconsole/svc/processcontrolcriterias'
        headers = {'Accept': 'application/json',
                    'CONTENT-TYPE':'application/json',
                    'Authorization':self.authorization,
                    'Cookie':self.cookie,
                    'X-XSRF-TOKEN': self.x_xsrf_token
                   }

        print("submit_process: Submitting Process ...")
        response = requests.post(url=url, headers=headers, json=json_process_file, verify=False)
        if response.ok:
            print("submit_process: Response OK: " + response.text)
            num = re.compile('[0-9]+')  # compile regular expression pattern
            procNum = num.findall(response.text)  # Get numbers from response
            pnum = int(procNum[1])  # Get process number from the list
        else:
            print("submit_process: Error occurred during process submission : " + response.text)
            return None
        
        print("submit_process: Process submission completed !!")
        return pnum

    def select_stats(self, processNumber):
        url = self.hostname + '/cdwebconsole/svc/selectstatistics'
        headers = {'Accept': 'application/json',
                    'CONTENT-TYPE': 'application/json',
                    'Authorization': self.authorization,
                    'Cookie': self.cookie,
                    'X-XSRF-TOKEN': self.x_xsrf_token
                   }
        print("select_stats: Select statistics pnum=" + str(processNumber) + " ...")
        pnum = {"processNumber": processNumber }
        response = requests.get(url=url, headers=headers, params=pnum, verify=False)
        if response.ok:
            print("select_stats: Response OK: " + response.text)
        else:
            print("select_stats: Error occurred during fetching statistics : " + response.text)


    def signout(self):
        url = self.hostname + '/cdwebconsole/svc/signout'
        headers = {'Accept': 'application/json',
                    'CONTENT-TYPE': 'application/json',
                    'Authorization': self.authorization,
                    'Cookie': self.cookie,
                    'X-XSRF-TOKEN': self.x_xsrf_token
                   }
        json = {'userAccessToken': self.authorization}

        response = requests.delete(url=url, headers=headers, json=json, verify=False)
        if response.ok:
            print("signout: OK ")
        else:
            print("signout: Failed = " + response.text)


#################### Main Module ###################
print('Connecting to IBM C:D WebServices ...\n')

sendfile = CDWSSendFile()

pnum = sendfile.submit_process()

if pnum is not None:
    time.sleep(10)
    sendfile.select_stats(pnum)

sendfile.signout()
