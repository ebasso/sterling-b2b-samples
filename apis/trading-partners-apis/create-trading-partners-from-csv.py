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
import random
import string
import requests,urllib
from requests.auth import HTTPBasicAuth
from datetime import datetime

B2B_URL = 'https://<REPLACE_HERE_IP_AND_PORT_B2B>:<PORT>'
B2B_API_USERNAME = '<REPLACE_HERE>'
B2B_API_PASSWORD = '<REPLACE_HERE>'
B2B_COMMUNITY_NAME = 'DEMO_SFG_COMMUNITY'
CSV_FILENAME = 'trading-partners.csv'

#----------- CSV FIELDS -----------
iPartnerName = 0
iCode = 1
iUsername = 2
iGivename = 3
iSurname = 4
iPhone = 5
iEmailAddress = 6

#----------- HTTP Request ----------- 
auth=HTTPBasicAuth(B2B_API_USERNAME, B2B_API_PASSWORD)
api_url = B2B_URL + '/B2BAPIs/svc/tradingpartners/'

#----------- Random Password -----------
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
#symbols = string.punctuation
#all = lower + upper + num + symbols
all = lower + upper + num


def randomPassword():
    temp = random.sample(all,8)
    return "".join(temp)

def doCreateTradingPartner(partnerData):
    
    headers = { 'Accept': 'application/json' }
    
    res =  requests.post(url=api_url, auth=auth, json=partnerData)

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
            partnerData = {
                'community': B2B_COMMUNITY_NAME,
                'partnerName': row[iPartnerName],
                'code': row[iCode],
                'phone':row[iPhone],
                'timeZone': '-031',
                'emailAddress': row[iEmailAddress],
                'username': row[iUsername],
                'password': randomPassword(),
                'authenticationType': 'Local',
                'givenName': row[iGivename],
                'surname': row[iSurname],
                'isInitiatingConsumer': True,
                'isInitiatingProducer': True,
                'isListeningConsumer': False,
                'isListeningProducer': False,
                'doesUseSSH': True,
                'postalCode': '12345'
            }
            #print(partnerData)
            print ('----- Create Trading Partners: "' + partnerData['partnerName'] + '":"' + partnerData['password'] + '"\n')
            doCreateTradingPartner(partnerData)

            line_count += 1
        print()
    print('Processed ' + str(line_count-1) + ' lines.')



####### Another Fields on REST API
#  "addressLine1": null,
#  "addressLine2": null,
#  "appendSuffixToUsername": false,
#  "asciiArmor": false,
#  "authenticationHost": null,
#  "authenticationType": "Local",
#  "authorizedUserKeyName": null,
#  "city": null,
#  "consumerCdConfiguration": null,
#  "consumerFtpConfiguration": null,
#  "consumerFtpsConfiguration": null,
#  "consumerSshConfiguration": null,
#  "consumerWsConfiguration": null,
#  "countryOrRegion": null,
#  "customProtocolExtensions": null,
#  "customProtocolName": null,
#  "doesRequireCompressedData": false,
#  "doesRequireEncryptedData": false,
#  "doesRequireSignedData": false,
#  "doesUseSSH": true,
#  "isInitiatingConsumer": true,
#  "isInitiatingProducer": true,
#  "isListeningConsumer": false,
#  "isListeningProducer": false,
#  "keyEnabled": false,
#  "mailbox": null,
#  "passwordPolicy": null,
#  "pollingInterval": null,
#  "postalCode": null,
#  "producerCdConfiguration": null,
#  "producerFtpConfiguration": null,
#  "producerFtpsConfiguration": null,
#  "producerSshConfiguration": null,
#  "publicKeyID": null,
#  "remoteFilePattern": null,
#  "sessionTimeout": null,
#  "stateOrProvince": null,
#  "textMode": false,
#  "useGlobalMailbox": false,