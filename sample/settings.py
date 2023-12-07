token = "<acces-token>"

api_version = "2022-07-01-preview"
resource_groupe_name = "<resource-groupe-name>"
subscription_id = "<subscription-id>"
capacity_name = "<capacity-name>"
sku = "<sku>"
location = "francecentral"
administrators = ["<administrators"]

root_url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_groupe_name}/providers/Microsoft.Fabric/capacities/{capacity_name}"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
    "Content-Type" : "application/json"
}