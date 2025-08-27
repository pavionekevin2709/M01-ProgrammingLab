"""
Project/File Name: CS111: Module 1 Demo ___________
Author:           KevinPavione____________________
Date Created:     8/11/2025___________________________
Last Modified:    8/11/2025__________________________

Purpose:          [Brief description of what this file/project does]

Dependencies:     [List any required libraries, modules, or files]
Usage:            [How to run or use this file/project]
Inputs:           [Describe expected input, if any]
Outputs:          [Describe output, if any]
Notes:            [Any additional important information]
"""

# ===========================
# Guided Practice 1: Python Introduction
# ===========================

# 1. Hello, World!
# ----------------
# Write code below to print "Hello, World!" to the screen.


print('Hello, World!')
print('Welcome to our CS111 Python Demo')



# 2. User Interaction
# ------------------
# Ask the user for their name using input().
# Then, print a personalized greeting, such as "Hello, <Your Name>!".
name=input("What's your name?")
print ("Hello,"+name)







# 3. Basic Arithmetic
# ------------------
# Ask the user to enter two numbers (you can use input()).
# Convert the inputs to numbers (int or float).
# Print the sum, difference, product, and quotient of these numbers.

#Arithmetic Demo
num1=100
num2=10

#SumDemo
print(num1+num2)

#DifferenceDemo 
print(num1-num2)

#ProductDemo
print(num1*num2)

#QuotientDemo
print(num1/num2)



num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)






# 4. Comments
# -----------
# Add comments to your code above explaining what each section does.
# (You can add them now if you haven't already!)



#5 Variables
#------------
#Integer
#assigning the value of 20 to a variable named age
age=20
print (age)
#Printing the variable type for the age variable 
print(type(age))
age_type=type(age)

#Float
height=6.3
print (type(height))

#String
name='Kevin'




# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


# ===========================
# Collaborative Activity #1: Student Information Manager
# ===========================
"""
Write a simple Python program that:
- Asks the user to input their name, age, GPA, and whether they are a full-time student (yes/no).
- Stores each piece of information in a variable of the appropriate type (str, int, float, bool).
- Prints out a summary of the student’s information, nicely formatted.
- (Pracice Using AI): If the user is a full-time student and their GPA is above 3.5, print a congratulatory message.
"""
# AI Assistance Disclosure Statement
"""
Student Name: Kevin Pavione_______________________
Date: 8/13/2025_______________________________
AI Tool Used: GrokAI_______________________

Prompt Given to AI: [Paste the exact prompt here]

Lines of Code AI Assisted: [e.g., 12-24, 37-40]

Description:
The code on the specified lines was generated or significantly modified with the help of the above AI tool, using the prompt provided. The student has reviewed and adapted this code to ensure understanding and compliance with course requirements.

Academic Integrity Statement:
All AI-generated content is properly acknowledged. The student affirms that they understand the code and have adhered to the institution’s academic integrity policy regarding the use of AI tools.
"""

name=input("What's your name?")
age=int(input("What's your age?"))
GPA=float(input("What's your GPA?"))
print(f"{name} is {age} years old and has a {GPA} studying at OCU.")
full_time = input("Are you a full-time student? (yes/no): ").lower() == "yes"
if full_time and GPA > 3.5:
    print(f"Congratulations, {name}! Your GPA of {GPA} as a full-time student is outstanding!")


# The first 3 codes are used to create questions and define the AGE as a integer number while the GPA is defined as a float because it's usually a decimal number.
# The fourth code is used to print the user's name and age, also showing their given GPA.
# The fifth code is used to define the full_time in the input(question) 
# The line 143 used IF to define if the student will get the congratulatory message in thE printing code below, only in case the student answer yes and he has a GPA greater than 3.5





