# practice for cs50p lecture 0 - functions and variables


# 1. first program
print("hello, world")

# 2. input and variables
name = input("What's your name? ")
print("hello, " + name)

# 3. multiple arguments (comma adds a space)
print("hello,", name)

# 4. named parameters: end and sep change how print works
print("hello, ", end="")
print(name)
print("a", "b", "c", sep="-")

# 5. escaping characters
print("he said \"hello\"")      # \" prints a quote
print("line one\nline two")     # \n makes a new line

# 6. f-string
print(f"hello, {name}")

# 7. string methods
name = name.strip().title()
print(f"cleaned: {name}")

# 8. split
full = input("Full name: ").strip().title()
first, last = full.split(" ")
print(f"hello, {first}")

# 9. calculator (type conversion)
x = int(input("x: "))
y = int(input("y: "))
print(x + y)

# 10. floats and round
a = float(input("a: "))
b = float(input("b: "))
z = round(a + b)
print(z)

# 11. numeric formatting
big = round(a * 1000 + b * 1000)
print(f"{big:,}")           # commas in big numbers

# 12. division
print(a / b)                # normal division gives a float
print(round(a / b, 2))      # rounded to 2 digits
print(f"{a / b:.2f}")       # same thing using an f-string


# 13. my own functions
def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    hello()                 # no argument, so default "world" is used
    n = int(input("n: "))
    print("n squared is", square(n))


# 14. default parameter
def hello(to="world"):
    print(f"hello, {to}")


# 15. return value
def square(n):
    return n * n


# 16. scope: "name" inside main is not visible in hello or square,
# so values are passed in as arguments instead
main()