import requests
import json

url = "https://searchwebdocs.search.windows.net/indexes/webdocs-index/docs/search?api-version=2021-04-30-Preview&search
"

payload = json.dumps({
  "search": "New York",
  "queryType": "simple",
  "searchMode": "all",
  "searchFields": "content",
  "select": "file_name, url, metadata_storage_size,metadata_creation_date",
  "count": "true"
})
headers = {
  'Content-Type': 'application/json',
  'api-key': 'your_api_key'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
