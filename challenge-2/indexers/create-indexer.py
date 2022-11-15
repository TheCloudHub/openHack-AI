import requests
import json

url = "https://searchwebdocs.search.windows.net/indexers?api-version=2021-04-30-Preview&search "

payload = json.dumps({
  "name": "webdocs-indexer",
  "dataSourceName": "searchwebdocs-ds",
  "targetIndexName": "webdocs-index",
  "fieldMappings": [
    {
      "sourceFieldName": "metadata_storage_path",
      "targetFieldName": "url",
      "mappingFunction": {
        "name": "urlEncode"
      }
    },
    {
      "sourceFieldName": "metadata_storage_name",
      "targetFieldName": "file_name"
    },
    {
      "sourceFieldName": "metadata_storage_name",
      "targetFieldName": "id",
      "mappingFunction": {
        "name": "base64Encode"
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'api-key': 'your_api_key'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
