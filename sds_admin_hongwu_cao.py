# ============== SELWYN DANCE SCHOOL SYSTEM ==============
# Student Name: Hongwu Cao
# Student ID : 1173484
# ================================================================

from datetime import datetime, timedelta, date

# Make the variables and function in sds_data.py available in this code (without needing 'sds_data.' prefix)
from sds_data import students, classes, unique_id, display_formatted_row


def calculate_age(birth_date, current_date=None):
    """
    Calculates the age in years based on the birth date and current date.
    If current_date is not provided, uses today's date.
    Returns the age as an integer.
    """
    if current_date is None:
        current_date = date.today()

    age = current_date.year - birth_date.year

    # Adjust if birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


def calculate_age_with_months(birth_date, current_date=None):
    """
    Calculates the age in years and months (as a decimal).
    Used for determining class placement for students who need age checks
    that include half-year increments (e.g., 8.5 years old).
    Returns age as a float.
    """
    if current_date is None:
        current_date = date.today()

    years = current_date.year - birth_date.year
    months = current_date.month - birth_date.month
    days = current_date.day - birth_date.day

    # Adjust if birthday hasn't occurred yet this year
    if months < 0 or (months == 0 and days < 0):
        years -= 1
        months += 12

    # Adjust months if day hasn't occurred yet this month
    if days < 0:
        months -= 1

    # Return age as decimal (e.g., 8.5 years)
    return years + (months / 12.0)


def add_student_to_classes(student_id, grade, birthdate):
    """
    Assigns a student to the appropriate dance class based on their grade or age.
    Grade takes precedence over age for class assignment.
    Class assignments:
    - Senior Dance: Grade 6 or above
    - Bellbirds: Grade 5 or at least 12 years old
    - Robins: Grade 4 or at least 10 years old
    - Piwakawaka: Grade 3 or at least 8.5 years old
    - Butterflies: Grade 2 or at least 7 years old
    - Fireflies: Grade 1 or at least 6 years old
    - Glowworms: 5 years or under (others)
    """
    age = calculate_age_with_months(birthdate)

    # Check for Senior Dance first (Grade 6 or above, no age entry)
    if grade >= 6:
        classes["Senior Dance"].append(student_id)
    # Check for Bellbirds (Grade 5 or at least 12 years old)
    elif grade == 5 or age >= 12:
        classes["Bellbirds"].append(student_id)
    # Check for Robins (Grade 4 or at least 10 years old)
    elif grade == 4 or age >= 10:
        classes["Robins"].append(student_id)
    # Check for Piwakawaka (Grade 3 or at least 8.5 years old) - FIXED
    elif grade == 3 or age >= 8.5:
        classes["Piwakawaka"].append(student_id)
    # Check for Butterflies (Grade 2 or at least 7 years old)
    elif grade == 2 or age >= 7:
        classes["Butterflies"].append(student_id)
    # Check for Fireflies (Grade 1 or at least 6 years old)
    elif grade == 1 or age >= 6:
        classes["Fireflies"].append(student_id)
    # Default to Glowworms (5 years or under)
    else:
        classes["Glowworms"].append(student_id)


def list_all_students():
    """
    Lists all students with their details including ID, name, birth date, grade, and email.
    This is an example of how to produce basic output.
    """
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <6} {: <30}"
    display_formatted_row(
        ["ID", "First Name", "Family Name", "Birth Date", "Grade", "e-Mail"], format_str
    )

    for student in students:
        id = student[0]
        fname = student[1]
        famname = student[2]
        birthdate = student[3].strftime("%d %b %Y")
        grade = student[4]
        email = student[5]

        display_formatted_row([id, fname, famname, birthdate, grade, email], format_str)

    input("\nPress Enter to continue.")


def validate_name(prompt):
    """
    Validates that a name contains only alphabetic characters and is not empty.
    Continues prompting until valid input is received.
    Returns the validated name as a string.
    """
    while True:
        name = input(prompt).strip()
        if name and name.replace(" ", "").replace("-", "").isalpha():
            return name
        else:
            print(
                "*** Error: Name must contain only letters, spaces, or hyphens and cannot be empty."
            )


def validate_email(prompt):
    """
    Validates that an email address contains an @ symbol and a domain.
    Basic validation to ensure format is reasonable.
    Returns the validated email as a string.
    """
    while True:
        email = input(prompt).strip()
        if email and "@" in email and "." in email.split("@")[1]:
            return email
        else:
            print(
                "*** Error: Please enter a valid email address (e.g., name@example.com)."
            )


def validate_year(prompt):
    """
    Validates that a year is a 4-digit integer and is reasonable (between 1900 and current year + 1).
    Returns the validated year as an integer.
    """
    current_year = date.today().year
    while True:
        try:
            year = int(input(prompt))
            if 1900 <= year <= current_year + 1:
                return year
            else:
                print(f"*** Error: Year must be between 1900 and {current_year + 1}.")
        except ValueError:
            print("*** Error: Please enter a valid 4-digit year (e.g., 2020).")


def validate_month(prompt):
    """
    Validates that a month is an integer between 1 and 12.
    Returns the validated month as an integer.
    """
    while True:
        try:
            month = int(input(prompt))
            if 1 <= month <= 12:
                return month
            else:
                print("*** Error: Month must be between 1 and 12.")
        except ValueError:
            print("*** Error: Please enter a valid month number (1-12).")


def validate_day(prompt, year, month):
    """
    Validates that a day is valid for the given year and month.
    Handles different month lengths and leap years.
    Returns the validated day as an integer.
    """
    # Days in each month (index 0 is unused, indices 1-12 represent months)
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[2] = 29

    max_day = days_in_month[month]

    while True:
        try:
            day = int(input(prompt))
            if 1 <= day <= max_day:
                return day
            else:
                print(
                    f"*** Error: Day must be between 1 and {max_day} for the selected month."
                )
        except ValueError:
            print("*** Error: Please enter a valid day number.")


def validate_grade(prompt):
    """
    Validates that grade is an integer between 0 and 6.
    Grade 0 means no exam completed, grades 1-6 represent exam levels.
    Returns the validated grade as an integer.
    """
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 6:
                return grade
            else:
                print("*** Error: Grade must be between 0 and 6.")
        except ValueError:
            print("*** Error: Please enter a valid grade number (0-6).")


def add_new_student():
    """
    Adds a new student to the system by collecting and validating all required information.
    Validates: names, email format, birth date validity, and grade range.
    Automatically assigns the student to the appropriate class based on grade and age.
    Displays confirmation of successful addition.
    """
    print("\n=== Add New Student ===")

    # Collect and validate all student information
    fname = validate_name("Enter First Name: ")
    famname = validate_name("Enter Family Name: ")

    # Validate date components
    birthyear = validate_year("Enter Birth Year (YYYY): ")
    birthmonth = validate_month("Enter Birth Month (1-12): ")
    birthday = validate_day("Enter Birth Day (1-31): ", birthyear, birthmonth)

    # Create date object and validate it's not in the future
    try:
        birthdate = date(birthyear, birthmonth, birthday)
        if birthdate > date.today():
            print("*** Error: Birth date cannot be in the future.")
            input("\nPress Enter to continue.")
            return
    except ValueError:
        print("*** Error: Invalid date entered.")
        input("\nPress Enter to continue.")
        return

    email = validate_email("Enter e-Mail Address: ")
    grade = validate_grade("Enter Grade (0-6): ")

    # Generate new ID and add student
    new_id = unique_id()
    students.append([new_id, fname, famname, birthdate, grade, email])

    # Add student to appropriate class
    add_student_to_classes(new_id, grade, birthdate)

    # Confirmation message
    print(f"\n*** Student {fname} {famname} successfully added with ID {new_id}.")

    # Display which class they were assigned to
    for class_name, student_ids in classes.items():
        if new_id in student_ids:
            print(f"*** Assigned to class: {class_name}")
            break

    input("\nPress Enter to continue.")


def list_students_and_classes():
    """
    Displays which students are in which class.
    Output is grouped by class name, with students listed alphabetically by family name.
    Shows student ID, first name, and family name for each student in each class.
    """
    print("\n=== Students by Class ===\n")

    # Sort classes alphabetically for consistent display
    sorted_classes = sorted(classes.keys())

    for class_name in sorted_classes:
        print(f"\n{class_name}:")
        print("-" * 50)

        student_ids = classes[class_name]

        if not student_ids:
            print("  No students currently enrolled")
        else:
            # Get full student details for students in this class
            class_students = []
            for student in students:
                if student[0] in student_ids:
                    class_students.append(student)

            # Sort by family name, then first name
            class_students.sort(key=lambda x: (x[2], x[1]))

            # Display students
            format_str = "  {: <5} {: <15} {: <15}"
            display_formatted_row(["ID", "First Name", "Family Name"], format_str)

            for student in class_students:
                display_formatted_row([student[0], student[1], student[2]], format_str)

    input("\n\nPress Enter to continue.")


def list_students_and_ages():
    """
    Displays a report showing each student's name and their current age in years.
    Students are listed in order by family name, then first name.
    Age is calculated from birth date to today's date.
    """
    print("\n=== Dancers Ages ===\n")

    # Sort students by family name, then first name
    sorted_students = sorted(students, key=lambda x: (x[2], x[1]))

    format_str = "{: <15} {: <15} {: <5}"
    display_formatted_row(["First Name", "Family Name", "Age"], format_str)

    for student in sorted_students:
        fname = student[1]
        famname = student[2]
        birthdate = student[3]
        # Use calculate_age_with_months to get decimal age and format to 1 decimal place
        age = calculate_age_with_months(birthdate)
        age_formatted = f"{age:.1f}"

        display_formatted_row([fname, famname, age_formatted], format_str)

    input("\nPress Enter to continue.")


def disp_menu():
    """
    Displays the main menu options for the Selwyn Dance School System.
    Shows all available functions including reports and data entry options.
    """
    print("\n" + "=" * 50)
    print("==== WELCOME TO SELWYN DANCE SCHOOL SYSTEM ====")
    print("=" * 50)
    print(" 1 - List Students")
    print(" 2 - List Students and their Classes")
    print(" 3 - List Students and their Ages")
    print(" 4 - Not Implemented")
    print(" 5 - Not Implemented")
    print(" 6 - Add New Student")
    print(" X - eXit (stops the program)")
    print("=" * 50)


# ------------ This is the main program ------------------------

# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"

# Rebuild class assignments based on current student data
# This ensures all students are correctly assigned
for class_name in classes:
    classes[class_name] = []

for student in students:
    student_id = student[0]
    grade = student[4]
    birthdate = student[3]
    add_student_to_classes(student_id, grade, birthdate)

# Main menu loop
# Don't change the menu numbering or function names in this menu.
# Repeat this loop until the user enters an "X" or "x"
response = ""
while response.upper() != "X":
    disp_menu()
    response = input("\nPlease enter menu choice: ").strip()

    if response == "1":
        list_all_students()
    elif response == "2":
        list_students_and_classes()
    elif response == "3":
        list_students_and_ages()
    elif response == "4":
        print("\n*** This feature has not been implemented yet.")
        input("\nPress Enter to continue.")
    elif response == "5":
        print("\n*** This feature has not been implemented yet.")
        input("\nPress Enter to continue.")
    elif response == "6":
        add_new_student()
    elif response.upper() == "X":
        pass  # Exit loop
    else:
        print("\n*** Invalid response, please try again (enter 1-6 or X)")
        input("\nPress Enter to continue.")

print("\n" + "=" * 50)
print("=== Thank you for using the SELWYN DANCE SYSTEM! ===")
print("=" * 50 + "\n")
