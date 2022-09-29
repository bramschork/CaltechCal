'''
Author: Bram Schork
Date: September 2022

Version: 1.0.1

Version Notes: 
 - Currently setup for fall term 2022
 - Program allows for spaces in the days of the week
 - Program input only accepts CSV files as the input in the file dialogue menu
 - Added error messages
 
 ToDo:
  - Error out for inproperly formatted/headered input CSV file
  - Make file dialogue menu pop to top of other windows
'''

# FALL TERM 2022 DATES
start_date = '09-27-2022'
end_date = '12-02-2022'
days_off_raw = ['11-24-2022', '11-25-2022']

### IMPORTS ###
import pandas as pd
import datetime
import calendar
import tkinter as tk
from tkinter import filedialog
import os
import sys

# Set environment variable to silence TK
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Create and hide root window for TK. This is needed for the file dialog.
root = tk.Tk()
root.attributes("-topmost", True)
root.wm_attributes('-topmost', 1)
root.lift()
root.withdraw()

# Get class file from user
path = filedialog.askopenfilename(filetypes=(("CSV Files","*.csv"),))

while path == '':
    print('No file entered. Exiting.')
    sys.exit(-1)


# Turn date strings into datetime objects
start_date = datetime.datetime.strptime(start_date, '%m-%d-%Y')
end_date = datetime.datetime.strptime(end_date, '%m-%d-%Y')
days_off = []
for item in days_off_raw:
       days_off.append(datetime.datetime.strptime(item, '%m-%d-%Y'))

# Convert class file into Pandasa DataFrame
try:
    df = pd.read_excel(path)
except FileNotFoundError:
    print('Error reading file. Exiting.')
    sys.exit(-1)

# Create empty DataFrame for the output
outputDF = pd.DataFrame()

# DOW (Days of Week) dictionary
days_of_week = {
    'M': 'Monday',
    'T': 'Tuesday',
    'W': 'Wednesday',
    'TR': 'Thursday',
    'F': 'Friday'
}


# check_date - This is a var that I will iterate through to check every day of the term
check_date = start_date

# Iterate over every single class
course_names = []
descriptions = []
dates = []
start_time = []
end_time = []
locations = []

for index, row in df.iterrows():
    check_date = start_date
    # For each class, iterate through each date to add a calendar event for every class
    class_days = row['Class Days'].replace(' ', '')
    class_days = [days_of_week[item] for item in class_days.split(',')]
        
    while check_date <= end_date:
        # dow = Day of Week
        dow = (calendar.day_name[check_date.weekday()])
        
        if dow != 'Saturday' and dow != 'Sunday' and check_date not in days_off:
            
            # if the check date is a day I have class, create an event
            if dow in class_days:
                # Add event title
                course_names.append(row['Course Name'])
                
                # Add event description
                descriptions.append('Course Title: {0}\nSection/Instructor: {1}'.format(row['Course Title'], row['Section/Instructor']))

                # Add start date
                dates.append(check_date)
                
                # Add Start Time
                times = row['Class Time'].split('-')
                start_time.append(times[0])
                end_time.append(times[1])
                
                # Add Location
                locations.append(row['Class Location'])
                
        check_date += datetime.timedelta(days=1)
            
outputDF['Subject'] = course_names
outputDF['Description'] = descriptions
outputDF['Start Date'] = dates
outputDF['Start  Time'] = start_time
outputDF['End Time'] = end_time
outputDF['Location'] = locations
outputDF.to_csv('CaltechCalOutput.csv')
print('Output File Generated')