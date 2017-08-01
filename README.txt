This pthon package extracts general trends from a large list of short statements.
Operation:
    Read a column as an array of strings from csv file,
    Give them their pos-tag via the PENN treebank
    Convert to wordnet post-tags and keep only: ADJ / VERB / NOUN / ADV
        Option for user to save this lemmas-array back to csv file
    Enumerate most_common lemmas
    Weight each string in the array according to the most-common lemmas it contains
        Option for user to save this weight-array back to the csv file
