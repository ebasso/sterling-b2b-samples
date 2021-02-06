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

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_USERNAME = '<REPLACE_HERE>'
B2B_API_PASSWORD = '<REPLACE_HERE>'
CSV_FILENAME = 'routing-channels.csv'

#----------- CSV FIELDS -----------
iRoutingTemplate = 0
iProducer = 1
iConsumer = 2
iFact1 = 3
iFact2 = 4
iFact3 = 5
iFact4 = 6
iFact5 = 7
iFact6 = 8
iFact7 = 9
iFact8 = 10
iFact9 = 11

#----------- HTTP Request ----------- 
auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
api_url = B2B_URL + '/B2BAPIs/svc/routingchannels/'

def doCreateRC(codeListData):
    
    headers = { 'Accept': 'application/json' }
    
    res =  requests.post(url=api_url, auth=auth, json=codeListData)

    if (res.status_code != 200):
        print ('requests.post -> %s = %s\n' % (res.url, res) )
        print (res.content)
        return None;

    if (res.headers['Content-Type'] == 'application/json;charset=utf-8'):
        print(res.headers['Content-Type'])

    return res.content


# -------------------------------------------- Main Module  --------------------------------------------
print ('B2B API Service...\n')

with open(CSV_FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #print(row)
        if line_count == 0:
            line_count += 1
        else:      
            rcData = {
                'templateName': row[iRoutingTemplate],
                'producer': row[iProducer],
                'consumer': row[iConsumer],
                'provisioningFacts': []
            }
            #print(partnerData)
            print ('----- Create RC: "' + rcData['templateName'] + ' | ' + rcData['producer'] + ' | ' + rcData['consumer']+ '"\n')
            doCreateRC(rcData)

            line_count += 1
        print()
    print('Processed ' + str(line_count-1) + ' lines.')

#provisioningFacts = [
#    {
#        'provFactName': 'myFact1',
#        'provFactValue': 'blabla'
#    },
#        {
#        'provFactName': 'myFact2',
#        'provFactValue': 'blabla2'
#    }
#]
