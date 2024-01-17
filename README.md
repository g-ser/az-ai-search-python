# Repo Content

This repo contains a simple Python module which defines some functions for interacting with Azure's AI search service. For instance it defines functions for creating an index, retrieving the documents of an index, uploading a document to the search index etc. 

# Run the module in interactive mode<a name="interactive_mode"></a>

You can test the [azSearchService](azSearchService.py) module using Python's interpreter in interactive mode. Below the instructions for doing that are listed.

1. Clone the repository in a directory of your choice:
```git clone git@github.com:g-ser/az-ai-search-python.git```
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


# Run the functions included in the module

After entering the interactive mode by completing all the steps of [Run the module in interactive mode](#interactive_mode) section, you can call the functions defined in the module to experiment. Below you can find some examples:

* Call the [get_number_of_documents_in_a_search_index](azSearchService.py#L19) function

    ![Get documents](/assets/images/get_number_of_documents.png)

* Upload a [document](azSearchService.py##L12) to the [search index](azSearchService.py#L8) using   [upload_document_to_search_index](azSearchService.py#L24) function

    ![Upload document](/assets/images/upload_document.png)

* Delete the previously uploaded document [document](azSearchService.py#L12) from the [search index](azSearchService.py#L8) using [delete_document_from_search_index](azSearchService.py#L32) function

    ![Delete document](/assets/images/delete_document.png)

* List all the documents of the [search index](azSearchService.py#L8) using the function [get_all_documents_in_a_search_index](azSearchService.py#L40)

    ![List documents](/assets/images/list_documents.png)

* Create a [new index](azSearchService.py#L10) in the search service using the function [create_index_in_search_service](azSearchService.py#L58)

    ![Create index](/assets/images/create_index.png)

* Delete the [new index](azSearchService.py#L10) from the search service using the function [delete_index_in_search_service](azSearchService.py#L66)

    ![Delete index](/assets/images/delete_index.png)