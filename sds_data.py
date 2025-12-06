# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: Hongwu Cao
# Student ID : 1173484
# =============================================================


# * * * * * * * * * ======= WARNING ======= * * * * * * * * * * *
# * * * Do not add any functions or variables to this file. * * *
# * * *                                                     * * *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

from datetime import date,datetime,timedelta


classes = {
    "Glowworms": [816, 786],
    "Fireflies": [121],
    "Butterflies": [343, 810],
    "Piwakawaka": [],
    "Robins": [801],
    "Bellbirds": [],        # New class
    "Senior Dance": []      # New class
}


# [id, first_name, family_name, birthdate, grade, email address]
students = [ 
	[816, 'Simon', 'Charles', date(2021,7,15),0, 'simon@charles.nz'],
	[343, 'Charlie', 'Charles', date(2018,1,25),2, 'charlie@charles.nz'],
	[810, 'Kate', 'McArthur', date(2018,9,30),2, 'K_McArthur94@gmail.com'],
	[786, 'Jack', 'Hopere', date(2022,2,10),0, 'Jack643@gmail.com'],
	[801, 'Chloe', 'Mathewson', date(2015,3,15),4, 'Chloe572@gmail.com'],
	[121, 'Kate', 'McLeod', date(2019,7,15),1, 'KMcLeod112@gmail.com'],
    # New students
    [817, "Emma", "Wilson", date(2020, 3, 15), 0, "emma@wilson.nz"],
    [818, "Oliver", "Brown", date(2018, 6, 20), 1, "oliver@brown.nz"],
    [819, "Sophia", "Taylor", date(2017, 9, 10), 2, "sophia@taylor.nz"],
    [820, "Lucas", "Anderson", date(2016, 4, 5), 3, "lucas@anderson.nz"],
    [821, "Isabella", "Thomas", date(2015, 11, 25), 4, "isabella@thomas.nz"],
    [822, "Mason", "Jackson", date(2013, 2, 14), 5, "mason@jackson.nz"],
    [823, "Ava", "White", date(2011, 8, 30), 6, "ava@white.nz"],
    [824, "Liam", "Harris", date(2019, 5, 12), 0, "liam@harris.nz"],
    [825, "Mia", "Martin", date(2017, 3, 8), 0, "mia@martin.nz"],
    [826, "Noah", "Garcia", date(2016, 1, 20), 0, "noah@garcia.nz"],
    [827, "Charlotte", "Martinez", date(2014, 7, 5), 0, "charlotte@m.nz"],
    [828, "James", "Rodriguez", date(2012, 9, 18), 0, "james@rodriguez.nz"],
    [829, "Amelia", "Lee", date(2010, 12, 1), 7, "amelia@lee.nz"]

]


def unique_id():
    """
    This will return the next available ID as a new integer value
    that is one higher than the current maximum ID number in the list."""
    
    return max(list(zip(*students))[0]) + 1


def display_formatted_row(row, format_str):
    """
    row is a list or tuple containing the items in a single row.
    format_str uses the following format, with one set of curly braces {} for each column:
       eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
       <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
        format_str = "{: <5}  {: ^10}  {: >15}"
    Make sure the column is wider than the heading text and the widest entry in that column,
        otherwise the columns won't align correctly.
    You can also pad with something other than a space and put characters between the columns, 
        eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
           format_str = "{:.<5} | {:.^10} | {:.>15}"
    """
    # Convert a tuple to a list, to allow updating of values
    if type(row) == tuple: 
        row = list(row)
    # Loop through each item in the row, changing to "" (empty string) if value is None and converting all other values to string
    #   (Extra info:  enumerate() places a loop counter value in index to allow updating of the correct item in row)
    for index,item in enumerate(row):
        if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
            row[index] = ""       
        else:    
            row[index] = str(item)
    # Apply the formatting in format_str to all items in row
    print(format_str.format(*row))
