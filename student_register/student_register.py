############## *** T15 *** ###################
# The 15th task in HyperionDev Bootcamp.
# Student registration form
##############################################

from datetime import datetime

# Maximum and minimum number of students to be allowed to register at once
min_students = 1
max_students = 387


# Pluralize function to add appropriate suffix to number
def pluralize(count):
    if count == 1:
        plural = 'st'
    elif count == 2:
        plural = 'nd'
    elif count == 3:
        plural = 'rd'
    else:
        plural = 'th'
    return plural


# Zeroing loop counter
loop = 0


# Get input from user and save to file
while True:
    try:
        student_num = int(
            input(f"How many students do you want to register? ({min_students}-{max_students}): "))

        # Validate input
        if student_num == 0:
            print("❌ If you want to register any one, you can't enter 0.")
        elif student_num < min_students:
            print(
                f"❌ It is not possible to register students in the number of '{student_num}'. You must specify the number of students from {min_students} to {max_students}.")
        elif student_num > max_students:
            print(
                f"❌ We have a total of {max_students} students. So you can't register '{student_num}' students.")
        else:
            # Loop over appropriate number of students
            for student in range(student_num):
                loop += 1
                try:
                    # Get ID of the student
                    student_id = str(input(
                        f"Enter the ID of the {loop}{pluralize(loop)} student: "))

                except Exception as e:
                    print(e)
                try:
                    # Save data to file in readable format ready to sign by students
                    with open('reg_form.txt', 'a') as reg_form:
                        reg_form.write(f'''
============================================================

Student ID: {student_id}
Registration date: {datetime.now().strftime('%d %B %Y')}
Signature:



..................................

        
                    ''')

                # This shouldn't happen
                except Exception as e:
                    print(f"❌ Something went wrong when saving file: {e}")

            # Ask the user if want to see the current state of form
            read_file = input(
                "Do you want read current state of register form? (y/n): ").lower()

            if read_file == "y":
                # Print out the content of the form file
                with open('reg_form.txt', 'r') as reg_form:
                    print(reg_form.read())

    # Catch errors
    except ValueError as e:
        print('❌ Only integers are allowed.')
    # Catch unexpected errors
    except Exception as e:
        print('❌ ', e)
