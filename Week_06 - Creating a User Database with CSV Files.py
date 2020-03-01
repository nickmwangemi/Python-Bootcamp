# Creating a User Database with CSV Files
# import all necessary packages
import csv
from IPython.display import clear_output
# handle user registration and writing to csv


def registerUser():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info:")
        email = input("E-mail: ")
        password = input("Password: ")
        password2 = input("Re-type password: ")
        clear_output()
        if password == password2:
            writer.writerow([email, password])
            print("You're now registered!")
        else:
            print("Something went wrong. Try again.")

# Handling User Login
# ask for use info and return true to login or false if incorrect info


def loginUser():
    print("To login, please enter your info: ")
    print("+"*50)
    email = input("E-mail: ")
    password = input("Password: ")
    clear_output()
    with open("users.csv", mode="r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("You are now logged in!")
                print("+"*50)
                return True
    print("Something went wrong. Try again.")
    print("+"*50)
    return False

# adding changing of passwords functionality


def changePassword():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        email = input("Please enter your email: ")
        print("Please enter your new password:")
        password = input("Password: ")
        password2 = input("Confirm new password: ")
        clear_output()
        if password == password2:
            writer.writerow([email, password])
            print("Your password has been successfully changed!")
            print("+"*50)
        else:
            print("Something went wrong. Try again.")
            print("+"*50)


# Creating the Main Loop - handles system menu and what to show based on the user being logged in or not
# variables for main loop
active = True
logged_in = False
# main loop
while active:
    if logged_in:
        print("1. Logout\n2. Quit\n3. Change Password")
    else:
        print("1. Login\n2. Register\n3. Quit")
    choice = input("What would you like to do? ").lower()
    clear_output()
    print("+"*50)
    if choice == "register" and logged_in == False:
        registerUser()

    elif choice == "login" and logged_in == False:
        logged_in = loginUser()

    elif choice == "quit":
        active = False
        print("Thanks for using our software!")
        print("+"*50)

    elif choice == "logout" and logged_in == True:
        logged_in = False
        print("You're now logged out.")
        print("+"*50)

    elif choice == "change password" and logged_in == True:
        logged_in = changePassword()

    else:
        print("Sorry, please try again!")
        print("+"*50)
