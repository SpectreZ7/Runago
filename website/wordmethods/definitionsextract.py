import re

def definition_extract(definitions):
    definitions_list = []
    for key in definitions:
        definition = definitions[key]
        pattern = r"\b[A-Za-z]+\b"
        my_list = re.findall(pattern, definition)
        definitions_list.append(' '.join(my_list[1:]))
    return definitions_list



