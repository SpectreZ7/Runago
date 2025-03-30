
from flask import Blueprint,render_template,request
from flask_login import login_required, current_user
from .wordmethods.retreived_definition import get_definition
from flask import jsonify, session
from .wordmethods.scramblesentence import scramble_word
from .wordmethods.definitionsextract import definition_extract
import random
import numpy as np
import json
from .wordmethods.matchdef import checkdef, checkword, check_correct
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user,  login_required, logout_user, current_user
from .models import LearnedWord
import copy

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
    learned_words = LearnedWord.query.filter_by(user_id=current_user.id).all()
    Users = User.query.all()
    Users_id = current_user.id
    print(Users_id)
    return render_template("library.html", user = current_user, learned_words=learned_words, Users = Users, Users_id = Users_id)


@pages.route('/scrambleplay', methods=['GET', 'POST'])
def scrambleplay():
    if request.method == 'POST':
        words = request.json
        session["words"] = words  # Store words in session
        #When a POST request is received, the JSON data from the request is stored in the session using session["words"].
        definitions = {word: get_definition(word) for word in words}
        extracted_definitions = definition_extract(definitions, words)
        print(extracted_definitions)
        scrambled_definitions = [scramble_word(definition) for definition in extracted_definitions]
        print(scrambled_definitions)

        session["scrambled_definitions"] = scrambled_definitions  # Store scrambled definitions in session
        return  jsonify(scrambled_definitions=scrambled_definitions)
    else:
        words = session.get("words", [])  # Retrieve words from session
        #When a GET request is received, the words are retrieved from the session using session.get().
        definitions = [get_definition(word) for word in words]       
        scrambled_definitions = session.get("scrambled_definitions", [])
        print(definitions)
        print(scrambled_definitions)
        print(words)  
        shuffled_definitions = scrambled_definitions.copy()
        random.shuffle(shuffled_definitions)


        session["shuffled_definitions"] = shuffled_definitions
        session["definitions"] = definitions
        return render_template("scrambleplay.html", scrambled_definitions=scrambled_definitions, words=words, user=current_user, enumerate=enumerate, shuffled_definitions=shuffled_definitions)

@pages.route('/scrambleprocess', methods = ['POST'])
def scrambleprocess():
    words = session.get("words", [])
    definitions = session.get("definitions", [])
    shuffled_definitions = session.get("shuffled_definitions", [])
    scrambled_definitions = session.get("scrambled_definitions", [])
    data = request.json.get('data')
    word = data[0].strip()
    definition = data[1].strip()
    print(data)
    print(word, definition)
    print(words, shuffled_definitions)
    print(scrambled_definitions)
    clicked_word_index = checkword(word, words)
    clicked_def_index = checkdef(definition, scrambled_definitions)
    print(definitions)
    print(clicked_word_index, clicked_def_index)
    match = check_correct(clicked_word_index, clicked_def_index)
    print(match)
     # Check if the word's correct definition matches the selected definition
 

    return jsonify(match=match)
  

@pages.route('/crosswordg', methods=['GET', 'POST'])
def crosswordg():
     if request.method == 'POST':    
         words = request.form.getlist('word') # Retrieve the values of the form field 'word' as a list
         definitions = [definition_extract(get_definition(word)) for word in words]

         return render_template("crosswordgenerator.html", user=current_user, definitions=definitions, words = words)
     return render_template("crosswordg.html", user=current_user)

@pages.route('/crossword', methods=['GET', 'POST'])
def crossword():
    if request.method == 'POST':
        words = request.json # Retrieve the JSON data from the request body
        session["words"] = words
        definitions = {}
        for i in words:
            definitions[i] = get_definition(i)
        extracted_definitions = definition_extract(definitions, words)
        session["extracted_definitions"] = extracted_definitions
        #print(extracted_definitions)
        #print(words)
        return jsonify( extracted_definitions = extracted_definitions,words = words)
    else:
        words = session.get("words", [])        
        definitions = [get_definition(word) for word in words]
        extracted_definitions = session.get("extracted_definitions", [])  # Retrieve scrambled definitions from session
        return render_template("crossword.html", words=words, user=current_user, enumerate=enumerate, extracted_definitions=extracted_definitions)


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
        extracted_definitions = definition_extract(definitions, words)

        return jsonify(extracted_definitions = extracted_definitions) 
    else:
        words = session.get("words", [])        
        definitions = [get_definition(word) for word in words]
        extracted_definitions = session.get("extracted_definitions", [])  # Retrieve extracted definitions from session
        word_definitions = [{"word": word, "definition": get_definition(word)} for word in words]
        return render_template("flashcards_generator.html",word_definitions=word_definitions, words=words, extracted_definitions=extracted_definitions ,user=current_user, enumerate=enumerate)



@pages.route('/flashcardswg' , methods=['GET', 'POST'])
def flashcardswg():
    if request.method == 'POST':
        words = request.form.getlist('word')
        definitions = [get_definition(word) for word in words]
        return render_template("flashcards_generator.html", user=current_user, definitions=definitions, words = words)
    return render_template("flashcardswg.html", user=current_user)


@pages.route('/complete', methods =['GET', 'POST'])
@login_required
def complete():
    if request.method == "POST":
        words = session.get("words", [])
        definitions = [get_definition(word) for word in words]
        for(word, definitions) in zip(words, definitions):
            new_word = LearnedWord(user_id=current_user.id, word=word, definition=definitions)
            db.session.add(new_word)
            db.session.commit()

    return render_template("complete.html", user=current_user)