import requests
import re
def get_definition(word):
    endpoint = "https://dictionaryapi.com/api/v3/references/collegiate/json/"
    api_key = "dfb4cc17-6bc1-425f-8e41-1c1f590d7d9c"

    url = f"{endpoint}{word}?key={api_key}"
    response = requests.get(url)
    response_dict = response.json()
    
    if response_dict:
        if 'def' in response_dict[0]:
            if 'sseq' in response_dict[0]['def'][0]:
                if 'dt' in response_dict[0]['def'][0]['sseq'][0][0][1]:
                    definition = response_dict[0]['def'][0]['sseq'][0][0][1]['dt'][0][1]
                    c = re.search("^{bc}", definition)
                    if c:
                        definition = re.sub("{bc}", "", definition)
                        print(definition)
                        return definition
                    else:
                        return definition
    return ""
    

words = ["oligopoly", "banana", "unstable", "car", "wordnotindictionary", "altruist", "idiot","pulchritudinous","psychopath"]
for word in words:
    definition = get_definition(word)
    defi = f"Definition for {word}: {definition}"
    print(defi)
