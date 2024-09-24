import sqlite3

def save_to_db(df, db_name, table_name):
    """
    Sparar data i en SQLite-databas.
    """
    connection = sqlite3.connect(db_name)  # Skapa en SQLite-anslutning
    df.to_sql(table_name, con=connection, if_exists="replace", index=False)  

    connection.commit()
    connection.close()
    print(f"Data has been successfully saved to the {table_name} table in {db_name}")

    
    
    
    
    """
    Sparar data i en SQLite-databas.
    
    Parametrar:
    - df: En pandas DataFrame med data att spara.
    - db_name: Sträng som representerar namnet eller sökvägen till databasen.
    - table_name: Sträng som representerar namnet på tabellen i databasen.
    
    Returnerar:
    - Inget returnvärde. Skriv ut meddelande vid framgång.
    """
