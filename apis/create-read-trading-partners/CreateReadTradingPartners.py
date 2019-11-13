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

trading_api_url = B2B_URL + '/B2BAPIs/svc/tradingpartners/'


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

def doCreateTradingPartner(partnerData):
    
    headers = { 'Accept': 'application/json' }
    auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)

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
    auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)

    res = requests.get(url=url,headers=headers,auth=auth)

    if (res.status_code != 200):
        print ('Cannot Read Trading Partners \n requests.get -> %s = %s\n' % (res.url, res) )
        return None;

    return res.content

#################### Main Module ###################
print ('Connecting to B2B...\n')


strnow = datetime.now().strftime("_%Y%m%d_%H%M%S")

partnerData = {
    'username': 'demopartner' + strnow,
    'partnerName': 'REST_API_Partner' + strnow,
    'authenticationType': 'Local',
    'community': 'REST_UI_Community' + strnow,
    'emailAddress': 'kk@ibm.com',
    'givenName': 'Demo',
    'isInitiatingConsumer': False,
    'isInitiatingProducer': True,
    'isListeningConsumer': False,
    'isListeningProducer': False,
    'doesUseSSH': False,
    'password': 'password',
    'phone':'1234567891',
    'postalCode': '12345',
    'surname': 'Partner'
}

print ('----- Create Community \n')
doCreateCommunity('REST_UI_Community' + strnow)

print ('----- Create Trading Partners: "' + partnerData['username'] + '":"' + partnerData['partnerName'] + '"\n')
print ( doCreateTradingPartner(partnerData) )
print ('--------------------------------------------------------\n')

print ('----- Read Trading Partners: \n')

# you can remove _include to print all fields
params = {
    '_range': '0-100',
    'searchFor': '',
    '_include':'community'
}

print ( doReadTradingPartners(params) )
print ('--------------------------------------------------------\n')
