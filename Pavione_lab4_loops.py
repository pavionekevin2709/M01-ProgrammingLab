#File name : Pavione_Lab4_loops.py
# CSS 111 Module 4 Lab 4: Working with For and While Loops 

# Displaying FOR LOOPS
print("====FOR LOOPS====")


# Create a list of five favorite foods:
favorite_foods = ["Pasta", "Rice", "Fried Chicken", "Cheeseburger", "Brazilian BBQ"]

# Use a for loop to print each food on its own line
for food in favorite_foods:
    print(food)


# Displaying WHILE LOOPS
print("====WHILE LOOPS====")

#Use a while loop to print the favorite foods list in reverse order
index=len(favorite_foods) -1
while index>=0:
    print(favorite_foods[index])
    index-=1 

# Additional While Loop Examples
# Example 1: Countdown Timer
print("Countdown: \n")
countdown=5
while countdown>0:
    print(countdown)
    countdown-=1
    print("Countdown Complete!")


# Example 2: Sum numbers from 1 to 5
print("Sum of numbers 1 to 5: \n")
total=0
number=1
while number<=5:
    total+=number
    number+=1
    print(f"Total Sum: {total}!")
