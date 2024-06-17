#!/usr/bin/python3

def show_homepage():
    """Function to display homepage menu"""
    print("     === DonateMe Homepage ===     ")
    print("------------------------------------")
    print("| 1. Login       | 2. Register      |")
    print("------------------------------------")
    print("| 3. Donate      | 4. Show Donations|")
    print("------------------------------------")
    print("|              5. Exit              |")
    print("------------------------------------")


def donate(username):
    """Function to accept donation amounts."""
    donation_amount = int(input("\nEnter amount to donate: "))
    donation_string = f"{username.title()} donated ${donation_amount}."
    print("\nThank you for donating!!\n")
    #  This now returns a tuple (donation_string, donation_amount)
    return donation_string, donation_amount


def show_donations(donations):
    """Function to display donations"""
    print("\n--- All Donations ---")
    amounts = []  # Empty list to hold donation_amount
    total_amt = 0
    user_entries = []  # Empty list to hold donation_string
    if not donations:  # Check if list is empty
        # if donations = "": should also check if list is empty
        print("There are no donations")
    else:
        # Trying to access Tuple that was created from return value above
        # Which is stored in the donations list specifically
        # trying to access the donation_string portion of the return value
        user_entries = [user_entry[0] for user_entry in donations]
        for user_entry in user_entries:
            print(user_entry)
        # attempting to use list comprehension, little confusing
        # Trying to access donation_amount, which is stored in donations list
        # and total them all up
        amounts = [amount[1] for amount in donations]
        for amount in amounts:
            total_amt += amount
        print(f"Total Amount Donated: ${total_amt}")







