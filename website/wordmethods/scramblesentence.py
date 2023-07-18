import random




def scramble_word(definition):
    input_scram = definition
    input_words = input_scram.split()
    scrambled_words = []
    # Using list comprehension to scramble each word in the 'input_words' list.
    # For each 'word' in 'input_words', a new scrambled word is created by using list comprehension to select each character 'char' from the 'word'.
    # The characters are sampled in random order using the 'random.sample' function, and then joined back together using the '"".join' method.
    # The resulting scrambled words are stored in the 'scrambled_words' list.
    for word in input_words:
        scrambled_word = "".join(random.sample([char for char in word], len(word)))
        scrambled_words.append(scrambled_word)
    scrambled_sentence = " ".join(scrambled_words)
    # Joining the scrambled words in the 'scrambled_words' list to form a scrambled sentence.

    return scrambled_sentence