import os
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    ComplexField,
    CorsOptions,
    SearchIndex,
    ScoringProfile,
    SearchFieldDataType,
    SimpleField,
    SearchableField
)

endpoint = "https://searchwebdocs.search.windows.net"
key = "VetajnX171BkMmynXujnVRFAibwJnT7zOhtHPcXdGoAzSeAQ4aKF"

# Create a service client
client = SearchIndexClient(endpoint, AzureKeyCredential(key))

#  the index name
name = "webdocs-index"
