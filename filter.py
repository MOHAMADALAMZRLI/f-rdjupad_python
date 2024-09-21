def extract_wanted_data(df, year):
    """
    Filtrerar data efter ett specifikt år.
    """
    extracted_rows = df[df['Year'] == year]  # Filtrera data för det givna året
    return extracted_rows
