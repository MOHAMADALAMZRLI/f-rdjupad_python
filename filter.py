def extract_wanted_data(df, year):
    """
    Filtrerar data efter ett specifikt år.
    """
    extracted_rows = df[df['Year'] == year]  
    return extracted_rows
