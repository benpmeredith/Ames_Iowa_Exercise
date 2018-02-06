'''
This subroutine takes any DataFrame, variabled as 'df', and runs a BASIC level EDA.
'''
def eda(df):
    display("df Head: ", df.head())
    display('df shape: ', df.shape)
    display('df keys: ', df.keys())
    display('df describe: ', df.describe())
    print(df.info())
    display(df.dtypes)
    display(df.count())
    
    keys = df.keys()
    num_columns = []
    cat_columns = []
    for key in keys:
        if df[key].dtypes == 'int64':
            num_columns.append(key)
        elif df[key].dtypes == 'float64':
            num_columns.append(key)
        else:
            cat_columns.append(key)
        
        
    print ("The numeric columns in this data set, or `num_columns`, are: ", '\n', num_columns, '\n',)
    print ("The categoric columns in this data set, or 'cat_columns` are: ", '\n', cat_columns, '\n',)
    

    print('\n',"End of Basic EDA")