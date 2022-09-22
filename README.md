# CaltechCal

1) Program setup. This program has been tested on both MacOS and Windows. Use the latest version of Python and install the required modules using 'pip3 install -r requirements.txt'. You should use a 'venv'.

2) Format your class file. Check the 'ExampleClasses.xlsx' file in the 'docs' folder for an example. Here is a brief summary:

Course Name | Course Title | Section/Instructor | Class Days | Class Time | Class Location
----------- | ------------ | ------------------ | ---------- | ---------- | --------------
Class A | Intro to Caltech | 07, President Rosenbaum | M,W,F | 11:55-13:15 |  Lecture Hall BAX
Class A Recitation | Intro to Caltech! | | T | 15:00-16:00 | B270 MRE
Class B | Intro to Math | 07, President Einstein | T,TR| 10:15-11:00 | 201 BRG

Note: Each calendar event descriotion contains the course title and section/instructor. This information is concatenated in the program.

The 'Class Days' should have no spaces. Ex. "TR, M" = BAD --> "TR,M" = Good
These abbbreviations are generated by REGIS. Here is the key for reference:

Abbreviation | Day of Week
------------ | -----------
M | Monday
T | Tuesday
W | Wednesday
TR | Thursday
F | Friday

3) Run the program. A file dialog will appear. If you don't see it, check your taskbar. It may just be minimized. Select the Excel file with your classes. The program will automatically run once the file is selected and output the calendar file.

4) Import the calendar CSV file. The program exports a CSV file called "CaltechCalOutput.csv". This CSV file contains the events to import into your Google Calendar. The instructions to import a CSV file into Google Calendar [can be found here](https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop).

**I recommend creating a new calendar to import the birthdays. This way, if there is any issue with the program, you can simply delete the bad calendar, rather than having to sift through your main calendar. Instructions to create a new calendar [can be found here](https://support.google.com/calendar/answer/37095?hl=en)**.
