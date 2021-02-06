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
import requests
from requests.auth import HTTPBasicAuth

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_PASSWORD = '<REPLACE_HERE>'
B2B_API_USERNAME = '<REPLACE_HERE>'


#----------- HTTP Request ----------- 
auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
api_url = B2B_URL + '/B2BAPIs/svc/codelists/'

def doReadCodeLists(codeListName):

    url = api_url + codeListName
    #print(url)
    
    headers = { 'Accept': 'application/json' }
    
    res =  requests.get(url=url, auth=auth, headers=headers)

    if (res.status_code != 200):
        print ('requests.post -> %s = %s\n' % (res.url, res) )
        print (res.content)
        return None;

    if (res.headers['Content-Type'] == 'application/json; charset=UTF-8'):
        return res.json()

    return res.content



# -------------------------------------------- Main Module  --------------------------------------------
print ('B2B API Service...\n')

#Demo_CL_Test1|||1 --> Code List Name | Sender Identity | Receiver Identity | Version Number
codeListName = "Demo_CL_Test1" + "%7C" + "" + "%7C"  + "" + "%7C" + "1"

print ('----- Read Code List Demo_CL_Test1 ----\n') 
codeListData = doReadCodeLists(codeListName)

print ('----- Show Code List ----\n')
#print(codeListData)
print("_id: %s" % codeListData['_id'])
print('codeListName: %s' % codeListData['codeListName'])
print('versionNumber: %s' % codeListData['versionNumber'])
print('comments: %s' % codeListData['comments'])
print('createDate: %s' % codeListData['createDate'])
print('userName: %s' % codeListData['userName'])
print('listStatus: %s' % codeListData['listStatus'])
print('createDate: %s' % codeListData['createDate'])
print()

print('List Codes\n')
for code in codeListData['codes']:
    print('   senderCode: %s' % code['senderCode'])
    print('   receiverCode: %s' % code['receiverCode'])
    print('   description: %s' % code['description'])
    print('   text1: %s' % code['text1'])
    print('   text2: %s' % code['text2'])
    print()

