import logging
from read import read_data
from filter import extract_wanted_data
from save import save_to_db
import schedule
import time

def main():
    """
    Huvudfunktionen för att läsa, filtrera och spara data.
    """
    # Ange filvägen för CSV-filen och databasen
    file_path = 'C:/Users/musta/OneDrive/Skrivbord/ds23_f-rdjupad_python-main/kunskapskontroll_2/superstore.csv'
    db_name = 'C:/Users/musta/OneDrive/Skrivbord/database.db'  # Exempel på korrekt sökväg
  # Ange rätt sökväg till databasen
    table_name = 'Traffic Accidents'

    # Läsa in data från CSV-filen
    df = read_data(file_path)
    logging.info("Data has been read successfully")

    # Filtrera data för ett specifikt år
    filtered_data = extract_wanted_data(df, 2013)
    logging.info("Data has been filtered for the year 2013")

    # Spara filtrerad data till databasen
    save_to_db(filtered_data, db_name, table_name)
    logging.info("Data has been saved to the database")

def job():
    """
    Schemalagd funktion att köra.
    """
    print("Starting the scheduled task...")
    main()

if __name__ == "__main__":
    # Konfigurera logging
    logging.basicConfig(filename='data_update.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Schemalägg jobbet att köras varje dag kl 12:00
    schedule.every().day.at("12:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
