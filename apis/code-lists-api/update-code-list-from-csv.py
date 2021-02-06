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
import csv
import requests,urllib
from requests.auth import HTTPBasicAuth
from datetime import datetime

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_USERNAME = '<REPLACE_HERE>'
B2B_API_PASSWORD = '<REPLACE_HERE>'
CSV_FILENAME = 'code-list-codes-updates.csv'

#----------- CSV FIELDS -----------
iReceiverCode = 0
iSenderCode = 1
iDescription = 2
iText1 = 3
iText2 = 4
iText3 = 4
iText4 = 5
iText5 = 6
iText6 = 7
iText7 = 9
iText8 = 10
iText9 = 11

#----------- HTTP Request ----------- 
auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
api_url = B2B_URL + '/B2BAPIs/svc/codelists/'

def doUpdateCodeLists(codeListName,codeListData):

    url = api_url + codeListName
    print(url)
    
    headers = { 'Accept': 'application/json' }
    
    res =  requests.put(url=url, auth=auth, headers=headers, json=codeListData)

    if (res.status_code != 200):
        print ('requests.post -> %s = %s\n' % (res.url, res) )
        print (res.content)
        return None;

    if (res.headers['Content-Type'] == 'application/json;charset=utf-8'):
        print(res.headers['Content-Type'])

    return res.content



# -------------------------------------------- Main Module  --------------------------------------------
print ('B2B API Service...\n')

codes = []
with open(CSV_FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #print(row)
        if line_count == 0:
            line_count += 1
        else:
            codeData = {
              'description': row[iDescription],
              'receiverCode': row[iReceiverCode],
              'senderCode': row[iSenderCode],
              'text1': row[iText1],
              'text2': row[iText2],
              'text3': row[iText3],
              'text4': row[iText4],
              'text5': row[iText5],
              'text6': row[iText6],
              'text7': row[iText7],
              'text8': row[iText8],
              'text9': row[iText9]
            }
            codes.append(codeData)
            line_count += 1
        print()
    print('Processed ' + str(line_count-1) + ' lines.')

#Demo_CL_Test1|||1 --> Code List Name | Sender Identity | Receiver Identity | Version Number
codeListName = "Demo_CL_Test1" + "%7C" + "" + "%7C"  + "" + "%7C" + "1"
strnow = datetime.now().strftime("_%Y%m%d_%H%M%S")
codeListData = {
  "comments": strnow,
  "listStatus": 1,
  "makeDefault": True,
  "codes": codes
}

print(codeListData)

print ('----- Update Code List Demo_CL_Test1 ----\n')
doUpdateCodeLists(codeListName, codeListData)
