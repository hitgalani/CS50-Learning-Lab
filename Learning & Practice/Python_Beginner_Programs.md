# Python Beginner Programs

A beginner-friendly collection of Python examples, arranged from basic
concepts to small projects.

## How to use this file

1.  Create a separate `.py` file for each program using the filename
    shown.
2.  Copy the matching code block into that file.
3.  Save the file.
4.  Run it from a terminal with `python filename.py` (on some systems,
    use `python3 filename.py`).

Most examples use only Python's standard library. The weather API
example additionally requires the `requests` package and a real API
endpoint.

## Programs included

1.  [1. Student Marks Calculator](#student_markspy) ---
    `student_marks.py`
2.  [2. Calculate Total and Average of a List](#number_calculatorpy) ---
    `number_calculator.py`
3.  [3. Print a Star Pattern](#star_patternpy) --- `star_pattern.py`
4.  [4. Local and Global Variables](#variable_scopepy) ---
    `variable_scope.py`
5.  [5. List Comprehension](#list_comprehensionpy) ---
    `list_comprehension.py`
6.  [6. Filter Even Numbers](#filter_even_numberspy) ---
    `filter_even_numbers.py`
7.  [7. Weather API Request](#weather_apppy) --- `weather_app.py`
8.  [8. Bank Account Management System](#bank_accountpy) ---
    `bank_account.py`
9.  [9. Simple Rule-Based Chatbot](#simple_chatbotpy) ---
    `simple_chatbot.py`
10. [10. Simple Calculator](#simple_calculatorpy) ---
    `simple_calculator.py`
11. [11. Basic Password Checker](#password_checkerpy) ---
    `password_checker.py`
12. [12. Number Guessing Game](#guessing_gamepy) --- `guessing_game.py`
13. [13. Student Management Using a Class](#student_managementpy) ---
    `student_management.py`

------------------------------------------------------------------------

`<a id="student_markspy">`{=html}`</a>`{=html} \## 1. Student Marks
Calculator

**File name:** `student_marks.py`

### What this program does

Accepts a student's name and marks in three subjects, calculates the
total and average, then displays Pass when the average is at least 40;
otherwise, it displays Fail.

### Complete code

``` python
# Get student details
name = input("Enter Student Name: ")

maths_marks = int(input("Enter Student Maths Marks: "))
science_marks = int(input("Enter Student Science Marks: "))
english_marks = int(input("Enter Student English Marks: "))

# Calculate total and average
total_marks = maths_marks + science_marks + english_marks
average_marks = total_marks / 3

# Check result
if average_marks >= 40:
    result = "Pass"
else:
    result = "Fail"

# Display student report
print(f"Student Name: {name}")
print(f"Maths Marks: {maths_marks}")
print(f"Science Marks: {science_marks}")
print(f"English Marks: {english_marks}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks:.2f}")
print(f"Result: {result}")
```

### Example output

``` text
Enter Student Name: Asha
Enter Student Maths Marks: 80
Enter Student Science Marks: 70
Enter Student English Marks: 90
Student Name: Asha
Maths Marks: 80
Science Marks: 70
English Marks: 90
Total Marks: 240
Average Marks: 80.00
Result: Pass
```

### Concepts covered

-   input() and int() for user input
-   Arithmetic operators for total and average
-   if-else conditions
-   f-strings for formatted output

`<a id="number_calculatorpy">`{=html}`</a>`{=html} \## 2. Calculate
Total and Average of a List

**File name:** `number_calculator.py`

### What this program does

Stores five numbers in a list, adds them using a for loop, and
calculates their average. len(numbers) gets the number of items, so the
code does not need a hard-coded list length.

### Complete code

``` python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total = total + number

average = total / len(numbers)

print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
```

### Example output

``` text
Numbers: [10, 20, 30, 40, 50]
Total: 150
Average: 30.0
```

### Concepts covered

-   Lists store multiple values
-   for loops process each item
-   len() returns the number of items
-   Running totals and division

`<a id="star_patternpy">`{=html}`</a>`{=html} \## 3. Print a Star
Pattern

**File name:** `star_pattern.py`

### What this program does

Uses nested loops to print rows of stars. The outer loop controls the
row number; the inner loop prints that row's stars. print() moves to the
next line.

### Complete code

``` python
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
```

### Example output

``` text
*
**
***
****
```

### Concepts covered

-   range() controls loop repetitions
-   Nested for loops
-   print(end='') keeps output on the same line

`<a id="variable_scopepy">`{=html}`</a>`{=html} \## 4. Local and Global
Variables

**File name:** `variable_scope.py`

### What this program does

Shows that a variable created inside a function is local to that
function. The global x remains 100 even though the function creates a
separate local x with value 50.

### Complete code

``` python
# Global variable
x = 100

def my_function():
    # Local variable
    x = 50
    print("Local Variable:", x)

my_function()

print("Global Variable:", x)
```

### Example output

``` text
Local Variable: 50
Global Variable: 100
```

### Concepts covered

-   Defining and calling functions
-   Local variable scope
-   Global variable scope

`<a id="list_comprehensionpy">`{=html}`</a>`{=html} \## 5. List
Comprehension

**File name:** `list_comprehension.py`

### What this program does

Creates a new list containing the square of each number. The expression
inside the list comprehension runs once for each item.

### Complete code

``` python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Original Numbers:", numbers)
print("Square Numbers:", squares)
```

### Example output

``` text
Original Numbers: [1, 2, 3, 4, 5]
Square Numbers: [1, 4, 9, 16, 25]
```

### Concepts covered

-   Lists
-   for-loop logic in a compact expression
-   Expressions and multiplication

`<a id="filter_even_numberspy">`{=html}`</a>`{=html} \## 6. Filter Even
Numbers

**File name:** `filter_even_numbers.py`

### What this program does

Uses filter() to keep only numbers for which the lambda condition is
true. A number is even when its remainder after division by 2 is zero.

### Complete code

``` python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original Numbers:", numbers)
print("Even Numbers:", even_numbers)
```

### Example output

``` text
Original Numbers: [1, 2, 3, 4, 5, 6]
Even Numbers: [2, 4, 6]
```

### Concepts covered

-   filter() selects items that pass a condition
-   lambda creates a small anonymous function
-   \% is the modulo operator
-   list() converts the filter result into a list

`<a id="weather_apppy">`{=html}`</a>`{=html} \## 7. Weather API Request

**File name:** `weather_app.py`

### What this program does

Demonstrates how to send an HTTP GET request and read a JSON response.
The example URL is a placeholder, not a working weather service. Replace
it with an endpoint from a real weather provider and supply any required
API key according to that provider's instructions.

### Complete code

``` python
import requests

# Replace this with a real weather API endpoint.
url = "https://api.example.com/weather"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    print("Weather Information:")
    print(data)

except requests.exceptions.RequestException as error:
    print("Error fetching weather data:", error)
```

### Example output

``` text
# Install the library first:
python -m pip install requests

# Then run:
python weather_app.py

# With the placeholder URL, the request will normally fail.
# The error is caught and displayed.
```

### Concepts covered

-   import requests loads the Requests library
-   get() sends an HTTP GET request
-   timeout limits how long the request waits
-   raise_for_status() raises an error for unsuccessful HTTP status
    codes
-   json() parses a JSON response
-   try-except handles request errors

`<a id="bank_accountpy">`{=html}`</a>`{=html} \## 8. Bank Account
Management System

**File name:** `bank_account.py`

### What this program does

Builds a simple menu-driven bank account practice program. The
BankAccount class stores the account holder's name and balance, and
provides methods to deposit, withdraw, and check the balance. It rejects
non-positive transactions and prevents withdrawals that exceed the
balance.

### Complete code

``` python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful.")
            print("New balance:", self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal successful.")
                print("New balance:", self.balance)
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print("Current balance:", self.balance)


name = input("Enter your name: ")
balance = float(input("Enter your starting balance: "))

if balance < 0:
    print("Starting balance cannot be negative.")
else:
    account = BankAccount(name, balance)

    while True:
        print("\n===== Bank Account Management =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            print("Thank you for using our bank service,", name)
            break

        else:
            print("Invalid choice. Please try again.")
```

### Example output

``` text
Enter your name: Ravi
Enter your starting balance: 1000

===== Bank Account Management =====
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. Exit
Enter your choice: 1
Enter deposit amount: 500
Deposit successful.
New balance: 1500.0

Enter your choice: 3
Current balance: 1500.0
```

### Concepts covered

-   Classes and objects
-   **init**() initializes an object
-   self refers to the current object
-   Methods define object behavior
-   while loop repeats the menu
-   if-elif-else handles menu choices

`<a id="simple_chatbotpy">`{=html}`</a>`{=html} \## 9. Simple Rule-Based
Chatbot

**File name:** `simple_chatbot.py`

### What this program does

Responds to a small set of predefined messages. It is rule-based, not an
AI or machine-learning chatbot. The conversation continues until the
user types bye.

### Complete code

``` python
print("Welcome to Simple Chatbot!")

name = input("What is your name? ")
print("Hello", name, "!")

while True:
    message = input("\nYou: ").lower()

    if message == "hello":
        print("Bot: Hello! How are you?")

    elif message == "how are you":
        print("Bot: I am fine. Thank you!")

    elif message == "what is your name":
        print("Bot: I am a Simple Chatbot.")

    elif message == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
```

### Example output

``` text
Welcome to Simple Chatbot!
What is your name? Ravi
Hello Ravi !

You: hello
Bot: Hello! How are you?

You: bye
Bot: Goodbye! Have a nice day.
```

### Concepts covered

-   while loop keeps the conversation running
-   lower() makes matching case-insensitive
-   if-elif-else selects a response
-   break exits the loop

`<a id="simple_calculatorpy">`{=html}`</a>`{=html} \## 10. Simple
Calculator

**File name:** `simple_calculator.py`

### What this program does

Takes two numbers and lets the user choose an arithmetic operation. It
checks for division by zero before dividing.

### Complete code

``` python
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\n===== Simple Calculator =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter Your Choice: ")

if choice == "1":
    print("Addition:", num1 + num2)

elif choice == "2":
    print("Subtraction:", num1 - num2)

elif choice == "3":
    print("Multiplication:", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid Choice!")
```

### Example output

``` text
Enter First Number: 10
Enter Second Number: 5

===== Simple Calculator =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter Your Choice: 1
Addition: 15.0
```

### Concepts covered

-   float() accepts decimal numbers
-   Arithmetic operators +, -, \*, /
-   if-elif-else selects the operation
-   Nested if checks for division by zero

`<a id="password_checkerpy">`{=html}`</a>`{=html} \## 11. Basic Password
Checker

**File name:** `password_checker.py`

### What this program does

Performs a few basic checks: at least eight characters, and not only
digits or only letters. This is a beginner exercise, not a complete
password-strength or security validator.

### Complete code

``` python
password = input("Enter Your Password: ")

if len(password) < 8:
    print("Password is too short.")

elif password.isdigit():
    print("Password cannot contain only numbers.")

elif password.isalpha():
    print("Password cannot contain only letters.")

else:
    print("Password looks good!")
```

### Example output

``` text
Enter Your Password: hello123
Password looks good!
```

### Concepts covered

-   len() checks string length
-   isdigit() checks whether all characters are digits
-   isalpha() checks whether all characters are letters
-   if-elif-else selects the message

`<a id="guessing_gamepy">`{=html}`</a>`{=html} \## 12. Number Guessing
Game

**File name:** `guessing_game.py`

### What this program does

Chooses a random integer from 1 to 10. The user keeps guessing; the
program gives a higher/lower hint and stops when the answer is correct.

### Complete code

``` python
import random

secret_number = random.randint(1, 10)

print("===== Number Guessing Game =====")
print("Guess a number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break

    elif guess < secret_number:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")
```

### Example output

``` text
===== Number Guessing Game =====
Guess a number between 1 and 10
Enter your guess: 3
Too low! Try again.
Enter your guess: 7
Congratulations! You guessed the correct number.
```

### Concepts covered

-   random.randint() generates a random integer
-   while loop repeats guesses
-   if-elif-else compares the guess
-   break exits when the guess is correct

`<a id="student_managementpy">`{=html}`</a>`{=html} \## 13. Student
Management Using a Class

**File name:** `student_management.py`

### What this program does

Uses a Student class to keep student data and related operations
together. The object calculates total marks, average marks, and the
pass/fail result, then prints a report.

### Complete code

``` python
class Student:
    def __init__(self, name, maths, science, english):
        self.name = name
        self.maths = maths
        self.science = science
        self.english = english

    def calculate_total(self):
        return self.maths + self.science + self.english

    def calculate_average(self):
        return self.calculate_total() / 3

    def check_result(self):
        if self.calculate_average() >= 40:
            return "Pass"
        else:
            return "Fail"

    def display_details(self):
        print("\n===== Student Report =====")
        print("Student Name:", self.name)
        print("Maths Marks:", self.maths)
        print("Science Marks:", self.science)
        print("English Marks:", self.english)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", self.calculate_average())
        print("Result:", self.check_result())


name = input("Enter Student Name: ")
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))

student = Student(name, maths, science, english)
student.display_details()
```

### Example output

``` text
Enter Student Name: Asha
Enter Maths Marks: 80
Enter Science Marks: 70
Enter English Marks: 90

===== Student Report =====
Student Name: Asha
Maths Marks: 80
Science Marks: 70
English Marks: 90
Total Marks: 240
Average Marks: 80.0
Result: Pass
```

### Concepts covered

-   Classes and objects
-   Attributes store student data
-   Methods calculate and display information
-   return sends a result back from a method

## General notes

-   The sample outputs are examples; user input and random values can
    make actual output different.
-   Enter valid numeric input where a program asks for a number. These
    beginner examples do not all include input-validation for every
    possible invalid entry.
-   The weather URL `https://api.example.com/weather` is intentionally a
    placeholder. It will not provide real weather data. Use a real
    provider's API endpoint and follow its authentication instructions.
-   The bank account program is for learning Python classes and
    conditions only. It is not connected to a bank and should not be
    used to store or manage real money.
-   The password checker is only a small string-method exercise. Do not
    use it as a real security assessment.

## Suggested learning order

Start with the student marks calculator, number list, star pattern, and
variable scope. Then study list comprehension and filtering. After that,
try the calculator, password checker, guessing game, chatbot, and
finally the class-based student and bank account projects.
