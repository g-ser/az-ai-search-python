# Repo Content

This repo contains a simple Python module which defines some functions for interacting with Azure's AI search service. For instance it defines functions for creating an index, retrieving the documents of an index, uploading a document to the search index etc. 

# Run the module in interactive mode

You can test the [azSearchService](azSearchService.py) module using Python's interpreter in interactive mode. Below the instructions for doing that are listed.

1. Clone the repository in a directory of your choice:
```git clone git@personal:g-ser/az-ai-search-python.git```
2. It is recommended to create a Python virtual environment where the required libraries will be installed. Run the commands below within the ```az-ai-search-python``` folder that you cloned:
    * Create the virtual environment: ```python3 -m venv .venv```
    * Activate virtual environment: ```source .venv/bin/activate```
    * Test that you are working on the expected Python virtual environment that you created above: ```which python```
3. Install the required libraries. Run the following commands within the ```az-ai-search-python``` folder: 
    * ```pip install azure-core``` 
    * ```pip install azure-search-documents```
4. Export the Azure Search API Key. Make sure that you provide the right key.
    * ```export AZURE_SEARCH_API_KEY="<AZURE_SEARCH_API_KEY>"```
5. Make sure that the environment variable is exported correctly:
    * ```echo $AZURE_SEARCH_API_KEY```
6. Make sure that you provide the correct values for the variables ```service_endpoint```, ```index_name``` and ```index_name_new``` in [azSearchService](azSearchService.py) file.
7. Enter the interpreter's interactive mode by simply typing ```python``` in the CLI. (make sure that you enter the interactive mode while in ```az-ai-search-python``` folder)
8. Import all the definitions of the [azSearchService](azSearchService.py) by running the following command in the interactive mode: ```from azSearchService import *```
9. Now you can start calling the functions defined in [azSearchService](azSearchService.py). For example you can get the number of documents in the search index by running: ```get_number_of_documents_in_a_search_index(service_endpoint, index_name, key)``` or you can get all the documents in the search index ```get_all_documents_in_a_search_index(service_endpoint, index_name, key)```