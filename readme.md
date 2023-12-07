

Microsoft Fabric is in GA but the documentation of the management API is not yet available.
This document describe how to use the management API based of the reverse enginnering of Azure portal.

I provide here some [python examples](/sample/) to try. You must update __settings.py__ with your informations.

This document describes the behaviour for this version: 
```
<api-version> = 2022-07-01-preview
```

# Connection to API
## Aquire token

Get a token from Azure to manage the Azure API. One way to get the token is to use [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli). All information about the Azure API are available on [Microsoft documentation](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resources-rest?tabs=azure-cli).

After the installation, execute the folllowing steps.

1. Connect to Azure

Connect to Azure and select the target subscription
``` bash
az login
```
2. Aquire the token

Get the token with a scope to _"https://management.azure.com"_
``` bash
az account get-access-token --resource="https://management.azure.com"
```

The result of the previous command:
``` json
{
  "accessToken": "<access-token>",
  "expiresOn": "2023-12-07 10:24:28.000000",
  "expires_on": 1701941068,
  "subscription": "<subscription-id>",
  "tenant": "<tenant-id>",
  "tokenType": "Bearer"
}
```

## Headers
For each request, the headers must contain the folowing items:
``` json
{
    "Authorization": "Bearer <access-token>",
    "Content-Type" : "application/json"
}
```

# Operations
## Create a capacity

Request
``` http
PUT /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com

{
    "properties": {
        "administration" : {
            "members" : [
                <administrators>
            ]
        }
    },
    "sku": {
        "name": "<sku>",
        "tier": "Fabric"
    },
    "location": "<location>"
}
```
Response
``` http
HTTP/1.1 201 CREATED
Content-Type: application/json

{
    "provisioningState": "Provisioning",        
    "state": "Provisioning",
    "administration": 
        {
            "members": [<administrators>]
        },
    "id": "/subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>",
    "name": "<capacity-name>",
    "type": "Microsoft.Fabric/capacities",
    "location":"<location>",
    "sku": { 
        "name":"<sku>",
        "tier":"Fabric"
    }
}
```

Sample: [capacity_create.py](/sample/capacity_create.py)
## Remove a capacity

Request
``` http
DELETE /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com
```

Response
``` http
HTTP/1.1 202 Accepted
```

Sample: [capacity_remove.py](/sample/capacity_remove.py)

## Show capacity information

Request
``` http
GET /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com
```
Response:
``` http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "provisioningState": "Succeeded",        
    "state": "Active",
    "administration": 
        {
            "members": [<administrators>]
        },
    "id": "/subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>",
    "name": "<capacity-name>",
    "type": "Microsoft.Fabric/capacities",
    "location":"<location>",
    "sku": { 
        "name":"<sku>",
        "tier":"Fabric"
    }
}
```

Sample: [capacity_show.py](/sample/capacity_show.py)

## Suspend a capacity

Request
``` http
POST /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>/suspend?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com
```

Response
``` http
HTTP/1.1 202 Accepted
```

Sample: [capacity_suspend.py](/sample/capacity_suspend.py)

## Resume a capacity
Request
``` http
POST /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>/resume?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com
```

Response
``` http
HTTP/1.1 202 Accepted
```

Sample: [capacity_resume.py](/sample/capacity_resume.py)


## Change SKU

Request
``` http
PATCH /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com
    "sku": {
        "name": f"<sku>",
        "tier": "Fabric"
    }
```

Response:
``` http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "provisioningState": "Succeeded",        
    "state": "Active",
    "administration": 
        {
            "members": [<administrators>]
        },
    "id": "/subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>",
    "name": "<capacity-name>",
    "type": "Microsoft.Fabric/capacities",
    "location":"<location>",
    "sku": { 
        "name":"<sku>",
        "tier":"Fabric"
    }
}
```

Sample: [capacity_scale.py](/sample/capacity_scale.py)


## Change administrators

Request
``` http
PATCH /subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>?api-version=<api-version>
Authorization: Bearer <access-token>
Content-Type: application/json
Host: management.azure.com
    "properties": {
        "administration" : {
            "members" : [
                <administrators>
            ]
        }
    }
```

Response:
``` http
HTTP/1.1 200 OK
Content-Type: application/json
{
    "provisioningState": "Succeeded",        
    "state": "Active",
    "administration": 
        {
            "members": [<administrators>]
        },
    "id": "/subscriptions/<subscription-id>/resourceGroups/<resource-groupe-name>/providers/Microsoft.Fabric/capacities/<capacity-name>",
    "name": "<capacity-name>",
    "type": "Microsoft.Fabric/capacities",
    "location":"<location>",
    "sku": { 
        "name":"<sku>",
        "tier":"Fabric"
    }
}
```

_:warning: The capacity must be started. If the capacity is not started, the API will send a success status but will do nothing_

Sample: [capacity_admins.py](/sample/capacity_admins.py)



