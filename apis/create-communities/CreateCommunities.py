# -*- coding: utf-8 -*-
# Using Python3
#
# Necessary libraries:
#
# > pip install requests
#
# or
#
# pip install -r requirements.txt
#
# For documentation on:
#    https://www.ibm.com/support/knowledgecenter/SS4TGX_2.2.0/com.ibm.help.sfg_reference.doc/B2B_APIs_avail.html
#
#

import json
import requests,urllib
from requests.auth import HTTPBasicAuth
from datetime import datetime

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_USERNAME = '<REPLACE_HERE>'
B2B_API_PASSWORD = '<REPLACE_HERE>'

comm_api_url = B2B_URL + '/B2BAPIs/svc/communities/'

def doCreateCommunity(communityName, cdListening=True, ftpListening=True):
    
    data = {
        'name': communityName,
        'cdListening': cdListening,
        'ftpListening': ftpListening,
        'partnerNotificationsEnabled': True,
        'partnersInitiateConnections': False,
        'partnersListenForConnections': True,
        'sshListening': False,
        'wsListening': True
    }

    headers = { 'Accept': 'application/json' }
    auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)

    res = requests.post(url=comm_api_url, auth=auth, json=data)

    if (res.status_code == 201):
        print ( 'Community Created with Sucess %s\n' % (res) )
    else:
        print ( 'Community NOT created-> %s\n' % (res) )

    return res.content


#################### Main Module ###################
print ('Connecting to B2B...\n')


communityName = 'REST_UI_Community' + datetime.now().strftime("_%Y%m%d_%H%M%S")


print('----- Create Community: "' + communityName + '"\n')
print( doCreateCommunity(communityName) )
print('--------------------------------------------------------\n')


