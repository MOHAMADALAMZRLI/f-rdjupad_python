### f-rdjupad_python
## Data Processing Pipeline
  * Automates reading data from a CSV file, filtering by year, and saving it to an SQLite database. The script can be scheduled to run daily.


## Files
   * main.py: Runs the data pipeline (read, filter, save) and supports scheduling.
   * read.py: Reads data from a CSV file.
   * filter.py: Filters data for a specific year.
   * save.py: Saves filtered data to an SQLite database.


 ## Installation
   * Install dependencies:
   -  pip install pandas sqlite3 schedule

 ## Usage
   * Modify file paths and database location in main.py, then run:
     - python main.py
## Logging
   * All activities are logged in data_update.log.

## License
   * MIT License
