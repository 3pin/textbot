This python package prevalent trends from a large list of short statements.

Operation:
    Read a column as an array of strings from a csv file,
    Give them their pos-tag via the PENN treebank
    Convert to wordnet POS-tags and keep only: ADJ / VERB / NOUN / ADV
        Option for user to save this POS array back to the csv file
    Enumerate most_common words
    Weight each string in the array according to the most-common words it contains
        Option for user to save this weight-array back to the csv file
