# Eric Isaac
# Project 2
"""This program produces a variety of menu options that user can select, and each
of the options will generate a math or security related function."""

import math
import string
import secrets
from datetime import date

# Function to display the menu options
def display_menu():
    """This function displays the menu options for this program."""
    print('Please choose from the following options:')
    print('a. Generate Secure Password')
    print('b. Calculate and Format a Percentage')
    print('c. How many days from today until July 4, 2025?')
    print('d. Use the Law of Cosines to calculate the leg of a triangle.')
    print('e. Calculate the volume of a Right Circular Cylinder')
    print('f. Exit program')

# Function to generate a secure password
def generate_password(password_length, use_mixed_case, use_numbers, special_characters):
    """Function to generate a secure password"""
    # Generate a password with only lower letters
    if use_mixed_case == 'n' and use_numbers == 'n' and special_characters == 'n':
        alphabet = string.ascii_lowercase
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

    # Generate a password with only mixed-case letters
    if use_mixed_case == 'y' and use_numbers == 'n' and special_characters == 'n':
        alphabet = string.ascii_letters
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

    # Generate a password with lower letters and numbers only
    if use_mixed_case == 'n' and use_numbers == 'y' and special_characters == 'n':
        alphabet = string.ascii_lowercase + string.digits
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

    # Generate a password with lower letters and special characters only
    if use_mixed_case == 'n' and use_numbers == 'n' and special_characters == 'y':
        alphabet = string.ascii_lowercase + string.punctuation
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

    # Generate a password with lower letters, numbers, and special characters
    if use_mixed_case == 'n' and use_numbers == 'y' and special_characters == 'y':
        alphabet = string.ascii_lowercase + string.digits + string.punctuation
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

    # Generate a mixed-case password with numbers
    if use_mixed_case == 'y' and use_numbers == 'y' and special_characters == 'n':
        alphabet = string.ascii_letters + string.digits
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

    # Generate a mixed-case password with numbers and special characters
    if use_mixed_case == 'y' and use_numbers == 'y' and special_characters == 'y':
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ' '.join(secrets.choice(alphabet) for i in range(password_length))
        print('Password: ', password)

# Function to calculate and format a percentage
def calculate_format_percentage(numerator, denominator, decimal_points):
    """Function to calculate and format a percentage"""
    percentage = numerator / denominator * 100.00
    print('%.*f' % (decimal_points, percentage) + ' percent')

# Function to determine number of days from today until July 4, 2025
def days_until_2025():
    """Determine the number of days until July 4, 2024"""
    d_1 = date.today()
    d_2 = date(2025, 7, 4)
    delta = d_2 - d_1
    print(delta.days, 'days until July 4, 2025')

# Function to use the Law of Cosines to calculate the leg of a triangle
def calculate_triangle_leg():
    """Use cosine to calculate the leg of a triangle"""
    print('a=8, b=11, C=37 ... c = ?')
    print('Using the law of cosine to calculate c...')
    c_squared = 8 ** 2 + 11 ** 2 - 2 * 8 * 11 * math.cos(37)
    c_0 = math.sqrt(c_squared)
    print(f'c = {c_0:.2f}')

# Function to calculate the volume of a Right Circular Cylinder
def calculate_cylinder(radius, height):
    """Calculate the volume of a right circular cylinder"""
    volume = math.pi * radius ** 2 * height
    print(f'The volume is {volume:.2f}')



# Welcome the user to the program and display the menu-options
print('Welcome to the Math and Security Program!')
display_menu()

# Read in the menu selection from the user
user_choice = input('\nSelection: ')

# Process user selection, and run the appropriate function
if user_choice == 'a':
    # Read a validate the input for the password length
    password_len = int(input('Password length: '))
    while password_len < 4:
        password_len = int(input('Password length (greater than 4 characters): '))
    # Read in and validate the input for 'use_mixed_case'
    use_mix_case = input('Do you want mixed case letters (y/n)? ')
    while use_mix_case not in ('y', 'n'):
        use_mix_case = input('Do you want mixed case letters (y/n)? ')
    # Read in and validate the input for 'use_numbers'
    use_num = input('Do you want to use numbers (y/n)? ')
    while use_num not in ('y', 'n'):
        use_num = input('Do you want to use numbers (y/n)? ')
    # Read in and validate the input for 'special_characters'
    special_char = input('Do you want to include special characters (y/n)? ')
    while special_char not in ('y', 'n'):
        special_char = input('Do you want to include special characters (y/n)? ')
    print('Generating random password...')
    #Call the function, and pass in the arguments
    generate_password(password_len, use_mix_case, use_num, special_char)
elif user_choice == 'b':
    # Read in the values from the user
    num = int(input('Enter a numerator: '))
    denom = int(input('Enter a denominator: '))
    decimal_point = int(input('Enter a number to format the decimal: '))
    print('Calculating percentage...')
    #Call the function, and pass in the arguments
    calculate_format_percentage(num, denom, decimal_point)
elif user_choice == 'c':
    print('Counting down the days...')
    days_until_2025()
elif user_choice == 'd':
    print('Using cosine to calculate triangle leg...')
    calculate_triangle_leg()
elif user_choice == 'e':
    radius_0 = int(input('Enter the radius of the base of the cylinder: '))
    height_0 = int(input('Enter the height of the cylinder: '))
    print('Calculating the volume of a right circular cylinder...')
    calculate_cylinder(radius_0, height_0)
elif user_choice == 'f':
    print('Exiting the program. Thank you!')
