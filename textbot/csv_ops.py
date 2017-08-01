#!python3
# a series of functions to read/load/save arrays to column in a csv file
encoding = "ISO-8859-1"
csvfile = ""

# open filedialog for user to select a file - return loaded filename for use in other functions
# in IDLE set; variable_filename 'csvfile' = read_csv()
def read_csv():
    global csvfile
    global encoding
    from tkinter.filedialog import askopenfilename
    csvfile = askopenfilename()
    # print the columns in the csvfile
    import pandas as pd
    df = pd.read_csv(csvfile, encoding = encoding)
    col_index = 0
    '''
    for column in df:
        print("Col:" + str(col_index+1) + " " + column)
        col_index = col_index+1
    print("There are " + str(col_index) + " columns in this csv file.")
    print(csvfile)
    '''
    return csvfile

def read_csv_load_col():
    #load a csv file
    global csvfile
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
    # load a column's data as a string array
    from tkinter.simpledialog import askstring
    col_name = askstring("PromptWindow", "Enter name of the col to load from")
    import_data = []
    import pandas as pd
    df = pd.read_csv(csvfile)
    for column in df:
        if column == col_name:
            print("Array loaded from column: " + col_name)
            import_data = df[col_name].tolist()
        '''
        print('///' + '\n' + 'Printing the data in col: '+ col_name + '\n' + '///')
        for line in import_data:
            print (line)
        '''
    return csvfile, import_data

# refs the filename selected in read_csv()
# opens a fieldialog asking user for name of column to load from,
# load the columns rows to a list (whose name the user supplies)
# in IDLE set; variable_array = load_col()
def load_col_ByNum():
    global csvfile
    global encoding
    print(csvfile)
    import pandas as pd
    df = pd.read_csv(csvfile, encoding = encoding)
    col_index = 0
    for column in df:
        print("Col:" + str(col_index+1) + " " + column)
        col_index = col_index+1
    #print("There are " + str(col_index) + " columns in this csv file.")
    from tkinter.simpledialog import askstring
    col_num = askstring("PromptWindow", "Enter number of the column to load from")
    print("col_num: " + col_num + " to be loaded.")
    col_num_int = int(col_num)
    df = pd.read_csv(csvfile, encoding = encoding)
    import_data = []
    col_index = 0
    for column in df:
        #print("Col:" + str(col_index+1) + " " + column)
        col_index = col_index+1
        if col_index == col_num_int:
            print("Loaded array Num: " + col_num + " Named: " + column)
            import_data = df[column].tolist()
    return(import_data)

# refs the filename selected in read_csv()
# opens a fieldialog asking user for name of column to load from,
# load the columns rows to a list (whose name the user supplies)
# in IDLE set; variable_array = load_col()
def load_col_ByName():
    global csvfile
    global encoding
    print(csvfile)
    from tkinter.simpledialog import askstring
    col_name = askstring("PromptWindow", "Enter name of the col to load from")
    import_data = []
    import pandas as pd
    df = pd.read_csv(csvfile, encoding = encoding)
    col_index = 0
    for column in df:
        if column == col_name:
            print("Array loaded from column: " + col_name)
            import_data = df[col_name].tolist()
        '''
        print('///' + '\n' + 'Printing the data in col: '+ col_name + '\n' + '///')
        for line in import_data:
            print (line)
        '''
    return(import_data)

# ask user for name of new column to save dataInList to
def save_col_2_csv(column_title, dataArray):
    global csvfile
    global encoding
    print(csvfile)
    import_data = []
    import pandas as pd
    df = pd.read_csv(csvfile, encoding = encoding)
    col_index = 0
    for column in df:
        col_index = col_index+1
    print("There are " + str(col_index) + " columns in this csv file - new data would be saved to col - " + str(col_index+1))
    #
    '''from tkinter.simpledialog import askstring
    new_col_name = askstring("PromptWindow", "Enter the name for the new col to save data to")
    '''
    #
    df.insert(col_index, column_title, dataArray)
    df.to_csv(csvfile, index=False)
