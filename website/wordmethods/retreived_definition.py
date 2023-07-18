import random
import requests
import re
from .scramblesentence import scramble_word
from flask import Blueprint,render_template



def get_definition(word):
    endpoint = "https://dictionaryapi.com/api/v3/references/collegiate/json/"
    api_key = "dfb4cc17-6bc1-425f-8e41-1c1f590d7d9c"
    
    # Construct the API request URL with the provided word and API key
    url = f"{endpoint}{word}?key={api_key}"

    # Send a GET request to the API and retrieve the response
    response = requests.get(url)

     # Convert the response to a JSON format
    response_dict = response.json()
    
    if response_dict:
        if 'def' in response_dict[0]:
            # Check if the 'def' key exists in the first element of the response dictionary
            if 'sseq' in response_dict[0]['def'][0]:
                # Check if the 'sseq' key exists in the nested structure
                if 'dt' in response_dict[0]['def'][0]['sseq'][0][0][1]:
                    # Access the nested structure to retrieve the definition
                    definition = response_dict[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
                    
                    # Perform additional processing on the definition using regular expressions
                    c = re.search("^{bc}", definition)
                    d = re.search(".*{d_link", definition)
                    
                    if c:
                        # Remove "{bc}" from the definition if it matches at the beginning
                        definition = re.sub("{bc}", "", definition)
                        return definition
                    elif d:
                        # Remove "{d_link|" from the definition if it matches anywhere
                        re.sub("{d_link|", "", definition)
                        return definition
                    else:
                        return definition

    return ""






