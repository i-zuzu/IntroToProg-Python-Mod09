# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# IZubova,3.11.2021,Finished the script
# ------------------------------------------------------------------------ #

# Data  ---------------------------------------------------- #

lstTable = []
strChoice = ''

# Data  ---------------------------------------------------- #


import DataClasses as DC
from ProcessingClasses import FileProcessor as PC
from IOClasses import EmployeeIO as Eio
from sys import exit

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts

lstTable = PC.read_data_from_file('EmployeeData.txt')

if lstTable is None:
    print('Error reading file EmployeeData.txt!')
    exit(1)

# print(lstTable)

# Show user a menu of options
while True:
    Eio.print_menu_items()

    # Get user's menu option choice
    strChoice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice =='1':
        # print(lstTable)
        Eio.print_current_list_items(lstTable)

    # Let user add data to the list of employee objects
    elif strChoice =='2':
        new_employee = Eio.input_employee_data()
        lstTable.append(new_employee)

    # let user save current data to file
    elif strChoice =='3':
        PC.save_data_to_file('EmployeeData.txt', lstTable)

    # Let user exit program
    elif strChoice =='4':
        print('Good bye')

    else:
        print(strChoice + ' is not in the Menu of Options')

# Main Body of Script  ---------------------------------------------------- #
