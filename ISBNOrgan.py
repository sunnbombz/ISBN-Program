#program to convert 12 digit ISBN numbers to 13 digit

# LIBRARIES

import time

# ARRAYS/LISTS
ISBN_12 = ["978052556415", "978048626688"]

ignore_list = ["978014144174", "978014143947", "978034538475", "978014143984",
                 "978150289728", "978014144246", "978014312248", "978034900657", "978030774531", "978014144135",
                   "978014143955", "978076539753", "978125018692", "978125019178", "978125019185", "978125022986", 
                   "978125076537", "978125082697"]

ISBN_13 = []

# FUNCTIONS

def typewrite(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()  # moves to a new line when finished


def length_check(item):
    if len(item) == 12:
        message = f"ISBN Number is of valid length. Number/Book {item} is {len(item)} characters long."
        return True, message
    else:
        message = f"False Length. Not 12 digits. Number/Book {item} is {len(item)} characters long. It must be 12 numeric digits."
        return False, message
    
def data_type_check(item):
    if item.isdigit() == True:
        message = f"ISBN Number is of valid data type."
        return True, message
    else:
        message = f"False Data Type, it must be all numeric digits."
        return False, message

def prefix_check(isbn12_str):
    PREFIXES = ["978", "979"]
    prefix = isbn12_str[:3]

    if prefix not in PREFIXES:
        message = "The ISBN prefix is incorrect. It must be either 978, or 979."
        return False, message
    elif prefix in PREFIXES:
        message = "The ISBN prefix is correct."
        return True, message

verd_prefix, prefix_message = prefix_check(ISBN_12[0])
#typewrite(prefix_message)

# completes the 12 ISBN to make it a 13 ISBN 
def check_digits(isbn12_str):
    ISBN_13 = []
    total = 0

    for i in range(len(isbn12_str)):
        if i % 2 ==  0:
            total  += int(isbn12_str[i])
        else:
            total += (int(isbn12_str[i]) * 3)
        
    remainder = total % 10
    checkDigit = 10 - remainder

    if checkDigit == 10:
        checkDigit = 0

    full_13_number = f"{isbn12_str}-{checkDigit}"
    ISBN_13.append(full_13_number)

    message = f"Your full 13-digit ISBN number is {full_13_number}."
    return ISBN_13, message

number, num_message = check_digits(ISBN_12[0])
#typewrite(num_message)

# exit program
def r_u_sure():
    while True:
        print("Do you want to quit, or retry?")
        answer = input("Enter your answer (Y, for Quit/N, for retry): ").upper()
        if answer == "Y":
            print("Quitting program...")
            return "Y"
        elif answer == "N":
            print("OK, continue.")
            return "N"
        else:
            print("Invalid Answer. Please retry.")

# MAIN PROGRAM

qChoice = False
while qChoice == False:

    typewrite("\n\t-- MENU --\n" \
    "\tHello! Please choose an option below!\n" \
    "\t1. Find Check Digit for a 12 Digit ISBN.\n" \
    "\t2. Quit.")
    choice = input("Enter Choice here: ")

    if choice == "1":
        typewrite("Option 1 - Find Check Digit from 12Digit ISBN - has been chosen.")
        input_ISBN_12 = input("Please enter a 12 Digit ISBN.")

        verd_leng, leng_message = length_check(input_ISBN_12) # LENGTH CHECK
        if verd_leng:
            verd_data, data_message = data_type_check(input_ISBN_12) #DATA TYPE CHECK
            if verd_data:
                verd_prefix, prefix_message = prefix_check(input_ISBN_12) # PREFIX CHECK
                if verd_prefix:
                    
                    typewrite("Valid ISBN.")
                    number, num_message = check_digits(input_ISBN_12) # CHECK DIGITS
                    print(num_message) # Final 13 ISBN number list 

                    r_u_sure() # Exit Choice
                else:
                    print(prefix_message) # PREFIX : ERROR MESSAGE
                    r_u_sure() # Gives user exit choice
            else:
                print(data_message) # DATA TYPE : ERROR MESSAGE
                r_u_sure() # Exit Choice
        else:
            print(leng_message) # LENGTH : ERROR MESSAGE
            r_u_sure() # Exit Choice

    elif choice == "2":
        typewrite("Are you sure you want to Quit?")
        answer = input("Enter Y for Yes, N for No: ").upper()
        if answer == "Y":
            typewrite("Quitting program...")
            qChoice = True
        elif answer == "N":
            typewrite("Ok, continue.")
        else:
            typewrite("Invalid choice, please retry.")
    else:
        typewrite("Invalid Choice, please retry.")


        

