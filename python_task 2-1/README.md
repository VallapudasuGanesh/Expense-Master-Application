Expense Master Application

Step 1: Importing Modules

import csv
import os
from datetime import datetime

We start by importing necessary modules.

--> csv: This module provides functionality to read and write CSV files.
--> os: This module provides a portable way to interact with the file system.
-->datetime: This module provides classes for manipulating dates and times.

Step 2: Loading Data

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            for entry in data:
                entry['Date'] = datetime.strptime(entry['Date'], '%Y-%m-%d').date()
            return data
    return []

This function load_data is used to load existing expense data from the CSV file.
It checks if the file exists, and if it does, it reads the data.
The csv.DictReader reads the file and interprets the first row as the header, creating a dictionary for each row.
The for loop converts the date strings to actual datetime.date objects for easier manipulation.

Step 3: Saving Data

This function save_data is used to save the data back to the CSV file after any changes.
It opens the file in write mode ('w') and uses csv.DictWriter to write the data back to the file.
It writes the header row and then writes the rest of the data.

Step 4: Adding an Expense

This function add_expense allows the user to input a new expense.
It takes the inputs for date, category, and amount and appends a new dictionary representing the expense to the data list.

Step 5: Generating a Report

This function generate_report calculates the total expenses for a specific month and year.
It iterates through the list of expenses and checks if the month and year match the input.
If a match is found, it adds the expense amount to the total.

Step 6: Main Function

he main function is where the program starts running.
It initializes the filename and loads existing data using load_data.
It then enters a loop to display the menu options and get user input.

Step 7: Running the Program

This conditional statement checks if the script is being run directly (not imported as a module).
If it is, it calls the main function, starting the execution of the program.


