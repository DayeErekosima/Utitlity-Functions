import pandas as pd

def explore_data(file_path):
    ''' This function takes in the file path as input and automatically displays the basic EDA of the csv data inputed'''


    data = pd.read_csv(file_path, sep=r'[,-]')  # regular expression handles both ',' and '-' seperators
    
    value = {
        "head": data.head(),
        "shape": data.shape,
        "describe": data.describe(),
        "missing_values": data.isna().sum()
    }
    
    print("Data Info:")
    data.info()  # Prints dataset info since it cannot be stored
    
    return value