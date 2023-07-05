# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

USER_FILE = "user.txt"
TASKS_FILE = "tasks.txt"


def reg_user():
    '''Add a new user to the user.txt file'''

    # Read in user_data
    with open(USER_FILE, 'r') as user_file:
        user_data = user_file.read().split("\n")

    # - Request input of a new username
    while True:
        try:
            new_username = input("New Username: ").strip().lower()

            # Convert to a dictionary
            username_password = {}
            for user in user_data:
                username, password = user.split(';')
                username_password[username] = password

            # Check if username isn't already taken
            if new_username in username_password:
                raise ValueError(f"""
=========================================================================
    ❌ User with username {new_username} already exists. Choose another username.
=========================================================================
                """)
            else:
                break
        # Catch errors
        except ValueError as e:
            print(e)

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print(f"""
=========================================================================
    ✅ New user added: {new_username}
=========================================================================
""")
        username_password[new_username] = new_password

        with open(USER_FILE, "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise present a relevant message.
    else:
        print("""
=========================================================================
    ❌ Passwords do no match.
=========================================================================
                """)


def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and
        - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        raise ValueError("""
=========================================================================
    ❌ User does not exist. Please enter a valid username.
=========================================================================
                """)
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(
                task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open(TASKS_FILE, "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("""
=========================================================================
    ✅ Task successfully added.
=========================================================================
                """)


def view_all():
    '''Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def tasks_stats(user=None):
    '''Generates task statistics for all tasks or tasks specific to a user.

    The function reads tasks from a tasks file, calculates the number of completed,
    uncompleted, and overdue tasks, and returns a dictionary with the task statistics.

    Args:
        user (str, optional): The username for which to generate task statistics. If not provided,
                              statistics for all tasks will be generated. Default is None.

    Returns:
        dict: A dictionary containing the task statistics:
            - If user is not provided, the dictionary contains the following keys:
                - total_tasks_number (int): The total number of tasks.
                - complated_tasks_number (int): The number of completed tasks.
                - uncomplated_tasks_number (int): The number of uncompleted tasks.
                - overdue_tasks_number (int): The number of overdue tasks.
                - uncomplated_tasks_percentage (float): The percentage of uncompleted tasks.
                - overdue_tasks_percentage (float): The percentage of overdue tasks.
            - If user is provided, the dictionary contains the following keys:
                - user_total_tasks (int): The total number of tasks for the user.
                - user_complated_tasks (list): The list of completed tasks for the user.
                - user_complated_tasks_number (int): The number of completed tasks for the user.
                - user_uncomplated_tasks_number (int): The number of uncompleted tasks for the user.
                - user_overdue_tasks_number (int): The number of overdue tasks for the user.
    '''
    if user == None:
        total_tasks_number = 0
        complated_tasks = []
        complated_tasks_number = 0
        uncomplated_tasks_number = 0
        overdue_tasks_number = 0

        with open(TASKS_FILE, 'r') as tasks_file:
            for t in tasks_file.readlines():
                total_tasks_number += 1
                username, title, description, due_date, assigned_date, complated = t.strip().split(';')

                if complated == 'Yes':
                    complated_tasks_number += 1
                    complated_tasks.append(t)
                if complated == 'No':
                    uncomplated_tasks_number += 1
                    if datetime.strptime(due_date, '%Y-%m-%d').date() < datetime.now().date():
                        overdue_tasks_number += 1

        if uncomplated_tasks_number != 0 and total_tasks_number != 0:
            uncomplated_tasks_percentage = (
                uncomplated_tasks_number/total_tasks_number)*100
        else:
            uncomplated_tasks_percentage = 0
        if overdue_tasks_number != 0 and total_tasks_number != 0:
            overdue_tasks_percentage = (
                overdue_tasks_number/total_tasks_number)*100
        else:
            overdue_tasks_percentage = 0

        return {
            'total_tasks_number': total_tasks_number,
            'complated_tasks_number': complated_tasks_number,
            'uncomplated_tasks_number': uncomplated_tasks_number,
            'overdue_tasks_number': overdue_tasks_number,
            'uncomplated_tasks_percentage': uncomplated_tasks_percentage,
            'overdue_tasks_percentage': overdue_tasks_percentage
        }
    else:
        user_total_tasks = 0
        user_complated_tasks = []
        user_complated_tasks_number = 0
        user_uncomplated_tasks_number = 0
        user_overdue_tasks_number = 0

        with open(TASKS_FILE, 'r') as tasks_file:
            for t in tasks_file.readlines():
                username, title, description, due_date, assigned_date, complated = t.strip().split(';')
                if user == username:
                    user_total_tasks += 1
                    if complated == 'Yes':
                        user_complated_tasks.append(t)
                        user_complated_tasks_number += 1
                    if complated == 'No':
                        user_uncomplated_tasks_number += 1
                        if datetime.strptime(due_date, '%Y-%m-%d').date() < datetime.now().date():
                            user_overdue_tasks_number += 1
        return {
            'user_total_tasks': user_total_tasks,
            'user_complated_tasks': user_complated_tasks,
            'user_complated_tasks_number': user_complated_tasks_number,
            'user_uncomplated_tasks_number': user_uncomplated_tasks_number,
            'user_overdue_tasks_number': user_overdue_tasks_number
        }


def gen_task_report():
    '''
    Generates a task report summarizing the task statistics for all tasks.

    The function retrieves task statistics from the tasks_stats() function, formats the data into a
    report, and writes the report to a file named 'task_overview.txt'. It also prints a message
    indicating successful report generation.
    '''
    tasks_data = tasks_stats()

    report_content = (f"""
============================= Task Report =============================
    Total number of tasks: {tasks_data['total_tasks_number']}
    Number of complated tasks: {tasks_data['complated_tasks_number']}
    Number of uncomplated tasks: {tasks_data['uncomplated_tasks_number']}
    Overdue tasks: {tasks_data['overdue_tasks_number']}

    Incomplated tasks [percentage]: {round(tasks_data['uncomplated_tasks_percentage'])}%
    Overdue tasks [percentage]: {round(tasks_data['overdue_tasks_percentage'])}%
========================================================================
    """)

    with open('task_overview.txt', 'w') as task_report:
        task_report.write(report_content)
        print("\n✅ Task report created successfully")


def per_user_stats():
    '''
    Generates task statistics for each user in the 'user.txt'.

    The function reads user information from the 'user.txt', calculates task statistics for each user
    using the tasks_stats() function, and returns a formatted string containing the statistics for
    each user.

    Returns:
        str: A formatted string containing task statistics for each user, including the total number
             of tasks assigned to the user, percentage of tasks assigned to the user among all tasks,
             completed tasks percentage, tasks to complete, and failed tasks (overdue).
    '''
    users_data = ''
    with open(USER_FILE, 'r') as users_file:
        for u in users_file.readlines():
            username, password = u.strip().split(';')
            user_tasks = tasks_stats(username)
            all_tasks = tasks_stats().get('total_tasks_number')
            user_total_tasks = user_tasks['user_total_tasks']
            user_complated_tasks_number = user_tasks['user_complated_tasks_number']
            tasks_to_complate = user_total_tasks-user_complated_tasks_number
            if user_total_tasks != 0 and all_tasks != 0:
                user_tasks_percentage = (
                    user_total_tasks/all_tasks)*100
            else:
                user_tasks_percentage = 0
            if user_complated_tasks_number != 0 and user_total_tasks != 0:
                user_complated_tasks_percentage = (
                    user_complated_tasks_number/user_total_tasks)*100
            else:
                user_complated_tasks_percentage = 0

            user_stats = (f"""
    ======================== {username.upper()} ========================
    |
    |    Username: {username}
    |    User's tasks: {user_tasks['user_total_tasks']}
    |    Percentage of tasks assigned to the {username} among all tasks: {round(user_tasks_percentage)}%
    |    Completed user tasks [percentage]: {round(user_complated_tasks_percentage)}%
    |    Tasks to complete: {tasks_to_complate}
    |    Failed tasks [overdue]: {user_tasks['user_overdue_tasks_number']}
    |""")

            users_data += ''.join(user_stats)
    return users_data


def gen_user_report():
    '''
    Generates a user report summarizing task statistics for each user.

    The function retrieves per-user task statistics from the per_user_stats() function, formats the
    data into a report, and writes the report to a file named 'user_overview.txt'. It also prints a
    message indicating successful report generation.
    '''
    user_stats = per_user_stats()
    total_users = len(username_password.keys())
    total_tasks_number = tasks_stats().get('total_tasks_number')
    report = (f"""============================= Users report =============================
  
   Users in the system: {total_users}
   Tasks in the system: {total_tasks_number}
   
   Users individual reports:\n {user_stats} 
    =========================================================""")
    with open('user_overview.txt', 'w') as user_report:
        user_report.write(report)
        print("\n✅ Users report created successfully")


def gen_report():
    '''Generates task and user reports.

    The function calls gen_task_report() to generate a task report and gen_user_report() to generate
    a user report. Both reports are saved to separate files.
    '''
    gen_task_report()
    gen_user_report()


def view_main():
    '''
    Reads the tasks from the task.txt file and displays them to the console in a readable list.

    The function prints the tasks assigned to the current user in a visually appealing format, with
    details such as task title, assignee, date assigned, due date, and task description. Users can
    select a task by entering its task number or return to the main menu by entering '-1'. Once a
    task is selected, the user has the option to mark it as completed, edit the task, or go back to
    the main menu. User can edit only uncompleted tasks.
    '''

    print("""
* ============================== My Task List ============================== *""")

    full_task_list = []
    user_task_list = []
    for i, t in enumerate(task_list):
        full_task_list.append(t)
        if t['username'] == curr_user:
            user_task_list.append(t)
    if len(user_task_list) == 0:
        print(len(user_task_list))
        print("*   🔍 Nothing here yet")
    else:
        for i, t in enumerate(user_task_list):
            if t['username'] == curr_user:
                # user_task_list.append(t)
                print(f"""*
*    ============================= Task no {i} =============================
*     Task: \t\t {t['title']}
*     Assigned to: \t {t['username']}
*     Date assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}
*     Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}
*     Task Description:  {t['description']}
*    ==================================================================
*        """)
        print("""* ========================================================================== *
        """)

        selected_task = int(input(
            "Select a task by entering the task number or return to main menu by entering '-1': "))
        if selected_task == -1:
            print('main menu')

        elif selected_task in range(0, len(user_task_list)):
            edited_task_list = []
            if user_task_list[selected_task]['completed'] == True:
                print("""
This task is already completed and cannot be edited.
            """)
            else:
                task_action = input(f"""
Choose action: 
c - mark task '{user_task_list[selected_task]['title']}' as completed
e - edit task '{user_task_list[selected_task]['title']}'
x - go back to main menu
: """)

                if task_action == 'c':
                    for t in full_task_list:
                        user_task_list[selected_task]['completed'] = "Yes"
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(
                                DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        edited_task_list.append(";".join(str_attrs))

                        with open(TASKS_FILE, 'w') as task_file:
                            task_file.write("\n".join(edited_task_list))
                    print("\n✅ Task marked as completed. \n")
                elif task_action == 'e':
                    edit_action = input(f"""
Choose action: 
u - assign task to someone else (currently assigned to: '{user_task_list[selected_task]['username']}')
d - change due date (current due date: '{user_task_list[selected_task]['due_date'].strftime(DATETIME_STRING_FORMAT)}')
x - go back to main menu
: """)
                    if edit_action == 'u':
                        while True:
                            try:
                                username = input(
                                    "Enter the username of the user you wish to assign to this task: ").strip().lower()
                                if username not in username_password.keys():
                                    raise ValueError("""
=========================================================================
    ❌ User does not exist. Please enter a valid username.
=========================================================================
                """)
                            except ValueError as e:
                                print(e)
                            else:
                                break
                        for t in full_task_list:
                            if username:
                                user_task_list[selected_task]['username'] = username

                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(
                                    DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            edited_task_list.append(";".join(str_attrs))
                            with open(TASKS_FILE, 'w') as task_file:
                                task_file.write("\n".join(edited_task_list))
                        print(
                            f"\n✅ {username} is now assigned to this task \n")

                    if edit_action == 'd':
                        due_date = str(
                            input("Enter the new due date (YYYY-MM-DD): "))
                        due_date_time = datetime.strptime(
                            due_date, DATETIME_STRING_FORMAT)

                        for t in full_task_list:
                            user_task_list[selected_task]['due_date'] = due_date_time

                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(
                                    DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            edited_task_list.append(";".join(str_attrs))

                            with open(TASKS_FILE, 'w') as task_file:
                                task_file.write("\n".join(edited_task_list))
                        print(f"\n✅ Due date updated to {due_date}\n")
        else:
            print(f"Task number {selected_task} does not exist. ")


# Create tasks.txt if it doesn't exist
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as default_file:
        pass

with open(TASKS_FILE, 'r+') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(
        task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    # curr_t['task_no'] = task_components[6]

    task_list.append(curr_t)


# ====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open(USER_FILE, 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ").lower()
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    if curr_user == 'admin':
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
    try:
        if menu == 'r':
            reg_user()

        elif menu == 'a':
            add_task()

        elif menu == 'va':
            view_all()

        elif menu == 'vm':
            view_main()

        elif menu == 'gr' and curr_user == 'admin':
            gen_report()

        elif menu == 'ds' and curr_user == 'admin':
            '''If the user is an admin they can display statistics about number of users
                and tasks.'''
            try:
                with open('task_overview.txt', 'r') as f:
                    print(f.read())
                with open('user_overview.txt', 'r') as f2:
                    print(f2.read())
            except FileNotFoundError:
                # If files don't exist, generate reports first
                gen_report()
                with open('task_overview.txt', 'r') as f:
                    print(f.read())
                with open('user_overview.txt', 'r') as f2:
                    print(f2.read())

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
    except ValueError as e:
        print(e)
        continue
