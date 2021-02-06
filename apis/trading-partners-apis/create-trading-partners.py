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

auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
comm_api_url = B2B_URL + '/B2BAPIs/svc/communities/'
trading_api_url = B2B_URL + '/B2BAPIs/svc/tradingpartners/'


def doCreateCommunity(communityData):

    headers = { 'Accept': 'application/json' }

    res = requests.post(url=comm_api_url, auth=auth, json=communityData)

    if (res.status_code == 201):
        print ( 'Community Created with Sucess %s\n' % (res) )
    else:
        print ( 'Community NOT created-> %s\n' % (res) )

    return res.content

def doCreateTradingPartner(partnerData):
    
    headers = { 'Accept': 'application/json' }

    res =  requests.post(url=trading_api_url, auth=auth, json=partnerData)

    if (res.status_code != 200):
        print ('requests.post -> %s = %s\n' % (res.url, res) )
        print (res.content)
        return None;

    if (res.headers['Content-Type'] == 'application/json;charset=utf-8'):
        print(res.headers['Content-Type'])

    return res.content

def doReadTradingPartners(params):

    url = trading_api_url + '?'+ urllib.parse.urlencode(params)
    headers = { 'Accept': 'application/json'}

    res = requests.get(url=url,headers=headers,auth=auth)

    if (res.status_code != 200):
        print ('Cannot Read Trading Partners \n requests.get -> %s = %s\n' % (res.url, res) )
        return None;

    return res.content

#################### Main Module ###################
print ('Connecting to B2B...\n')


strnow = datetime.now().strftime("_%Y%m%d_%H%M%S")



communityData = {
    'name': 'DEMO_SFG_COMMUNITY',
    'cdListening': True,
    'ftpListening': True,
    'partnerNotificationsEnabled': True,
    'partnersInitiateConnections': True,
    'partnersListenForConnections': True,
    'sshListening': True,
    'wsListening': True
}

print('----- Create Community: "' + communityData['name'] + '"\n')
print( doCreateCommunity(communityData) )
print ('\n\n')

partnerData = {
    'username': 'demopartner' + strnow,
    'partnerName': 'REST_API_Partner' + strnow,
    'authenticationType': 'Local',
    'community': 'DEMO_SFG_COMMUNITY',
    'emailAddress': 'kk@ibm.com',
    'givenName': 'Demo',
    'isInitiatingConsumer': True,
    'isInitiatingProducer': True,
    'isListeningConsumer': False,
    'isListeningProducer': False,
    'doesUseSSH': True,
    'password': 'password',
    'phone':'1234567891',
    'postalCode': '12345',
    'surname': 'Partner'
}

print ('----- Create Trading Partners: "' + partnerData['username'] + '":"' + partnerData['partnerName'] + '"\n')
print ( doCreateTradingPartner(partnerData) )
print ('\n\n')


print ('----- Read Trading Partners: \n')
# you can remove _include to print all fields
params = {
    '_range': '0-100',
    'searchFor': '',
    '_include':'community'
}
print ( doReadTradingPartners(params) )
print ('\n\n')
