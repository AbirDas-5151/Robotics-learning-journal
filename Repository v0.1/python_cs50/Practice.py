#Gemini Lecture 0 & 1 practice quiz
""""
x = int(input("Enter a number: "))
if x > 5:
    print("Greater")
else:
    print("Leaser or equal")
"""

#ChatGPT: Lecture 0 — Functions and Variables
#Easy
""""
#F1 — Print: Write a program that prints exactly:
print("hello, world")

#F2 — Input: Ask the user for their name, then print:
User = input("What is your name: ")
print("Hello,", User)

#F3 — Argument: What does the end argument do here?
print("hello", end="...")
print("world")
-> The end argument in print("hello", end="...") changes what is printed at the end of the line instead of the default newline (\n).

#F4 — Separator: Change this code so it prints hello-world.
print("hello", "world")
-> print("hello", "world", sep="-")

#F5 — Variable: Ask for the user’s favorite color and store it in a variable called color. Print a sentence using it.
color = input("What is your favorite color: ")
print(color)

#F6 — String formatting: Fix the bug:
name = input("What's your name? ")
print("hello," , name)

#F7 — Integer conversion: Ask for two whole numbers and print their sum.
number_1 = int(input("Enter the number: "))
number_2 = int(input("Enter the number: "))

sum = (number_1 + number_2)
print(sum)

#F8 — Float conversion: Ask for the price of one item and how many items the user wants. Print the total cost.
Price = float(input("What is the price: "))
Quantity = int(input("How many items: "))
print(Price * Quantity)

#F9 — Comments: Add a useful one-line comment to explain this code:
#Ask the user for their names & then greet them
name = input("Name: ")
print(f"Hello, {name}")
"""
#Medium
"""
#F11 — Greeting function: Write a function called hello() that prints hello, then call it.
def hello():
    print("hello")
    
hello()

#F12 — Function parameter: Write hello(to) so this works:
def hello(to):
    print("hello,", to)

#F13 — Default parameter: Write hello(to="world") so both of these work:
def hello(to="world"):
    print("hello", to)

#F14 — Return value: Write a function square(n) that returns the square of n. Print the result of square(5)
def square(n):
    return (n ** 2)

print(square(5))

#F15 — Refactor: Turn this repeated code into a function:
def meow():
    for i in range(3):
        print("Meow")

meow()

#F16 — Name cleanup: Ask for a name that may have extra spaces, such as "   grace hopper   ", and print it neatly as Grace Hopper.
name = input("What is your name: ").strip().title()
print (name)

#F17 — Division: Ask for two numbers and print the result of dividing the first by the second. Use floats.
x = float(input("what is your 1st number: "))
y = float(input("What is your 2nd number: "))
division = (x / y)
print(division)

#F18 — Rounding: Ask for a bill total and number of people. Print each person’s share rounded to two decimal places.

total_bill = float(input("What is the total amount? "))
people = float(input("Total number of people? "))

total = total_bill / people

print(f"{total:.2f}")

#F19 — Debugging: Fix this:
def main():
    name = input("Name: ")
    hello(name)

def hello(to):
    print(f"hello, {to}")

main()
"""
#Hard
#F21 — Calculator function: Write calculate(x, y) that returns and prints:
# - sum
# - difference
# - product
# - quotient
