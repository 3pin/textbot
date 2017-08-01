# function to readin an Array of Strings, then POS-tag them
# specific strings can also be converged / MONIKERED / removed

# POS tag a list of strings, selectively tagging (ie. only for: nouns/verbs/adj)
# in idle; supply the data_In_array in the brackets
# in idle; set dat_out_array via new_dataArray = POStag(dat_in_array)
def PENN(dataArray):
    from nltk import pos_tag, word_tokenize
    lemmaList = []

    # converge/remove a specific word-set
    for i, row in enumerate(dataArray):
        row = row.lower()
        #print('old: '+ row)
        if "public service broadcasting" in row:
            new_row = row.replace("public service broadcasting", "psb")
            dataArray[i] = new_row

    for row in dataArray:
        #print(row)
        #stringAll = stringAll + row.lower() + ' '
        keys = word_tokenize(row.lower())
        #print(keys)
        keys_vals = pos_tag(word_tokenize(row.lower()))
        #print(keys_vals)
        stringFiltered = ""
        for word, tag in keys_vals:
            #if tag in ('NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS') :
            if tag in ('NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'RB', 'RBR', 'RBS') :
                #print(word, ' -> ', tag)
                '''
                if word.endswith('ing'):        # if it ends with 'ing' = VBG
                    word = word[:-3]            # convert VBG > VB
                if word.endswith('ies'):        # if it ends with 'ies' = NNS
                    word = word[:-3]+'y'        # convert NNS > NN
                if word.endswith('s'):          # if it ends with 's' && is 'verb-3rd-person' VBZ
                    if tag == 'VBZ':
                        if len(word) >2:
                            word = word[:-1]        # convert VBZ > VB
                '''
                stringFiltered = stringFiltered + word  + ' '       #create string from words with only filtered tags
        lemmaList.append(stringFiltered)
    return(lemmaList)

def WN(dataArray):

    # function to convert PENN-POS-TAGS to WN-POS-TAGS
    from nltk.corpus import wordnet
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return 's'

    # function to lemmatize (change to base-word) WN words
    from nltk.stem.wordnet import WordNetLemmatizer
    lmtzr = WordNetLemmatizer()
    lemmaList = []

    # converge/remove a specific word-set
    for i, row in enumerate(dataArray):
        row = row.lower()
        #print('old: '+ row)
        if "public service broadcasting" in row:
            new_row = row.replace("public service broadcasting", "psb")
            dataArray[i] = new_row

    # POS-tag each sentence
    from nltk import pos_tag, word_tokenize
    for row in dataArray:
        #keys = word_tokenize(row.lower())
        #print(keys)
        keys_vals = pos_tag(word_tokenize(row.lower()))
        stringFiltered = ""
        for word, tag in keys_vals:
            # convert PENN-tag to WN-tag
            wn_tag = get_wordnet_pos(tag)
            wn_tag_formatted = "'" + wn_tag + "'"
            # convert word to base LEMMA
            new_word = lmtzr.lemmatize(word, wn_tag)
            if wn_tag in ('a', 'n', 'v', 'r') :
                stringFiltered = stringFiltered + new_word  + ' '       #create string from words with only filtered tags
        stringFiltered = stringFiltered.rstrip()
        lemmaList.append(stringFiltered)

    return(lemmaList)
