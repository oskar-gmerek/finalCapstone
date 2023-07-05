# Task Manager
This is a simple command-line task manager program written in Python. It allows users to register new users, add tasks, view tasks, and generate task statistics.
--- 


## Table of Contents
1. [Getting Started](#getting_started)
2. [Usage](#usage)
3. [Notes](#notes)
4. [Screenshot](#screenshot)
5. [Credits](#credits)

## Getting Started

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/oskar-gmerek/finalCapstone
   ```
2. Navigate to the project directory
   ```bash
   cd task_manager
   ```
3. Ensure you have Python installed. This project was developed using Python 3.11.
4. Run the script using a Python interpreter `python student_register.py` from student_register folder.

## Usage
Run program `python student_register.py`
 Use prompt menu to navigate.

 ### User Registration
- To register a new user, run the program and choose the option to register.
- Enter a new username and password when prompted.
- If the username is available and the password confirmation matches, the new user will be added to the user.txt file.

### Adding a Task
- To add a new task, run the program and choose the option to add a task.
- Enter the username of the person to whom the task is assigned.
- Enter the title, description, and due date of the task as requested.
- The task will be added to the tasks.txt file.

### Viewing Tasks
- To view all tasks, run the program and choose the option to view all tasks.
- The program will read tasks from the tasks.txt file and display them in a formatted manner.

### Generating Task Statistics
- To generate task statistics, run the program and choose the option to generate task statistics.
- The program will calculate the number of completed, uncompleted, and overdue tasks.
- If no user is specified, overall task statistics will be displayed.
- If a user is specified, task statistics specific to that user will be displayed.

## Notes
Use the following username and password to access admin rights:
- Username: admin
- Password: password

## Screenshot

<img width="728" alt="Zrzut ekranu 2023-07-5 o 23 18 52" src="https://github.com/oskar-gmerek/finalCapstone/assets/53402105/3a3e4dc9-02a0-4ad4-b2f3-f426d05a93df">


## Credits
This project was created by [Oskar Gmerek](https://github.com/oskar-gmerek) as part of the HyperionDev Software Engineering Bootcamp.
