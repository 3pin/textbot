#!python3
# a series of functions to read/load/save arrays to column in a csv file
encoding = "ISO-8859-1"
from textbot import csvfile

# open filedialog for user to select a file - return loaded filename for use in other functions
# in IDLE set; variable_filename 'csvfile' = read_csv()
def read_csv():
    from tkinter.filedialog import askopenfilename
    csvfile = askopenfilename()
    print(csvfile)
    # print csv-file's header-names to console
    import pandas as pd
    df = pd.read_csv(csvfile, encoding = encoding)
    col_index = 0
    for column in df:
        print("Col:" + str(col_index+1) + " " + column)
        col_index = col_index+1
    print("There are " + str(col_index) + " columns in this csv file - new data would be saved to col - " + str(col_index+1))
    return csvfile
