### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Declare the class variable, with default value, for emails.

# Initialise the instance variables for emails.

# Create the method to change 'has_been_read' emails from False to True.

from typing import List


class Email():

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.

    inbox.append(Email('example1@example.com', 'Welcome to HyperionDev!',
                       'Some content of this email'))
    inbox.append(Email('example2@example.com', 'Great work on the bootcamp!',
                       'Some longer content of second email'))
    inbox.append(Email('example3@example.com', 'Your excellent marks!',
                       'Sample content. Kind Regards, Oskar'))
    print('\n\n✅ The inbox was successfully filled with sample emails.\n')


def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    email: Email
    print("""
=======================================================   
                    💌 Inbox 💌
=======================================================
  ID    |   Read   |    Subject
=======================================================""")
    for index, email in enumerate(inbox):
        if email.has_been_read == False:
            print(
                f"   {index}    |   {email.has_been_read}  |    {email.subject_line}")
        else:
            print(
                f"   {index}    |   {email.has_been_read}   |    {email.subject_line}")
    print("=======================================================")


def read_email(index):
    # Create a function which displays a selected email.
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    email: Email
    for i, email in enumerate(inbox):
        if i == index:
            print(f"""
================================================
From: {email.email_address}
Subject: {email.subject_line}
Content: {email.email_content} 
================================================           
            """)
            if email.has_been_read == False:
                print(f'👀 Email: "{email.subject_line}" has marked as read 👀.')
            email.mark_as_read()


# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    [1] Read an email 
    [2] View unread emails 
    [3] Quit application 

    Enter selection: '''))

    if user_choice == 1:
        # add logic here to read an email
        list_emails()
        id = int(input("\n Enter ID to read an email: "))
        read_email(id)

    elif user_choice == 2:
        # add logic here to view unread emails
        email: Email
        unread = []

        print("""
    =======================================================   
                      📬 Unread emails 📬
    =======================================================
        ID      |       Subject
    =======================================================""")
        for index, email in enumerate(inbox):
            if email.has_been_read == False:
                unread.append(email)
                print(f"        {index}       |       {email.subject_line}")
        if len(unread) == 0:
            print("\n       👏 Well done! You have no unread emails.\n")
        print("    =======================================================")
    elif user_choice == 3:
        # add logic here to quit appplication
        print("""
        ...............................................
        .                                             .
        .   😁 Have a good day, and see you soon !    .
        .                                             .
        ...............................................
        """)
        exit()

    else:
        print("Oops - incorrect input.")
