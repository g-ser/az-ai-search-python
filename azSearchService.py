from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import SearchIndex
import os

service_endpoint = ''
index_name = ''
key = os.getenv("AZURE_SEARCH_API_KEY")
index_name_new = ''

document =  {
    "id": "1",
    "title": "Test Document",
    "content": "This is a test document to be uploaded to an Azure Search index."
}


def get_number_of_documents_in_a_search_index(service_endpoint, index_name, key):
    # create search client object
    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))
    return search_client.get_document_count()

def upload_document_to_search_index(service_endpoint, index_name, key, document):
    # create search client object
    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))
    
    # upload the document to the search index
    search_client.upload_documents(documents=[document])
    print("Document uploaded successfully!")

def delete_document_from_search_index(service_endpoint, index_name, key, document):
    # create search client object
    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))
    
    # delete the document from the search index
    search_client.delete_documents(documents=[document])
    print("Document deleted successfully!")

def get_all_documents_in_a_search_index(service_endpoint, index_name, key):
    # create search client object
    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))
    
    # get all documents in the search index
    results = search_client.search(search_text="*", top=10000)
    document_names = [result["title"] for result in results]
    return document_names

def list_indexes_in_search_service(service_endpoint, key):
    # create search index client object
    index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(key))
    
    # get all indexes in the search service
    results = index_client.list_indexes()
    # index_names = [result["name"] for result in results]
    return results

def create_index_in_search_service(service_endpoint, key, index_name):
    # create search index client object
    index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(key))
    # create search index object definition
    search_index = SearchIndex(name=index_name, fields=[{"name": "id", "type": "Edm.String", "key": True, "searchable": False}, {"name": "title", "type": "Edm.String", "searchable": True}, {"name": "content", "type": "Edm.String", "searchable": True}])
    # create search index in the search service
    return index_client.create_index(search_index)

def delete_index_in_search_service(service_endpoint, key, index_name):
    # create search index client object
    index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(key))
    # delete search index in the search service
    return index_client.delete_index(index_name)