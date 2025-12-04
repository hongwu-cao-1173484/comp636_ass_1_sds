# ============== SELWYN DANCE SCHOOL SYSTEM ==============
# Student Name: 
# Student ID : 
# ================================================================
 
from datetime import datetime,timedelta,date     # datetime module is required for working with dates

# Make the variables and function in sds_data.py available in this code (without needing 'sds_data.' prefix)
from sds_data import students,classes,unique_id,display_formatted_row   

def calculate_age(birth_date, current_date=None):
    if current_date is None:
        current_date = date.today()
    
    age = current_date.year - birth_date.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def list_all_students():
    """
    Lists student details.
    This is an example of how to produce basic output."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <20}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","First Name","Family Name","Birth Date","Grade","e-Mail"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for student in students:
        id = student[0]
        fname = student[1]
        famname = student[2]
        birthdate = student[3].strftime("%d %b %Y")
        grade = student[4]
        email = student[5]

        display_formatted_row([id,fname,famname,birthdate, grade, email],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    input("\nPress Enter to continue.")


def add_student_to_classes(student_id, grade, birthdate):
      age = calculate_age(birthdate)
      if grade == 4:
            classes["Robins"].append(student_id)
      elif grade == 3:
                  classes["Piwakawaka"].append(student_id)
      elif grade == 2:
                  classes["Butterflies"].append(student_id)
      elif grade == 1:
                  classes["Fireflies"].append(student_id)
      else:
            if age <= 10:
                    classes["Robins"].append(student_id)
            elif age <= 8.5:
                    classes["Piwakawaka"].append(student_id)
            elif age <= 7:
                    classes["Butterflies"].append(student_id)
            elif age <= 6:
                    classes["Fireflies"].append(student_id)
            else:
                    classes["Glowworms"].append(student_id)
            
def add_new_student():
    fname = input("Enter First Name: ")
    famname = input("Enter Family Name: ")
    birthyear = int(input("Enter Birth Year (YYYY): "))
    birthmonth = int(input("Enter Birth Month (1-12): "))
    birthday = int(input("Enter Birth Day (1-31): "))
    email = input("Enter e-Mail Address: ")
    grade = int(input("Enter Grade (0-4): "))
    birthdate = date(birthyear, birthmonth, birthday)
    new_id = unique_id()
    students.append([new_id, fname, famname, birthdate, grade, email])
    add_student_to_classes(new_id, grade, birthdate)
    print(f"Student {fname} {famname} added with ID {new_id}.")

def list_students_and_classes():
    pass

def list_students_and_ages():
      pass

def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TO SELWYN DANCE SCHOOL SYSTEM ===")
    print(" 1 - List Students")
    print(" 2 - List Students and their Classes")
    print(" 3 - List Students and their Ages")
    print(" 4 - Not Implemented")
    print(" 5 - Not Implemented")
    print(" 6 - Add New Student")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"
response = ""
while response.upper() != "X":
    disp_menu()
    # Display menu for the first time, and ask for response
    response = input("Please enter menu choice: ")    
    if response == "1":
        list_all_students()
    elif response == "2":
        list_students_and_classes()
    elif response == "3":
        list_students_and_ages()
    elif response == "4":
        pass
    elif response == "5":
        pass
    elif response == "6":
        add_new_student()
    elif response.upper() != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)")

    print("")

print("\n=== Thank you for using the SELWYN DANCE SYSTEM! ===\n")

