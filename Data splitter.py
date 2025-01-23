def create_sample_df(df, n_splits=5):
    """
    Splits a DataFrame into n_splits parts after shuffling the data.

    Parameters:
        df (pd.DataFrame): The input DataFrame to split.
        n_splits (int): The number of splits to create.

    Returns:
        list: A list of n_splits DataFrame parts.
    """
    try:
        import pandas as pd
        import numpy as np
    except ImportError as e:
        print("Error: Required libraries are not installed.")
        print(f"Missing library: {e.name}")
        print("Please install the missing library and try again.")
        return None

    # Shuffle the DataFrame and reset the index
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    
    # Split the DataFrame into n_splits parts
    df_parts = np.array_split(shuffled_df, n_splits)
    return df_parts