# Selwyn Dance School System - README

## Test Data

### Test Cases for Add New Student Function

| Test Case | First Name | Family Name | Birth Year | Birth Month | Birth Day | Email | Grade | Expected Result | Feature Tested |
|-----------|------------|-------------|------------|-------------|-----------|-------|-------|----------------|----------------|
| 1 | Emma | Wilson | 2020 | 3 | 15 | emma@wilson.nz | 0 | Successfully added to Glowworms | Glowworms class assignment (age 5 or under) |
| 2 | Oliver | Brown | 2018 | 6 | 20 | oliver@brown.nz | 1 | Successfully added to Fireflies | Fireflies class assignment (Grade 1) |
| 3 | Sophia | Taylor | 2017 | 9 | 10 | sophia@taylor.nz | 2 | Successfully added to Butterflies | Butterflies class assignment (Grade 2) |
| 4 | Lucas | Anderson | 2016 | 4 | 5 | lucas@anderson.nz | 3 | Successfully added to Piwakawaka | Piwakawaka class assignment (Grade 3) - FIXED BUG |
| 5 | Isabella | Thomas | 2015 | 11 | 25 | isabella@thomas.nz | 4 | Successfully added to Robins | Robins class assignment (Grade 4) |
| 6 | Mason | Jackson | 2013 | 2 | 14 | mason@jackson.nz | 5 | Successfully added to Bellbirds | Bellbirds class assignment (Grade 5) - NEW FEATURE |
| 7 | Ava | White | 2011 | 8 | 30 | ava@white.nz | 6 | Successfully added to Senior Dance | Senior Dance class assignment (Grade 6) - NEW FEATURE |
| 8 | Liam | Harris | 2019 | 5 | 12 | liam@harris.nz | 0 | Successfully added to Fireflies | Age-based assignment (6 years old, no grade) |
| 9 | Mia | Martin | 2017 | 3 | 8 | mia@martin.nz | 0 | Successfully added to Butterflies | Age-based assignment (7 years old, no grade) |
| 10 | Noah | Garcia | 2016 | 1 | 20 | noah@garcia.nz | 0 | Successfully added to Piwakawaka | Age-based assignment (8.5+ years old, no grade) - TESTS FIX |
| 11 | Charlotte | Martinez | 2014 | 7 | 5 | charlotte@m.nz | 0 | Successfully added to Robins | Age-based assignment (10+ years old, no grade) |
| 12 | James | Rodriguez | 2012 | 9 | 18 | james@rodriguez.nz | 0 | Successfully added to Bellbirds | Age-based assignment (12+ years old, no grade) - NEW FEATURE |
| 13 | Amelia | Lee | 2010 | 12 | 1 | amelia@lee.nz | 7 | Successfully added to Senior Dance | Senior Dance (Grade 7+) - NEW FEATURE |

### Invalid Input Test Cases

| Test Case | Input Field | Invalid Input | Expected Behavior | Feature Tested |
|-----------|-------------|---------------|-------------------|----------------|
| 14 | First Name | 123 | Error message, re-prompt | Name validation (numeric rejection) |
| 15 | First Name | (blank) | Error message, re-prompt | Name validation (empty rejection) |
| 16 | Email | invalid.email | Error message, re-prompt | Email validation (missing @) |
| 17 | Email | test@com | Error message, re-prompt | Email validation (invalid domain) |
| 18 | Birth Year | 1899 | Error message, re-prompt | Year validation (too old) |
| 19 | Birth Year | 2030 | Error message, re-prompt | Year validation (future year) |
| 20 | Birth Year | abc | Error message, re-prompt | Year validation (non-numeric) |
| 21 | Birth Month | 0 | Error message, re-prompt | Month validation (too low) |
| 22 | Birth Month | 13 | Error message, re-prompt | Month validation (too high) |
| 23 | Birth Day | 0 | Error message, re-prompt | Day validation (too low) |
| 24 | Birth Day | 32 | Error message, re-prompt | Day validation (too high) |
| 25 | Birth Day (Feb) | 30 | Error message, re-prompt | Day validation (invalid for month) |
| 26 | Birth Day (Feb leap) | 29 in 2023 | Error message, re-prompt | Day validation (non-leap year) |
| 27 | Grade | -1 | Error message, re-prompt | Grade validation (too low) |
| 28 | Grade | 7 | Error message, re-prompt | Grade validation (too high) |
| 29 | Grade | xyz | Error message, re-prompt | Grade validation (non-numeric) |
| 30 | Birth Date | 2025-12-25 | Error message, reject | Future date validation |

### Menu Function Test Cases

| Test Case | Menu Option | Expected Result | Feature Tested |
|-----------|-------------|-----------------|----------------|
| 31 | 1 | Display all students with formatted columns | List all students function |
| 32 | 2 | Display students grouped by class, sorted by family name | List students and classes - NEW REPORT |
| 33 | 3 | Display all students with their current ages | List students and ages - NEW REPORT |
| 34 | 4 | "Not implemented" message | Menu option 4 placeholder |
| 35 | 5 | "Not implemented" message | Menu option 5 placeholder |
| 36 | 6 | Prompt for new student information | Add new student function |
| 37 | X | Exit program with thank you message | Exit functionality |
| 38 | x | Exit program with thank you message | Exit functionality (lowercase) |
| 39 | 9 | Invalid response error message | Invalid menu input handling |
| 40 | abc | Invalid response error message | Invalid menu input handling (text) |

### Additional Edge Cases

| Test Case | Scenario | Test Data | Expected Result | Feature Tested |
|-----------|----------|-----------|-----------------|----------------|
| 41 | Student exactly 8.5 years old | Birth: 2016-06-04, Today: 2024-12-04 | Added to Piwakawaka | Piwakawaka age boundary (8.5 years) - BUG FIX |
| 42 | Student just under 8.5 years | Birth: 2016-06-05, Today: 2024-12-04 | Added to Butterflies | Age calculation precision |
| 43 | Leap year birthday | Birth: 2020-02-29 | Valid date accepted | Leap year handling |
| 44 | Class with no students | View Piwakawaka initially | "No students currently enrolled" | Empty class display |
| 45 | Name with hyphen | First Name: Mary-Jane | Accepted | Name validation (hyphen allowed) |
| 46 | Name with space | Family Name: Van Der Berg | Accepted | Name validation (spaces allowed) |
| 47 | Student moving from Grade 5 to 6 | Change grade from 5 to 6 | Would move to Senior Dance | Grade-based class priority |

## Reflection

### Most Difficult Aspect

The most difficult aspect of this assessment was correctly implementing the age-based class assignment logic, particularly for the **Piwakawaka class which requires students to be at least 8.5 years old**.

#### Key Challenges:

1. **Decimal Age Calculation**: The original code used a simple integer age calculation (`calculate_age()`), which only returned whole years. This caused the bug where students who should be in Piwakawaka (8.5+ years) were incorrectly assigned to Butterflies (7+ years). I had to create a separate `calculate_age_with_months()` function that returns age as a decimal (e.g., 8.5 years) to properly handle the half-year requirement.

2. **Logic Flow in Class Assignment**: The original `add_student_to_classes()` function had flawed conditional logic with incorrect age comparisons (using `<=` instead of `>=`) and didn't properly prioritize grade over age. I had to restructure the entire function using `if-elif-else` statements in the correct order, checking from highest to lowest class level, ensuring grade-based assignment takes precedence over age-based assignment.

3. **Validation Complexity**: Implementing comprehensive input validation was challenging because it required:
   - Creating separate validation functions for each input type
   - Handling edge cases like leap years for date validation
   - Ensuring the validation functions would loop until valid input was received
   - Providing clear, helpful error messages that guide users to correct their input
   - Validating that dates aren't in the future

4. **Testing Edge Cases**: Ensuring the system correctly handled boundary conditions (e.g., a student exactly 8.5 years old, leap year birthdays) required careful testing and adjustment of the conditional logic.
