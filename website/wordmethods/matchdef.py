


def matchdef(def_word):
    return [[words, shuffled_definitions] for words, shuffled_definitions in def_word.items()]

def_word = {
    "lmea ahconrm fo a ajomr itteloarirr tnui": "king", "": "glass", "or siwgonh nmelta or lmrao tstrengh to caef rngdae arfe or ifytifclud haingv or hgoswin uoegarc erguoca": "brave",
     "oflhosi ro pdusit rponse": "idiot", "a pciycaat to vemo noe ot erthie ocmopaeisnsat nspmcoaotasei ro ouptecnsmtuo tiyp": "pathetic",
       "altbe frema or acse hwti a songilp or ohoirtnazl asercuf lcaiyeepls fro gtriniw dna eanrdgi nda oetfn htwi arsdwre terocstpmamn nad ihooegneslp": "desk"
       }

word_defs = matchdef(def_word)
def checkword(word, shuffled_words):
    for i in range(len(shuffled_words)):
        if shuffled_words[i] == word:
            return i
def checkdef(definition, shuffled_definitions):
    for i in range(len(shuffled_definitions)):
        if shuffled_definitions[i] == definition:
            return i
shuffled_words = ["king", "glass", "brave", "idiot", "pathetic", "desk"]
shuffled_definitions = ["lmea ahconrm fo a ajomr itteloarirr tnui", "or siwgonh nmelta or lmrao tstrengh to caef rngdae arfe or ifytifclud haingv or hgoswin uoegarc erguoca", "oflhosi ro pdusit rponse", "a pciycaat to vemo noe ot erthie ocmopaeisnsat nspmcoaotasei ro ouptecnsmtuo tiyp", "altbe frema or acse hwti a songilp or ohoirtnazl asercuf lcaiyeepls fro gtriniw dna eanrdgi nda oetfn htwi arsdwre terocstpmamn nad ihooegneslp"]
testword = checkword("pathetic",shuffled_words)
testdef = checkdef("or siwgonh nmelta or lmrao tstrengh to caef rngdae arfe or ifytifclud haingv or hgoswin uoegarc erguoca",shuffled_definitions)
def check_correct(string):
    if string == 
