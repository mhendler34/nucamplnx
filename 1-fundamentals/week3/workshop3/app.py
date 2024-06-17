#!/usr/bin/python3

from donations_pkg import homepage, user
# from donations_pkg.homepage import show_homepage
# from donations_pkg.user import login, register

database = {'admin': 'password123'}
donations = []
authorized_user = ""  # Empty strings equivalent to BOOLEAN FALSE
fail_user_dict = {}  # Attempt to capture failed login attempt

while True:
    homepage.show_homepage()  # Call function from homepage module
    if not authorized_user:  # Check if string is empty
        #  if authorized_user = ""  This should also check if list is empty
        print("You must be logged into donate")
    else:
        print(f"Logged in as: {authorized_user.title()}!\n")

    print("Please choose an option (1, 2, 3, 4 or 5)")
    response = input('> ')

    if response == '1':  # LOGIN
        username = input('Enter username: ').lower().strip()
        password = input('Enter password: ').lower().strip()
        #  = return val   module, function, (parameters)
        authorized_user = user.login(database, username, password)
    elif response == '2':  # REGISTER
        username = input('Enter username: ').lower().strip()
        password = input('Enter password: ').lower().strip()
        #   = ret val module, function(parameters)
        authorized_user = user.register(database, username, password)
        #  Added in 'is not None' for failed reg validation, returns none
        #  Without 'is not None' failed reg gets added to database dict
        if authorized_user not in database and authorized_user is not None:
            database[authorized_user] = password
        else:
            fail_user_dict[username] = password

    elif response == '3':  # DONATE
        if not authorized_user:  # Check is string is empty
            print("\nYou must be logged in to donate")
        else:
            donation_string = homepage.donate(authorized_user)
            # print(type(donation_string)
            # Returns 'tuple' when 2nd return value added
            donations.append(donation_string)
    elif response == '4':  # SHOW DONATIONS
        homepage.show_donations(donations)
    else:  # EXIT
        print("Goodbye")
        break
print(f"Database: {database}")
print(f"Donations: {donations}")
print(f"Failed username & password: {fail_user_dict}")
