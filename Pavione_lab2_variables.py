# Programming Lab 2: Exploring Variables and Data Types 

name = str("Kevin Pavione") #Stores the name in a variable(string)
age= int(19) #Stores the age in a variable(integer)
height= float(1.92) #Stores the height in a variable(float)
is_student = True #Stores the student condition in a variable (boolean)

print (f"Hi my name is {name}, I am {age} years old and I'm {height} meters tall. I am a student: {is_student}") #Displays the wholes student's information and conditions.

# Calculating my age in months

age_months=age*12
print(f"My age in months: {age_months} months") #Displays the student's age in Months, by multiplying by 12.

# Calculating my height if I grew by 0.1 meters (since 0.1m = 10cm)

new_height=height+0.10
print(f"(If i grew by 0.1 meters, now I can say that I am {new_height} meters tall.)") #Displays the new height by adding 0.1m.

# Toggling my Student Status 
 
print(f"New student status: {'True' if is_student else 'False'}")  #Displays the student condition as a student or not.
 


