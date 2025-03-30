import random
import requests
import re
from .scramblesentence import scramble_word
from flask import Blueprint,render_template

def clean_definition(definition):
    # Remove parts like {d_link|rudimentary|rudimentary}
    #find all occurrences of the {d_link|...} pattern.
    #regex that matches strings starting with {d_link|, followed by any characters except }, then another |, and captures whatever follows until the next }
    #The replacement r"\1" replaces the entire matched string with just the captured part (what's inside the parentheses in the regex), 
    # effectively removing the {d_link|...|...} part and keeping the last term.
    
    definition = re.sub(r"\{d_link\|[^}]*\|([^}]*)\}", r"\1", definition)
    
    # removes any remaining content within curly braces {}
    #Remove parts like {bc}
    definition = re.sub(r"\{[^}]*\}", "", definition)
    
    return definition.strip()

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
                    
                    # Use the clean_definition function to clean up the definition
                    cleaned_definition = clean_definition(definition)
                    
                    return cleaned_definition

    return ""






