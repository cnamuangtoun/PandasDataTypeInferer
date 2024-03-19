import pandas as pd



def infer_and_convert_data_types(df):
    for col in df.columns:
       # Attempt to convert to numeric first
        df_converted = pd.to_numeric(df[col], errors='coerce')
        if not df_converted.isna().all():  # If at least one value is numeric
            df[col] = df_converted
            continue

        # Attempt to convert to datetime
        try:
            df[col] = pd.to_datetime(df[col])
            continue
        except (ValueError, TypeError):
            pass
        
        if convert_to_bool(df, col):
            continue

        # Check if the column should be categorical
        if len(df[col].unique()) / len(df[col]) < 0.4:  # Example threshold for categorization
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

def convert_to_bool(df, col):
    unique_vals = df[col].dropna().unique()

    normalized_vals = {str(val).lower() for val in unique_vals}

    true_values = {'true', '1', 'yes'}
    false_values = {'false', '0', 'no'}
    binary_values = true_values.union(false_values)

    if len(normalized_vals) == 2:
        if normalized_vals <= binary_values:
            true_map = {val: True for val in true_values}
            false_map = {val: False for val in false_values}
            mapping = {**true_map, **false_map}
            df[col] = df[col].str.lower().map(mapping).astype('bool')
            return True

    return False
