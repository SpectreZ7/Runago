

def checkword(word, shuffled_words):
    for i in range(len(shuffled_words)):
        if shuffled_words[i] == word:
            return i
        

def checkdef(definition, shuffled_definitions):
    for i in range(len(shuffled_definitions)):
        if shuffled_definitions[i] == definition:
            return i


def check_correct(index1, index2):
    if index1 == index2:
        return True
    else:
        return False 

