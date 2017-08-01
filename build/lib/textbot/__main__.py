# macro
# reads a csv, selects a column with comments, lemmatizes (saves them to csv), mostCommon count, cutoff-weighted / saves to csv

import csv_ops
# select / load the filename of the relevant csv file as 'csvfile'
csv_ops.read_csv()

# from the selected csv, load a specific column
comments = csv_ops.load_col_ByNum()

# lemmatize the array called comments
import pos_tag
lemmas = pos_tag.WN(comments)

# save lemmas array to csv column
from tkinter.simpledialog import askstring
YesNo = askstring("PromptWindow", "Would you like to write the 'LEMMAS' to the csvfile?")
if YesNo.lower() == 'yes' or YesNo.lower() == 'y':
    csv_ops.save_col_2_csv('lemmas', lemmas)
    print ("Saved 'LEMMAS' to csvfile")
else:
    print ("Did not save 'LEMMAS' to csvfile")

# count most common - prompt the user for the cutoff - calculated weightings for all counts above cutoff
import pos_count
column_title, counts = pos_count.mostCommon(lemmas)

# save counts to csv column
YesNo = askstring("PromptWindow", "Would you like to write the 'Weighted_Most_Common' to the csvfile?")
if YesNo.lower() == 'yes' or YesNo.lower() == 'y':
    csv_ops.save_col_2_csv(column_title, counts)
    print ("Saved 'Weighted_Most_Common' to csvfile")
else:
    print ("Did not save 'Weighted_Most_Common' to csvfile")
