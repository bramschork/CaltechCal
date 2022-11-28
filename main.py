'''
Author: Bram Schork
Date: November 2022

Version: 2.0.1
Academic Year: 2022-23

Version Notes: 
 - No longer need to generate CSV file, the program can parse the HTML file from Caltech Access.
 - Asks for correct term to select term start and ends dates.
 
 ToDo:
  - Make file dialogue menu pop to top of other windows
  - Check for null/nan values. Ex. for recitation
'''

# 2022-23 Academic Year Dates
start_dates = ['09-27-2022', '01-04-2023', '04-03-2023'] # beginning of instruction
end_dates = ['12-02-2022', '03-10-2023', '06-09-2023'] # last day of classes
days_off_raw = ['11-24-2022', '11-25-2022', '01-16-2023', '02-20-2023', '05-29-2023']

### IMPORTS ###
import pandas as pd
import datetime
import calendar
import tkinter as tk
from tkinter import filedialog
import os, sys

# Set environment variable to silence TK
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Create and hide root window for TK. This is needed for the file dialog.
root = tk.Tk()
root.attributes("-topmost", True)
root.wm_attributes('-topmost', 1)
root.lift()
root.withdraw()

# Get class file from user
path = filedialog.askopenfilename(filetypes=(("HTML Files","*.html"),))

# Error out if no file is given
while path == '':
    print('No file entered. Exiting.')
    sys.exit(-1)

# Get term from user for start and end dates
term = input('Select term:\nFall (0)\nWinter (1)\nSpring (2)\n------------\n')
valid_inputs = ['0', '1', '2']

while term not in valid_inputs:
    term = input('Select term:\nFall (0)\nWinter (1)\nSpring (2)\n------------\n')

term = int(term)

# Turn date strings into datetime objects
start_date = datetime.datetime.strptime(start_dates[term], '%m-%d-%Y')
end_date = datetime.datetime.strptime(end_dates[term], '%m-%d-%Y')

# Reformat days_off_raw
days_off = []
for item in days_off_raw:
    days_off.append(datetime.datetime.strptime(item, '%m-%d-%Y'))

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


def getDOW(vals):  
    '''
    getDOW takes in a takes of values and converts their abbreviations to their full names. Ex. TR --> Tuesday.
    It does this using the days_of_week dictionary.
    The function returns a list contians the full names in the same order as they came in.
    '''  
    i = 0
    DOW = []
    while i < len(vals):
        if vals[i] != 'T' and vals[i] != 'R':
            DOW.append(vals[i])
        else:
            if vals[i] == 'R':
                pass
            elif vals[i + 1] == 'R':
                DOW.append('TR')
            else:
                DOW.append('T')
        i += 1
    return DOW

# check_date is a var that I will iterate through to check every day of the term
check_date = start_date

# Create empty lists to store the class information for calendar import
course_names = []
descriptions = []
dates = []
start_time = []
end_time = []
locations = []

# Read the class HTML data as a Pandas object
table = pd.read_html(path)

# Reformat the Pandas dataframe from 1 list to a normal Pandas dataframe
df = table[0].dropna(axis=0, thresh=4)


for index, row in df.iterrows():
    
    # Start adding classes on the first day of the term
    check_date = start_date
    
    # Class days is a list containing the full DOW of days I have class
    class_days = []
    line = row['Days/Time'] #Ex. MTR 11:00-11:55 W 14:00-14:55
    line = line.split(' ')
    abbreviated_names = []
    class_times = []
    all_class_days = []
    
    i = 0
    while i < len(line):        
        # If not numeric, meaning it is a DOW (do this by checking first character)
        if not line[i][0].isnumeric():
            abbreviated_names.append([getDOW(line[i]), line[i + 1]])
        i += 1
        
    for item in abbreviated_names:
        for day in item[0]:
            all_class_days.append(days_of_week[day])
            class_days.append([days_of_week[day], item[1]])
    # make all class days final item of list
    class_days.append(all_class_days)

    while check_date <= end_date:
        # Get full DOW from check_date
        dow = (calendar.day_name[check_date.weekday()])
        
        if dow != 'Saturday' and dow != 'Sunday' and check_date not in days_off:
            
            # if the check date is a day I have class, create an event
            if dow in class_days[-1]:
                # Add event title
                course_names.append(row['Offering Name'])
                
                # Add event description
                section = row['Section/Instructor'][0:2]
                instructor = row['Section/Instructor'][3:]
                units = row['Units']
                descriptions.append('Section: {}\nInstructor: {}\nUnits: {}\n\nOffering Title & Class Info:\n{}\n'.format(section, instructor, units, row['Offering Title']))

                # Add start date
                dates.append(check_date)
                
                # Add Class Time
                for item in class_days[0:-1]:
                    if item[0] == dow:
                        times = item[1].split('-')
                start_time.append(times[0])
                end_time.append(times[1])
                
                # Add Location
                locations.append(row['Location'])
                
        check_date += datetime.timedelta(days=1)
            
outputDF['Subject'] = course_names
outputDF['Description'] = descriptions
outputDF['Start Date'] = dates
outputDF['Start  Time'] = start_time
outputDF['End Time'] = end_time
outputDF['Location'] = locations
outputDF.to_csv('CaltechCalOutput.csv', index=False)
print('Output File Generated')