# CaltechCal

**Caltech Students! Find a bug? Please submit an issue [here](https://github.com/bramschork/CaltechCal/issues)**. Feel free to make a pull request for new features. Also, please contact me at [bram@bramschork.com](mailto:bram@bramschork.com) for any questions or help!

1) Clone this repository to your computer.

2) Program setup. **Read through this step, it may not be required**. Set the key dates for the term. Change the three variables below to strings in the date format: MM-DD-YYYY

- start_date --> first day of classes
- end_date --> last day of classes
- days_off_raw --> Institute holidays when there are not classes

Note, I try to keep the Github up to date with the current acaddemic year.* **Program is current for the 2022-23 Academic Year**

3) Environment setup. This program has been tested on both MacOS and Windows. Use the latest version of Python and install the required modules using `pip3 install -r requirements.txt`. You should use a `venv`. To create a virtual environment, you can use `python3 -m venv venv`. To activate your `venv` (on Windows), navigate to the project directory and run `.\venv\Scripts\activate`.

4) Download classes. Go to Caltech REGIS [through Access](https://access.caltech.edu/). When on your course enrollment page for the term, print the page. This can be done through your browser's menu or through `CMD/CTRL + S`. Choose a convenient location on your computer and save the file. You want to download the webpage as HTML. This will download the page's HTML file as well as a folder contianing supporting files. We are only interested in the HTML file.

5) Run the program. A file dialog will appear. If you don't see it, check your taskbar. It may just be minimized. Select the HTML file you downloaded in Step 4. In the Python terminal you will have to select which term you are generating a calendar for. This alters the term start and end dates. The program will automatically run and finish. The program will otuput a file called `CaltechCalOutput.csv` **in the same folder as the code**(the folder is called `CaltechCal`). 

6) Import the calendar CSV file from the project directory. The program exports a CSV file called "CaltechCalOutput.csv". This CSV file contains the events to import into your Google Calendar. The instructions to import a CSV file into Google Calendar [can be found here](https://support.google.com/calendar/answer/37118?hl=en&co=GENIE.Platform%3DDesktop).

**I recommend creating a new calendar to import your classes. This way, if there is any issue with the program, you can simply delete the bad calendar, rather than having to sift through your main calendar. Instructions to create a new calendar [can be found here](https://support.google.com/calendar/answer/37095?hl=en)**.

7) You are done! I would recommend keeping the CaltechCal and it's dependencies installed on your computer for next term! The `CaltechCal` folder can be moved on your computer to a convenient location. The program overwrites the output file every time it is run. Feel free to delete the REGIS HTML file and supporting files folder your downloaded in Step 4.
