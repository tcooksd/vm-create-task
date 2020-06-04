import requests
import json
import sys

token = sys.argv[1]

#Vars from scripts:
#Replace tcvar01 and tcvar02 with your task field names. 
#hostname =  morpheus["results"]["tcvar01"].rstrip()
#ip = morpheus["results"]["tcvar02"].rstrip()

#Vars from text options:
hostname = morpheus["customOptions"]["tcookhostname"].rstrip()
url1 = morpheus["customOptions"]["appurl"].rstrip() + "/api/"

#Vars from rest populated drop down. 
#instance_type = morpheus["customOptions"]["tcookinstance"].rstrip()

#static var 
ip = "10.0.1.24"


#Function for queries
#accepts:
# api_location = location to access api for return data.
# auth token = token to authenticate against .
#returns:
# json formated string with values queried .
def get_request(api_location, authtoken):
    try:
        response = requests.get(
            url= url1 + api_location ,
            headers={
                'Authorization': 'Bearer %s ' % token,
            },
            verify = False
        )
        json_payload = ('{content}'.format(
                content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
    return json.loads(json_payload)

def launch_vm(hostname1, ip, api_location):
    data01 = """ {
        "zoneId": 2,
        "instance": {
            "name": "%s",
            "cloud": "VMware Demo Cluster",
            "site": {
              "id": 32
            },
            "type": "centos",
            "instanceType": {
              "code": "centos"
            },
            "instanceContext": "dev",
            "layout": {
              "id": 1209
            },
            "plan": {
              "id": 158,
              "code": "vm-1024",
              "name": "1 CPU, 1GB Memory"
            },
            "networkDomain": {
              "id": null
            }
        },
        "plan": {
            "id": 158,
            "code": "vm-1024",
            "name": "1 CPU, 1GB Memory"
          },
        "config": {
            "resourcePoolId": 1081,
            "noAgent": "off",
            "smbiosAssetTag": null,
            "nestedVirtualization": "off",
            "hostId": null,
            "vmwareFolderId": "group-v64130",
            "vmwareCustomSpec": null,
            "createUser": true
        },
        "volumes": [
            {
              "id": -1,
              "rootVolume": true,
              "name": "root",
              "size": 10,
              "sizeId": null,
              "storageType": 1,
              "datastoreId": "auto"
            }
          ],
            "networkInterfaces": [
              {
                  "network": {
                  "id": "network-12458"
              },
              "ipAddress": "%s"
            }
          ]
        }  """ % (hostname1, ip)
    response = requests.post(
        url= url1 + api_location ,
        headers={
            'Authorization': 'Bearer %s ' % token,
            'Content-Type': 'application/json',
            },
        data=data01,
        verify = False
    )

launch_vm(hostname, ip, "instances" )

