# function to preprocess (filter out shortwords, emoticons etc) then count most common words
# you can specify additional words to ommit via the 'extra_words[]'

# in idle; supply the data_In_array in the brackets
def mostCommon(dataArray):
    import nltk
    from nltk.corpus import stopwords
    from nltk.corpus import swadesh
    from nltk import bigrams
    import re
    import json
    import operator
    from collections import Counter, OrderedDict
    import string
    from bs4 import UnicodeDammit
    #
    # additional words to omit
    extra_words = ['be', 'psb']
    #
    stringAll = ''
    emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""
    regex_str = [
        emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:[\uD83C-\uDBFF\uDC00-\uDFFF]+)',
        r'(?:\S)' # anything else
        ]
    tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
    emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
    #
    def tokenize(s):
        return tokens_re.findall(s)
    #
    def preprocess(s, lowercase=False):
        tokens = tokenize(s)
        if lowercase:
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens
    #
    for row in dataArray:
        for item in row:
            stringAll = stringAll + item
        stringAll = stringAll + " "
    #print('stringAll...' + '\n' + stringAll)
    #
    count_all = Counter()
    # count everything
    terms_all = [term for term in preprocess(stringAll) if len(term) > 1]
    #
    # Count terms only once, equivalent to Document Frequency
    terms_single = set(terms_all)
    #
    # build up the words to omit...
    punctuation = list(string.punctuation)
    common_words = swadesh.words('en')
    stop_words = stopwords.words('english')
    omitted_words = punctuation + common_words + stop_words + extra_words
    #
    # Create a list with all the terms EXCLUDING punctuations
    terms_nostop = [term for term in preprocess(stringAll) if term not in omitted_words and len(term) > 1]
    # Count hashtags only
    terms_hash = [term for term in preprocess(stringAll) if term.startswith('#') and len(term) > 1]
    # Count terms only (no hashtags, no mentions)...startswith() takes a tuple (not a list) if we pass a list of inputs
    terms_only = [term for term in preprocess(stringAll) if term not in stop_words and not term.startswith(('#', '@')) and len(term) > 1]
    # Count duples (co-occurances)
    terms_bigram = bigrams(terms_nostop)
    # Update the counter
    count_all.update(terms_nostop)
    # Print the most frequent words
    print(count_all.most_common(20))
    #
    sorted_dictionary = OrderedDict( sorted(count_all.items(), key=lambda t : t[1] , reverse=True) )
    #print(sorted_dictionary.keys())
    # sort by VAL in descending order
    #print( sorted(count_all.values()) )
    #count_all_sorted = sorted(count_all.items(), key=operator.itemgetter(1))
    #print(count_all_sorted)

    # ask user for number which Most_Common_Count must be above, then create new dict with Top_Counts
    from tkinter.simpledialog import askstring
    shortdict_tresh = askstring("PromptWindow", "Enter cutoff integer in POS most-common-count")
    shortdict_num = int(shortdict_tresh)
    shortdict = dict((key,value) for key, value in sorted_dictionary.items() if value > shortdict_num)
    print('shortdict... ')
    print(str(shortdict))
    dict_title = str(shortdict)
    #
    # take most-Common count and calcualte weighted score per string in lemma-dataArray...
    processList = []
    for row in dataArray:
        #print(row)
        count = 0
        ratingCounter = 0
        row = row.split()
        for word in row:
            #print(word)
            for key, value in shortdict.items():
                if word == key:
                    count = count +  value
        processList.append(count)
    #print('processList... ')
    #print(processList)
    return dict_title, processList;
