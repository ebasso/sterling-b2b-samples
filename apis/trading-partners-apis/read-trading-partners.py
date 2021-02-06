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
B2B_COMMUNITY_NAME = '<REPLACE_HERE>'


trading_api_url = B2B_URL + '/B2BAPIs/svc/tradingpartners/'

def doReadTradingPartners(params):

    url = trading_api_url + '?'+ urllib.parse.urlencode(params)
    headers = { 'Accept': 'application/json'}
    auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)

    res = requests.get(url=url,headers=headers,auth=auth)

    if (res.status_code != 200):
        print ('Cannot Read Trading Partners \n requests.get -> %s = %s\n' % (res.url, res) )
        return None;

    return res.content



# -------------------------------------------- Main Module  --------------------------------------------
print ('Connecting to B2B...\n')


print ('----- Read Trading Partners: \n')

# you can remove _include to print all fields
params = {
    '_range': '0-100',
    'searchFor': '',
    '_include':'community'
}

print ( doReadTradingPartners(params) )
print ('--------------------------------------------------------\n')
