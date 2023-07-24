
from flask import Blueprint,render_template,request
from flask_login import login_required, current_user
from .wordmethods.retreived_definition import get_definition
from flask import jsonify, session
from .wordmethods.scramblesentence import scramble_word
from .wordmethods.definitionsextract import definition_extract
import random
import numpy as np


pages = Blueprint('pages',__name__)
@pages.route('/')
@login_required
def home():
    return render_template("home2.html", user =current_user )
@pages.route('/games')
def games():
    return render_template("games.html", user =current_user )


@pages.route('/scramblewg', methods=['GET', 'POST'])
def scramblewg():
    if request.method == 'POST':
        words = request.form.getlist('word')
        definitions = [get_definition(word) for word in words]
        # Using list comprehension to retrieve the definitions for each word in the 'words' list.
        # The 'get_definition' function is called for each 'word' in the 'words' list,
        # and the resulting definitions are stored in the 'definitions' list.
        scrambled_definitions = [scramble_word(definition) for definition in definitions]
        # Using list comprehension to scramble each definition in the 'definitions' list.
        # The 'scramble_word' function is called for each 'definition' in the 'definitions' list,
        # and the resulting scrambled definitions are stored in the 'scrambled_definitions' list.
        return render_template("scrambleplay.html", user=current_user, scrambled_definitions=scrambled_definitions, words = words)
    return render_template("scramblewg.html", user=current_user)

@pages.route('/library')
def library():
    return render_template("library.html", user = current_user)


@pages.route('/scrambleplay', methods=['GET', 'POST'])
def scrambleplay():
    if request.method == 'POST':
        words = request.json
        session["words"] = words  # Store words in session
        #When a POST request is received, the JSON data from the request is stored in the session using session["words"].
        definitions = {}
        for i in words:
            definitions[i] = get_definition(i)
        extracted_definitions = definition_extract(definitions)
        scrambled_definitions = [scramble_word(definition) for definition in extracted_definitions]
        session["scrambled_definitions"] = scrambled_definitions  # Store scrambled definitions in session
        return jsonify(scrambled_definitions=scrambled_definitions) 
    else:
        words = session.get("words", [])  # Retrieve words from session
        #When a GET request is received, the words are retrieved from the session using session.get().
        definitions = [get_definition(word) for word in words]
        scrambled_definitions = session.get("scrambled_definitions", [])  # Retrieve scrambled definitions from session
        
        shuffled_definitions = scrambled_definitions.copy()
        shuffled_words = words.copy()
        def_word_tup = list(zip(shuffled_definitions, shuffled_words))
        def_words_tup = list(zip(words, definitions))
        
        

        random.shuffle(shuffled_definitions)
        random.shuffle(shuffled_words)

        
        words_json = jsonify(shuffled_words)
        definitions_json = jsonify(shuffled_definitions)
        def_word_json = jsonify(def_word) 
        print(def_words)   
        print(def_word)    

        # q:are there any issues in this project, because i am getting a TypeError: Object of type Response is not JSON serializable
        # a: the issue is that you are trying to jsonify a list of tuples, which is not possible. You can only jsonify a dictionary or a list of dictionaries.
        # q: how do i fix it
        # a: you can use the zip function to combine the words and definitions into a list of dictionaries, and then jsonify the list of dictionaries.
        # q: I thought the zip function automatically makes them into tuples, how do i put it into a list of dictionaries?
        # a: you can use the list function to convert the zip object into a list.
        # q: did i not do that here?
        # a: you did, but you are trying to jsonify the list of tuples, which is not possible. You can only jsonify a dictionary or a list of dictionaries.
        # q: is this wrong? : def_word = list(zip(shuffled_definitions, shuffled_words))
        # a: yes, you are trying to jsonify a list of tuples, which is not possible. You can only jsonify a dictionary or a list of dictionaries.
        # q: but list(zip(shuffled_definitions, shuffled_words)) is a list of dictionaries, right?
        # a: no, it is a list of tuples. You can only jsonify a dictionary or a list of dictionaries.
        # q: give me the code to fix it
        

        



        

        return render_template("scrambleplay.html", scrambled_definitions=scrambled_definitions, words=words, user=current_user, enumerate=enumerate, shuffled_definitions=shuffled_definitions, shuffled_words=shuffled_words,words_json=words_json, definitions_json=definitions_json, def_word_json=def_word_json, def_word=def_word)

@pages.route('/crosswordg', methods=['GET', 'POST'])
def crosswordg():
    if request.method == 'POST':
        words = request.form.getlist('word') # Retrieve the values of the form field 'word' as a list
        definitions = [get_definition(word) for word in words]
        return render_template("crosswordgenerator.html", user=current_user, definitions=definitions, words = words)
    return render_template("flashcardswg.html", user=current_user)

@pages.route('/crosswordgenerator', methods=['GET', 'POST'])
def crosswordgenerator():
    if request.method == 'POST':
        words = request.json # Retrieve the JSON data from the request body
        if request.is_json:
            print(words)
        session["words"] = words
        definitions = {}
        for i in words:
            definitions[i] = get_definition(i)
        extracted_definitions = definition_extract(definitions)
        scrambled_definitions = [scramble_word(definition) for definition in extracted_definitions]
        session["scrambled_definitions"] = scrambled_definitions  # Store scrambled definitions in session
        return jsonify(scrambled_definitions=scrambled_definitions) 
    else:
        words = session.get("words", [])        
        definitions = [get_definition(word) for word in words]
        scrambled_definitions = session.get("scrambled_definitions", [])  # Retrieve scrambled definitions from session
        shuffled_definitions = scrambled_definitions.copy()
        shuffled_words = words.copy()
        random.shuffle(shuffled_definitions)
        random.shuffle(shuffled_words)
        def_word = np.array([shuffled_definitions, shuffled_words])
        def_words = np.array([words, definitions])
        print(def_words)
        print(def_word)
        return render_template("scrambleplay.html", scrambled_definitions=scrambled_definitions, words=words, user=current_user, enumerate=enumerate, shuffled_definitions=shuffled_definitions, shuffled_words=shuffled_words)

@pages.route('/flashcards_generator', methods=['GET', 'POST'] )
def flashcards_generator():
    if request.method == 'POST':
        words = request.json
        if request.is_json:
            print(words)
        session["words"] = words
        definitions = {}
        for i in words:
            definitions[i] = get_definition(i)
        extracted_definitions = definition_extract(definitions)

        return jsonify(extracted_definitions = extracted_definitions) 
    else:
        words = session.get("words", [])        
        definitions = [get_definition(word) for word in words]
        extracted_definitions = session.get("extracted_definitions", [])  # Retrieve extracted definitions from session
        return render_template("flashcards_generator.html", words=words, extracted_definitions=extracted_definitions ,user=current_user, enumerate=enumerate)

@pages.route('/flashcardswg' , methods=['GET', 'POST'])
def flashcardswg():
    if request.method == 'POST':
        words = request.form.getlist('word')
        definitions = [get_definition(word) for word in words]
        return render_template("flashcards_generator.html", user=current_user, definitions=definitions, words = words)
    return render_template("flashcardswg.html", user=current_user)