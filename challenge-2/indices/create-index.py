import requests
import json

url = "https://searchwebdocs.search.windows.net/indexes?api-version=2021-04-30-Preview&search "

payload = json.dumps({
  "name": "webdocs-index",
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "key": True,
      "filterable": True
    },
    {
      "name": "file_name",
      "type": "Edm.String",
      "searchable": True,
      "filterable": True,
      "sortable": True,
      "facetable": True
    },
    {
      "name": "url",
      "type": "Edm.String",
      "searchable": True,
      "filterable": True,
      "sortable": True,
      "facetable": True
    },
    {
      "name": "content",
      "type": "Edm.String",
      "searchable": True,
      "filterable": True,
      "sortable": True,
      "facetable": True
    },
    {
      "name": "metadata_storage_name",
      "type": "Edm.String",
      "searchable": True,
      "filterable": True,
      "sortable": True,
      "facetable": True
    },
    {
      "name": "metadata_creation_date",
      "type": "Edm.DateTimeOffset",
      "filterable": True,
      "sortable": True,
      "facetable": True
    },
    {
      "name": "metadata_storage_size",
      "type": "Edm.Int64",
      "filterable": True,
      "sortable": True,
      "facetable": True
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'api-key': 'your api key'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)