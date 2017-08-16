This python package extracts prevalent trends from a list of short phrases

Operation:
    Read a column as an array of strings from a .csv file
	User Option - convert a wordseries to a moniker?
    Give them their pos-tag via the PENN treebank
    Convert to WORDNET POS-tags and keep only: ADJ / VERB / NOUN / ADV
        User Option - to save this POS array back to the .csv file
    Enumerate most_common words
    Weight each string in the array according to the most-common words it contains
        User Option - to save this weight-array back to the .csv file
