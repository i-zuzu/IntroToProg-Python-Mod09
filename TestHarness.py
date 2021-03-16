# ---------------------------------------------------------- #
# Title: TestHarness
# Description: A main module for testing
# ChangeLog (Who,When,What):
# IZubova,3.11.2021,Created script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    # from DataClasses import Person  # Person class only!
    import DataClasses as DC
    import ProcessingClasses as PC
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Test Person class in DataClasses module
print('Test Person class in DataClasses module:\n')
objP1 = DC.Person("Bob", "Smith")
objP2 = DC.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test Employee class in DataClasses module
print('\nTest Employee class in DataClasses module:\n')
objE1 = DC.Employee(1, "Bob", "Smith")
objE2 = DC.Employee(2, "Sue", "Jones")
lstTable = [objE1, objE2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test ProcessingClasses module
print('\nTest ProcessingClasses module:\n')
PC.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstTable = PC.FileProcessor.read_data_from_file("EmployeeData.txt")
# lstTable.clear()
# for line in lstFileData:
#     lstTable.append(DC.Employee(line[0], line[1], line[2].strip()))
for row in lstTable:
    print(row.to_string(), type(row))


# Test IO classes
print("\nTest IOClasses module:\n")
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())