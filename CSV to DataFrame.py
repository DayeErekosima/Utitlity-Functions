import os
import pandas as pd
import chardet

def detect_encoding(file_path):

    """Function to automatically detect the encoding of the file before reading into pandas

    Returns:
        Result: encoding type
    """

    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read(100000))  
    return result['encoding']



def csv_to_df(folder_path):

    """Function to iterate through a large number of csv's and save them to a data frame

    Returns:
        dataframe: A dictionary of Dataframes with the loaded csv's
    """
    dataframes = {}  

    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            df_name = file.replace('.csv', '_df')

            encoding = detect_encoding(file_path)  # Detect encoding dynamically
            df = pd.read_csv(file_path, encoding=encoding)

            dataframes[df_name] = df  
            
    return dataframes
