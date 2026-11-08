# CS50P Lecture 0: Functions and Variables

Video: CS50P - Lecture 0 - Functions, Variables (CS50, about 1h 45m)
Official notes: https://cs50.harvard.edu/python/notes/0
Timestamps below come from a Google summary. Only 0:00, 3:19, 4:00 and
5:06 are confirmed, so check the rest in the video.

## Video map
| Time | Topic |
|---|---|
| 0:00 | Introduction |
| 0:24 | First program, hello.py |
| 3:19 | Command-line interface |
| 4:00 | Python interpreter |
| 5:06 | Functions, arguments, side effects |
| 7:35 | Bugs and debugging |
| 9:54 | VS Code and IDEs |
| 12:16 | Return values and variables |
| 19:56 | Comments and pseudocode |
| 25:05 | Multiple arguments |
| 31:01 | Named parameters |
| 40:48 | Escaping characters |
| 43:10 | f-strings |
| 45:04 | String methods |
| 54:43 | Style |
| 57:50 | split |
| 59:35 | Integers and operators |
| 1:03:13 | calculator.py |
| 1:06:25 | Type conversion |
| 1:14:36 | Floats |
| 1:19:18 | Numeric formatting |
| 1:22:47 | Division |
| 1:26:14 | Defining functions |
| 1:39:01 | Scope |
| 1:41:17 | Return values |
| 1:45:11 | Conclusion |

## 1. Running code
- Write code in a `.py` file in an editor like VS Code (an IDE).
- Run it in the terminal (command-line interface): `python hello.py`
- The Python interpreter translates your code into zeros and ones.

## 2. Functions
- A function is an action, like `print`.
- An argument is the input you give it: `print("hello, world")`.
- A side effect is what the function does, like showing text on screen.

## 3. Bugs
- A syntax error means you broke Python's rules, like a missing bracket.
- Read the error message. It shows the line to check.

## 4. Variables
- `name = input("What's your name? ")` stores the user's text in `name`.
- `=` means "store the right side in the left side".
- `input` always returns a string.

## 5. Comments and pseudocode
- A comment starts with `#`. Python ignores it.
- Pseudocode means writing the steps in plain words before coding.

## 6. Arguments and named parameters
- Many arguments are separated by commas: `print("hello,", name)`.
- Named parameters change behaviour: `end=""` stops the new line,
  `sep="-"` changes the separator.

## 7. Escaping characters
- `\"` prints a quote inside a string.
- `\n` starts a new line.

## 8. f-strings
- `print(f"hello, {name}")` puts a variable inside text.
- The `f` before the first quote is required.

## 9. String methods and split
- `.strip()` removes extra spaces. `.title()` capitalizes each word.
- Chain them: `name.strip().title()`.
- `.split(" ")` breaks text into parts.

## 10. Style
- Use clear names, add comments where needed, and keep lines readable.

## 11. Numbers
- `int` is a whole number, `float` has a decimal point.
- Operators: `+  -  *  /`
- Convert user input: `x = int(input("x: "))`.
- `round(number, digits)` rounds a number.
- `f"{big:,}"` adds commas. `f"{z:.2f}"` shows 2 decimal places.
- `/` always gives a float.

## 12. Defining functions
- `def` creates a function. A parameter can have a default: `to="world"`.
- `return` sends a value back to the caller.
- **Scope:** a variable made inside a function does not exist outside it.
  Pass values as arguments.
- Common pattern: put the steps in `main()` and call `main()` at the bottom.

## 13. Common mistakes
- Forgetting `int()` or `float()`, so `"2" + "3"` becomes `"23"`.
- Forgetting the `f` in an f-string.
- Forgetting to call `main()`.
- Wrong indentation inside a function.

## 14. Review questions
1. What is the difference between an argument and a side effect?
2. Why must you use `int()` or `float()` on `input()` before doing maths?
3. What do `end=""` and `sep="-"` change in `print`?
4. What is the difference between `print` and `return` in a function?
5. Why can't `hello()` use a variable that was created inside `main()`?

**Answers (check after trying):**
1. An argument is the input you give. A side effect is what the function does, like showing text.
2. `input` returns a string, and strings can't be added as numbers.
3. `end` changes what comes after the text (no new line), `sep` changes what goes between values.
4. `print` shows text on screen. `return` hands a value back so the program can use it.
5. Variables inside a function only exist there. This is scope.

## 15. Hints for Problem Set 0 (hints only)
- Read each problem's description and write the steps in comments first.
- For text problems, think about which string method could change the text.
- For the maths problem, remember `input` gives a string, so convert it first.
- Test each function with simple values before using real ones.
- Write your own solution. Ask me for a hint when stuck, with your code and the error.

## 16. Try yourself
- Add a `cube(n)` function.
- Change `hello` so it takes a first and last name.
- Print a name with `sep` and `end` in a different way.