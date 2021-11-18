# Programmers: Anthony DelVecchio
# Course: CS151, Dr. Rajeev
# Date: 11/17/21
# Lab Number: 8
# Program Inputs: File name
# Program Outputs: A random student name from that file

# Import random library
import random

# Define function to ask for filename
def load_name_list(filename):
    student_names = []
    filename = input("Enter a file name: ")
    try:
        file = open(filename, "r")
        for line in file:
            temp = line.split()
            student_names.append(temp)
    except FileNotFoundError:
        print("File does not exist.")
        load_name_list(filename)
    return student_names

# Define function for picking random name (using example file)
def pop_random_name():
    students = load_name_list("TestList.txt")
    random_student_name = random.choice(students)
    print(random_student_name)
    students.remove(random_student_name)
# Define main function
def main():
    pop_random_name()
    run_again = input("Would you like to run the program again? (Y or N) ")
    if run_again == "Y":
        main()
    elif run_again == "N":
        print("Exiting Program")
        exit()

# Run program
main()