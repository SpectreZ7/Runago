import re

def definition_extract(definitions, words):
    definitions_list = []
    for word in words:
        definition = definitions[word]
        pattern = r"\b[A-Za-z]+\b"
        my_list = re.findall(pattern, definition)
        definitions_list.append(' '.join(my_list[1:]))
    return definitions_list


