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
import requests,urllib
from requests.auth import HTTPBasicAuth

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_PASSWORD = '<REPLACE_HERE>'
B2B_API_USERNAME = '<REPLACE_HERE>'

#----------- HTTP Request ----------- 
auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
api_url = B2B_URL + '/B2BAPIs/svc/codelists/'

def doDeleteCodeLists(codeListName):

    url = api_url + codeListName
    #print(url)
    
    headers = { 'Accept': 'application/json' }
    
    res =  requests.delete(url=url, auth=auth, headers=headers)

    if (res.status_code != 200):
        print ('requests.post -> %s = %s\n' % (res.url, res) )
        print (res.content)
        return None;

    if (res.headers['Content-Type'] == 'application/json;charset=utf-8'):
        print(res.headers['Content-Type'])

    return res.content



# -------------------------------------------- Main Module  --------------------------------------------
print ('B2B API Service...\n')

#Demo_CL_Test1|||1 --> Code List Name | Sender Identity | Receiver Identity | Version Number
codeListName = "Demo_CL_Test1" + "%7C" + "" + "%7C"  + "" + "%7C" + "1"

print ('----- Delete Code List Demo_CL_Test1 ----\n')
doDeleteCodeLists(codeListName)
