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
#    https://www.ibm.com/support/knowledgecenter/SS3JSW_6.0.1/developing/developing/filegateway/B2B_APIs_avail.html
#
#
import json
import requests,urllib
from requests.auth import HTTPBasicAuth
from datetime import datetime

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_USERNAME = '<REPLACE_HERE>'
B2B_API_PASSWORD = '<REPLACE_HERE>'

auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
api_url = B2B_URL + '/B2BAPIs/svc/communities/'

def doCreateCommunity(communityData):
    
    headers = { 'Accept': 'application/json' }

    res = requests.post(url=api_url, auth=auth, json=communityData)

    if (res.status_code == 201):
        print ( 'Community Created with Sucess %s\n' % (res) )
    else:
        print ( 'Community NOT created-> %s\n' % (res) )

    return res.content


# -------------------------------------------- Main Module  --------------------------------------------
print ('B2B API Service...\n')

communityData = {
    'name': 'DEMO_SFG_COMMUNITY',
    'cdListening': True,
    'ftpListening': True,
    'partnerNotificationsEnabled': True,
    'partnersInitiateConnections': True,
    'partnersListenForConnections': True,
    'sshListening': True,
    'wsListening': False
}

print('----- Create Community: "' + communityData['name'] + '"\n')
print( doCreateCommunity(communityData) )
print('--------------------------------------------------------\n')


