import pandas as pd



def infer_and_convert_data_types(df):
    for col in df.columns:
        # Numeric conversion
        df[col] = pd.to_numeric(df[col], errors='coerce')
        if df[col].notna().any():  # If any value was converted
            continue

        # Date conversion
        df[col] = pd.to_datetime(df[col], errors='coerce')
        if df[col].notna().any():
            continue

        # Categorical conversion
        if df[col].nunique() / len(df) < 0.5:  # Threshold for categorical conversion
            df[col] = pd.Categorical(df[col])
    
    return df

def read_and_convert(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file, chunksize=10000)  # Adjust chunksize based on memory constraints
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file, chunksize=10000)  # Adjust chunksize
    
    # Process in chunks for large files
    if isinstance(df, pd.io.parsers.TextFileReader) or isinstance(df, pd.io.excel.ExcelFile):
        chunk_list = []
        for chunk in df:
            chunk_list.append(infer_and_convert_data_types(chunk))
        df = pd.concat(chunk_list)
    else:
        df = infer_and_convert_data_types(df)

    return df