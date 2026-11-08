# CS50 Study Guide: Python Basics and AI Search

A self-study guide with notes, worked examples, practice questions and a full answer key.
Based on two CS50 lectures. These are unofficial study materials, not official course content.

- **Part 1: Python** (CS50P Lecture 0: Functions, Variables)
- **Part 2: AI Search** (CS50 AI Lecture 0: Search)

The two parts are separate. Part 2 assumes you know basic Python: lists, dictionaries, loops and functions.

## How to use this guide

1. Read the notes for a part. Watch the matching video section.
2. Type every example yourself. Do not paste it.
3. Try each question for 10 to 15 minutes before looking at the answer key (the last section).
4. For "Fix the bug" questions, run the code and read the error message first. It tells you the line.
5. Your answer does not need to look like mine. For code, **the same output means correct**.
6. After each solution, change something (a name, a number, a rule) and run it again.

## Verification legend

- **Confirmed** means checked on an official CS50 page or by running the code.
- **Unverified** means it came from a third-party summary and I could not check it. Check it yourself.

All code in the answer key was run, and the outputs shown were produced by running it.

## Progress tracker

| Level | Part 1: Python | Part 2: AI |
|---|---|---|
| 0. Quick quiz | [ ] | [ ] |
| 1. Reader (predict the output) | [ ] | [ ] |
| 2. Fixer (find and fix the bug) | [ ] | [ ] |
| 3. Builder (write small programs) | [ ] | [ ] |
| 4. Project (build something bigger) | [ ] | [ ] |
| 5. Challenge (pro level) | [ ] | [ ] |

---

# PART 1: PYTHON

## 1.1 Video map (CS50P Lecture 0, about 1h 45m)

Only the first four times were confirmed (from the video description). All other times come from a Google summary and are unverified.

| Time | Topic | Status |
|---|---|---|
| 0:00 | Introduction | Confirmed |
| 3:19 | Command-line interface | Confirmed |
| 4:00 | Python interpreter | Confirmed |
| 5:06 | Functions, arguments, side effects | Confirmed |
| 7:35 | Bugs and debugging | Unverified |
| 9:54 | VS Code and IDEs | Unverified |
| 12:16 | Return values and variables | Unverified |
| 19:56 | Comments and pseudocode | Unverified |
| 25:05 | Multiple arguments | Unverified |
| 31:01 | Named parameters | Unverified |
| 40:48 | Escaping characters | Unverified |
| 43:10 | f-strings | Unverified |
| 45:04 | String methods | Unverified |
| 54:43 | Style | Unverified |
| 57:50 | split | Unverified |
| 59:35 | Integers and operators | Unverified |
| 1:03:13 | calculator.py | Unverified |
| 1:06:25 | Type conversion | Unverified |
| 1:14:36 | Floating point values | Unverified |
| 1:19:18 | Numeric formatting | Unverified |
| 1:22:47 | Division | Unverified |
| 1:26:14 | Defining functions | Unverified |
| 1:39:01 | Scope | Unverified |
| 1:41:17 | Return values | Unverified |
| 1:45:11 | Conclusion | Unverified |

## 1.2 Notes

The headings follow the official written notes. Everything in this section was confirmed against them, except where marked "video only" or "extra".

### Running code
- VS Code is a text editor. It also has a terminal where you type commands.
- Python code is saved in a file ending in `.py`. Run it with `python hello.py`.
- The Python interpreter reads your text and translates it into zeros and ones the computer understands.

### Functions
- A function is a verb, an action Python already knows how to do, like `print`.
- An argument is the value you give it: `print("hello, world")`.
- A side effect is what the function does, like showing text on the screen.

### Bugs
- A bug is a mistake in your code. They are a normal part of coding.
- A missing `)` makes the interpreter show an error. Error messages often show which line to check.

### Variables
- A variable is a container for a value.
- `name = input("What's your name? ")` stores what the user types in `name`.
- `=` assigns the right side to the left side. It does not mean "equals" as in maths.
- `print("hello, name")` prints the word `name`, not the variable.

### Comments and pseudocode
- A comment starts with `#`. Python ignores it. It is a note for you and others.
- Pseudocode is a plan written as comments, like a to-do list, before you write the code.

### Multiple arguments
- Separate arguments with a comma: `print("hello,", name)`. `print` adds a space between them.
- You can also join strings with `+`: `print("hello, " + name)`.

### Strings and parameters
- A string (`str`) is a sequence of text.
- `print` has a parameter `end`. Its default is a new line. `print("hello,", end="")` stops the new line.
- Extra: `sep` changes what goes between values: `print("a", "b", sep="-")` prints `a-b`. This comes from Python's `print` documentation, not the lecture notes.
- To put a quote inside a string, use single quotes outside, or escape it: `print("say \"hi\"")`.
- `\n` is a new line.

### Formatting strings
- An f-string puts variables inside text: `print(f"hello, {name}")`. The `f` before the quote is required.

### More on strings
- Never expect the user to type neatly. Clean their input.
- `.strip()` removes spaces at both ends. `.title()` capitalizes each word.
- You can chain them: `name = input("What's your name? ").strip().title()`.
- Video only: `split` breaks a string into parts. It is not in the written notes for this lecture.

### Integers
- `int` is a whole number. Operators: `+  -  *  /  %` (`%` is modulo, the remainder).
- `input` always gives a string. `"1" + "2"` gives `"12"`. Convert first: `x = int(input("What's x? "))`.
- Functions inside functions run from the inside out: `input` runs first, then `int`.

### Readability
- Several approaches can be correct. Pick the one that is easy to read, and add comments.

### Floats
- A float has a decimal point, like `0.52`. Use `float(input(...))`.
- `round(n)` rounds to the nearest whole number. `round(n, 2)` keeps 2 decimal places.
- `f"{z:,}"` adds commas, like `1,000`. `f"{z:.2f}"` shows 2 decimal places.
- Dividing 2 by 3 gives `0.6666666666666666`. Round it if you want a neat answer.

### Defining your own functions
- `def` creates a function. Python uses indentation to know what is inside it.
- A parameter lets you pass a value in: `def hello(to):`. A default value is used when you pass nothing: `def hello(to="world"):`.
- Put your steps in `main()` and call `main()` at the bottom. Without that call, nothing runs.
- A variable made inside a function only exists there (scope). Pass values in as arguments.

### Returning values
- `return` sends a value back to the code that called the function.
- `print` only shows something. `return` lets the program use the result.

### Not in this lecture
- `if __name__ == "__main__":` is introduced later, in Lecture 5 (Unit Tests). In Lecture 0, just call `main()` at the bottom.

## 1.3 Worked examples

Type each one. Then change something.

**Example 1: clean greeting**

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

- Line 1: `input` shows the question and waits. `.strip().title()` cleans what you typed. So `  ravi kumar ` becomes `Ravi Kumar`.
- Line 2: the f-string puts `name` inside the text.

**Example 2: calculator**

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)
print(f"{z:,}")
print(f"{x / y:.2f}")
```

- `float` turns the typed text into a number that can have decimals.
- `round(x + y)` rounds the sum to a whole number. `:,` adds commas, so 1000 shows as `1,000`.
- `x / y` divides. `:.2f` shows 2 decimal places.

**Example 3: your own function with a default**

```python
def main():
    name = input("What's your name? ")
    hello(name)
    hello()


def hello(to="world"):
    print("hello,", to)


main()
```

- `main` holds the steps. `hello` is our own function.
- `hello(name)` passes the typed name in. `hello()` passes nothing, so the default `"world"` is used.
- The last line starts the program. Delete it and nothing happens.

**Example 4: returning a value**

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```

- `x` is passed to `square` as `n`. `n * n` is sent back with `return`, and `print` shows it.

**Example 5: temperature converter**

```python
def main():
    c = float(input("Celsius: "))
    print(f"Fahrenheit: {to_fahrenheit(c)}")


def to_fahrenheit(c):
    return c * 9 / 5 + 32


main()
```

- `to_fahrenheit` does only the maths, so it is easy to reuse and test.
- Test: `100` should give `212.0`.

**Example 6: student report**

```python
def main():
    name = input("Student name: ").strip().title()
    maths = float(input("Maths marks: "))
    science = float(input("Science marks: "))
    english = float(input("English marks: "))

    total = maths + science + english
    average = total / 3

    print(f"Report for {name}")
    print(f"Total: {total}")
    print(f"Average: {round(average, 1)}")
    print(f"Percentage: {percent(total, 300)}%")


def percent(part, whole):
    return round(part / whole * 100, 1)


main()
```

- The first four lines collect a cleaned name and three marks as floats.
- `total` adds them. `average` divides by 3.
- `percent` is our own function. It takes marks obtained and total marks, and returns the percentage.

## 1.4 Common mistakes

- Forgetting `int()` or `float()`, so `"2" + "3"` becomes `"23"`.
- Forgetting the `f` before an f-string, so you see `{name}` printed literally.
- Writing `print("hello, name")` and expecting the variable.
- Forgetting to call `main()` at the bottom.
- Wrong indentation inside a function.
- Missing a bracket, quote or colon, which gives a syntax error.

## 1.5 Practice questions

### Level 0: Quick quiz
Answer in one or two simple sentences.

**PyQ1.** What is a function?
**PyQ2.** What is the difference between an argument and a side effect?
**PyQ3.** What does `=` do in `name = input("Name: ")`?
**PyQ4.** Why do we write `int(input("x: "))` instead of just `input("x: ")` when doing maths?
**PyQ5.** What is the difference between `print` and `return` inside a function?
**PyQ6.** What is scope?

### Level 1: Reader
Write what you think each program prints. Then run it and check.

**PyR1.**
```python
name = "ada"
print(f"hello, {name.title()}")
```

**PyR2.**
```python
x = 7
y = 2
print(x / y)
print(x + y)
```

**PyR3.**
```python
print("a", "b", "c", sep="-")
print("go", end="!")
print("now")
```

**PyR4.**
```python
x = "2"
y = "3"
print(x + y)
print(int(x) + int(y))
```

**PyR5.**
```python
def double(n):
    return n * 2


print(double(4))
print(double(double(3)))
```

**PyR6.**
```python
z = round(3.14159, 2)
print(z)
print(f"{1234567:,}")
```

**PyR7.**
```python
name = "  grace hopper  "
print(name.strip().title())
```

**PyR8.**
```python
def add(a, b=5):
    return a + b


print(add(3))
print(add(3, 1))
```

**PyR9.**
```python
print("a\nb")
print("say \"hi\"")
```

### Level 2: Fixer
Each program has one bug. Run it, read the error or the wrong output, and fix it.

**PyF1.** Should print the name the user types.
```python
name = input("What's your name? ")
print(f"hello, name")
```

**PyF2.** Should add two numbers, but gives joined text.
```python
x = input("x: ")
y = input("y: ")
print(x + y)
```

**PyF3.** Should print 16, but prints something else.
```python
def square(n):
    n * n


print(square(4))
```

**PyF4.** Gives a NameError.
```python
def main():
    name = input("Name: ")
    hello()


def hello():
    print(f"hello, {name}")


main()
```

**PyF5.** Gives a SyntaxError.
```python
print("hello, world"
```

**PyF6.** Should print the average of a and b, but the answer is wrong.
```python
a = float(input("a: "))
b = float(input("b: "))
average = a + b / 2
print(average)
```

**PyF7.** Gives an AttributeError.
```python
name = input("Name: ").strip.title()
print(name)
```

**PyF8.** Gives a SyntaxError.
```python
def hello(to="world")
    print(f"hello, {to}")


hello()
```

**PyF9.** Gives an IndentationError.
```python
def hello(to="world"):
print(f"hello, {to}")


hello()
```

**PyF10.** Should print 12 and then 13. It crashes.
```python
def triple(n):
    print(n * 3)


result = triple(4)
print(result)
print(result + 1)
```

### Level 3: Builder
Write each program yourself. Use `main()` and your own functions where it makes sense.

**PyB1. Name and age.** Ask for a name and an age. Clean the name. Print: `Ada is 20 years old`.

**PyB2. Circle area.** Ask for a radius (it can be a decimal). Use `3.14159` for pi. Print the area rounded to 2 decimals.

**PyB3. Cube.** Write a function `cube(n)` that returns n times n times n. Use it from `main()`.

**PyB4. Discount.** Write a function `final_price(price, discount)`. The discount is a percentage. Print the final price with 2 decimals.

**PyB5. Name order.** Ask for a first name and a last name. Clean both. Print them as `Last, First`.
Example: `ada` and `lovelace` gives `Lovelace, Ada`.

**PyB6. Average.** Write `average(a, b)` that returns the average of two numbers. In `main`, ask for two decimal numbers and print the average rounded to 1 decimal.
Example: `7` and `8` gives `7.5`.

**PyB7. BMI.** Write `bmi(weight, height)` that returns `weight / (height * height)`. Ask for weight in kg and height in metres. Print the BMI rounded to 1 decimal.
Example: `70` kg and `1.75` m gives `22.9`.

**PyB8. Greeting.** Write `greet(name, greeting="hello")` that prints `greeting, name`. Call it once with only a name, and once with a different greeting.

**PyB9. Simple interest.** Ask for principal, rate (in percent) and years. Interest = principal * rate * years / 100. Total = principal + interest. Print both with commas and 2 decimals.
Example: `10000`, `5`, `3` gives interest `1,500.00` and total `11,500.00`.

### Level 4: Project

**PyP1. Receipt maker.** Ask for an item name, a price and a quantity. Print the subtotal, 5% tax and total. Show money with commas and 2 decimals, like `1,250.50`.

**PyP2. Unit converter.** Write two functions: `km_to_miles` and `kg_to_pounds`. Ask for both values and print both answers.
Hint: 1 km is 0.621371 miles. 1 kg is 2.20462 pounds.

**PyP3. Shop bill.** Write three functions and a `main`:
- `total(price, qty)` returns price times quantity.
- `with_tax(amount)` returns the amount plus 18% tax.
- `main()` asks for a price (decimal) and a quantity (whole number), then prints the amount and the amount with tax, both with commas and 2 decimals.

Example: price `1000` and quantity `3` gives `3,000.00` and `3,540.00`.

**PyP4. Student report.** Without looking at Example 6, build a report for 3 subjects. Show the total, the average, and the percentage out of 300.
Extra: change it to 5 subjects.

### Level 5: Challenge

**PyC1. Initials.** Ask for a full name with two words, like `ada lovelace`. Print `A.L.`
Hint: look up how to take the first letter of a string.
Extra: make it work for names with three words.

**PyC2. Speed calculator.** Write `speed(distance_km, hours)`. Ask for both values and print the speed in km/h with 1 decimal.
Extra: what happens if the user types 0 for hours? Find out, then decide how to handle it.

### Hints for the official Problem Set 0 (hints only)
- Do the official problems yourself. CS50's academic honesty rules do not allow copying solutions.
- Write the steps as comments first (pseudocode), then turn each comment into code.
- For text problems, think about which string method could change the text.
- For maths problems, remember `input` gives a string, so convert it first.
- Test each function with simple values before using real ones.
- When stuck, ask for a hint with your code and the error message.

---

# PART 2: AI SEARCH

## 2.1 Video map (CS50 AI Lecture 0, about 1h 49m)

The official course page lists these Week 0 topics (confirmed): search problems, depth-first search, breadth-first search, greedy best-first search, A* search, minimax, alpha-beta pruning.

The Google summary adds depth-limited minimax. That is not in the official topic list I checked, so treat it as unverified. All timestamps from that summary are unverified. Check them in the video.

| Time (unverified) | Topic |
|---|---|
| 0:00 | Introduction |
| 3:14 | Search |
| 14:17 | Solving search problems |
| 25:57 | Depth-first search |
| 28:30 | Breadth-first search |
| 54:29 | Greedy best-first search |
| 1:05:15 | A* search |
| 1:12:01 | Adversarial search |
| 1:14:09 | Minimax |
| 1:36:17 | Alpha-beta pruning |
| 1:45:28 | Depth-limited minimax |

## 2.2 Notes

### What is search?
Search means finding a series of actions that takes an agent from a start to a goal, like solving a maze or a puzzle.

### Parts of a search problem
- **Agent:** the thing that looks at its surroundings and acts.
- **State:** one situation the agent can be in.
- **Initial state:** where we start.
- **Actions:** the moves possible in a state.
- **Transition model:** which state we reach after an action.
- **Goal test:** a check to see if we reached the goal.
- **Path cost:** the price of a path, such as distance or time.
- **Solution:** a path from start to goal. An **optimal** solution has the lowest path cost.

### How a search runs
1. Put the start in the **frontier** (the nodes waiting to be explored).
2. Take one out. If it is the goal, stop.
3. Otherwise add its neighbours to the frontier.
4. Repeat until the frontier is empty.

Keep an **explored set** so you never visit a state twice. Without it, the search can loop forever.

### Uninformed search (no guess about the goal)

| Search | Frontier | Idea | Good / bad |
|---|---|---|---|
| Depth-first (DFS) | stack (last in, first out) | go deep, backtrack at a dead end | uses little memory, may not find the shortest path |
| Breadth-first (BFS) | queue (first in, first out) | explore level by level | finds the path with the fewest steps, uses more memory |

### Informed search (uses a heuristic)
A **heuristic** is a rule-of-thumb estimate of how close a state is to the goal.
- **Greedy best-first:** picks the node that looks closest to the goal. Fast, but it can be fooled into a longer route.
- **A\* search:** picks the node with the smallest `cost so far + heuristic guess`. It finds the best path if the heuristic never overestimates the real distance (admissible). The lecture also asks for it to be consistent.
- When two options tie, the tie-break rule changes how many nodes A* explores. Task PyC4 below lets you see this.

### Adversarial search (games with an opponent)
- **Minimax:** MAX wants the highest score and MIN wants the lowest. Each assumes the other plays perfectly.
- **Alpha-beta pruning:** skips branches that cannot change the final answer. It gives the same result as minimax with less work.
- **Depth-limited minimax (unverified in the official topic list):** stop at a set depth and use an evaluation function to estimate the score. Used when the game is too big to search fully.

### Common mistakes
- Forgetting the explored set, which causes infinite loops.
- Using `pop()` when you want a queue. It takes the last item (stack). `pop(0)` takes the first (queue).
- Appending a neighbour when you should append the whole path.
- Thinking DFS always gives the shortest path. It does not.
- Not switching MAX and MIN at each level.

## 2.3 Practice questions

Unless a question gives its own, use this graph:
```python
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": [],
}
```

### Level 0: Quick quiz

**AiQ1.** What is a state?
**AiQ2.** What is the frontier, and why do we also keep an explored set?
**AiQ3.** What is the difference between depth-first and breadth-first search?
**AiQ4.** What is a heuristic? What two things does A* add together?
**AiQ5.** In minimax, what do MAX and MIN try to do?
**AiQ6.** What does alpha-beta pruning do?

### Level 1: Reader

**AiR1. Stack and queue.** What is printed?
```python
frontier = ["A", "B", "C"]
print(frontier.pop())
print(frontier.pop(0))
print(frontier)
```

**AiR2. Visiting order.** Predict both lines, then run it.
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}


def order(start, use_stack):
    frontier = [start]
    seen = []
    while frontier:
        node = frontier.pop() if use_stack else frontier.pop(0)
        seen.append(node)
        for n in graph[node]:
            frontier.append(n)
    return seen


print(order("A", True))
print(order("A", False))
```

**AiR3. Trace by hand.** Start at `S`. Each node is visited only once (use an explored set).
```python
graph = {"S": ["A", "B"], "A": ["C"], "B": ["C"], "C": []}
```
In what order are nodes visited by (1) breadth-first search, taking from the front, and (2) depth-first search, taking from the end, with neighbours added in the order listed?

**AiR4. Greedy or A\*?** Two nodes wait in the frontier.
- Node X: cost so far 2, heuristic guess 3
- Node Y: cost so far 8, heuristic guess 2

Which does greedy best-first pick? Which does A* pick?

**AiR5. Greedy or A\*, again.** Each node shows (cost so far, guess).
- P: (5, 4)
- Q: (3, 7)
- R: (9, 1)

Which does greedy pick? Which does A* pick?

**AiR6. Minimax by hand.** The root is MAX, the next level is MIN. Leaves are scores.
```
tree = [[3, 5], [2, 9]]
```
What is the value of the root?

**AiR7. Minimax by hand.**
```
tree = [[4, 7], [6, 1], [5, 8]]
```
What is the value of the root?

**AiR8. Three levels.** The root is MAX, the next level is MIN, and the level above the leaves is MAX.
```
tree = [[[3, 5], [2, 9]], [[0, 1], [7, 4]]]
```
What is the value of the root?

**AiR9. Pruning.** Alpha-beta runs on this tree. The root is MAX, the next level is MIN, and leaves are read left to right.
```
tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
```
Which leaves are never looked at?

### Level 2: Fixer

**AiF1. Runs forever.** Run it and press Ctrl+C to stop. Why does it never finish? Fix it.
```python
graph = {"A": ["B"], "B": ["C", "A"], "C": []}


def dfs(start, goal):
    frontier = [[start]]
    while frontier:
        path = frontier.pop()
        state = path[-1]
        if state == goal:
            return path
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(dfs("A", "C"))
```

**AiF2. Not really breadth-first.** This should find the shortest path from A to G, but it does not.
```python
graph = {"A": ["C", "B"], "B": ["D"], "C": ["G"], "D": ["G"], "G": []}


def bfs(start, goal):
    frontier = [[start]]
    while frontier:
        path = frontier.pop()
        state = path[-1]
        if state == goal:
            return path
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(bfs("A", "G"))
```

**AiF3. Wrong minimax.** For `[[3, 5], [2, 9]]` the answer should be 3. Find out why it is not.
```python
def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, is_max) for child in node]
    return max(scores) if is_max else min(scores)


print(minimax([[3, 5], [2, 9]], True))
```

**AiF4. Always returns None.** The answer should be a path from A to D.
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def bfs(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        explored.add(state)
        if state in explored:
            continue
        if state == goal:
            return path
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(bfs("A", "D"))
```

**AiF5. Crashes.** It gives a TypeError.
```python
def minimax(node, is_max):
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


print(minimax([[3, 5], [2, 9]], True))
```

**AiF6. Returns the wrong thing.** This should return the full path, like `['A', 'B', 'D']`, but it returns just the goal.
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}


def bfs(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(n)
    return None


print(bfs("A", "D"))
```

**AiF7. Swapped.** For `[[3, 5], [2, 9]]` the answer should be 3. This gives a different answer.
```python
def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, not is_max) for child in node]
    return min(scores) if is_max else max(scores)


print(minimax([[3, 5], [2, 9]], True))
```

**AiF8. Not A\*.** This is supposed to be A*, but it behaves like greedy best-first. Why? Fix it.
```python
roads = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "F": 3},
    "E": {"C": 10, "F": 2},
    "F": {"D": 3, "E": 2, "G": 6},
    "G": {"F": 6},
}
guess = {"A": 15, "B": 12, "C": 1, "D": 8, "E": 7, "F": 5, "G": 0}


def a_star(start, goal, h, roads):
    frontier = [(h[start], 0, [start])]
    explored = set()
    while frontier:
        frontier.sort()
        _, cost, path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path, cost
        if state in explored:
            continue
        explored.add(state)
        for n, c in roads[state].items():
            new_cost = cost + c
            frontier.append((h[n], new_cost, path + [n]))
    return None, None


print(a_star("A", "G", guess, roads))
```
Here the guess for C is deliberately too low. The best path costs 18.

**AiF9. Never stops early.** This is supposed to stop at a given depth and guess the score. It never stops early. Why? Fix it.
```python
def flatten(node):
    if isinstance(node, int):
        return [node]
    nums = []
    for child in node:
        nums += flatten(child)
    return nums


def depth_limited(node, is_max, depth):
    if isinstance(node, int):
        return node
    if depth == 0:
        nums = flatten(node)
        return sum(nums) / len(nums)
    scores = [depth_limited(c, not is_max, depth) for c in node]
    return max(scores) if is_max else min(scores)


deep = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
print(depth_limited(deep, True, 1))
```
With a depth of 1 the answer should be 5.75.

### Level 3: Builder

**AiB1. Path cost.** Here are roads with distances.
```python
roads = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "F": 3},
    "E": {"C": 10, "F": 2},
    "F": {"D": 3, "E": 2, "G": 6},
    "G": {"F": 6},
}
```
Write `path_cost(path, roads)` that adds up the distances along a path.
Test: `["A", "B", "D", "F", "G"]` should give 18.

**AiB2. Best move.** Write `best_move(tree)` for a tree like `[[3, 12, 8], [2, 4, 6], [14, 5, 2]]`. MAX picks one of the groups. Return the index of the best group and its score. For this tree the answer is group 0 with score 3.
Hint: use minimax for each group, where the next player is MIN.

**AiB3. Distance guess.** On a grid, a cell is `(row, column)`. Write `heuristic(a, b)` that returns the number of steps between two cells if there were no walls.
Test: `(0, 0)` and `(3, 4)` should give 7.

**AiB4. Count the work.** Change a BFS function so it returns the path and also how many states it explored.

**AiB5. Grid neighbours.** Write `neighbours(cell, rows, cols)`. Return the cells above, below, left and right that are inside the grid, in that order.
Example: `neighbours((0, 0), 3, 3)` gives `[(1, 0), (0, 1)]`, and `neighbours((1, 1), 3, 3)` gives `[(0, 1), (2, 1), (1, 0), (1, 2)]`.

**AiB6. Depth-first search.** Write `dfs(graph, start, goal)` that returns a path as a list, using a stack and an explored set. Return `None` if there is no path.
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(dfs(graph, "A", "D"))
```
Take paths from the end of the frontier and add neighbours in the order listed.

**AiB7. Number of steps.** Write `shortest_steps(graph, start, goal)` that returns the fewest steps from start to goal using breadth-first search, or `None` if there is no path.
Using the graph above: `shortest_steps(graph, "A", "D")` gives `2`, and `shortest_steps(graph, "D", "A")` gives `None`.

**AiB8. Pick like A\*.** Write `choose_best(options)`. Each option is `(name, cost_so_far, guess)`. Return the name with the smallest `cost_so_far + guess`.
Example: `choose_best([("P", 5, 4), ("Q", 3, 7), ("R", 9, 1)])` gives `"P"`.

### Level 4: Project

**AiP1. Maze solver.** Find the shortest path through this maze with BFS. `S` is the start, `G` is the goal, `#` is a wall, `.` is open.
```python
maze = [
    "S.#.....",
    ".##.###.",
    "....#...",
    ".####.#.",
    "......#G",
]
```
Goals:
- Find S and G in the maze.
- Move up, down, left, right. Do not walk through walls or off the grid.
- Print the number of steps (it is 15) and how many cells you explored.
- Print the maze again with `*` on the path.

**AiP2. Nim bot.** There is a pile of stones. Two players take turns taking 1, 2 or 3 stones. The player who takes the last stone wins. Write `best_take(stones)` that says how many to take.
Hint: a position is winning if you can move to a position where the other player is losing. This is minimax with only two scores: win and lose.
Test: with 5 stones you should take 1. What can you do with 8 stones?

**AiP3. Number puzzle.** You start at the number 1. You may do one of two actions: add 1, or multiply by 2. Write `fewest_steps(goal)` that uses BFS to find the fewest actions needed to reach the goal.
- `fewest_steps(1)` gives `0`
- `fewest_steps(10)` gives `4`
- `fewest_steps(15)` gives `6`

Before you code, write down: what is a state? what are the actions? what is the goal test? Do not explore numbers bigger than the goal.

### Level 5: Challenge

**AiC1. A\* on the maze.** Solve the maze from AiP1 with A*, using your Manhattan heuristic from AiB3. Count how many cells BFS explored and how many A* explored. Which explored fewer, and why?
Hint: when two options have the same total, prefer the one with the larger cost so far.

**AiC2. Alpha-beta.** Write minimax with alpha-beta pruning. Count how many leaves it looks at and compare with plain minimax on `[[3, 12, 8], [2, 4, 6], [14, 5, 2]]`. It should check fewer than 9.

**AiC3. Your own idea.** Pick a puzzle or game (a tiny sliding puzzle, a word ladder, a bigger Nim) and solve it with search. Write what the states, actions and goal are before you code.

**AiC4. Open grid.** Run your AiC1 solution on this open grid and compare the counts.
```python
open_grid = [
    "S.......",
    "........",
    "...##...",
    "........",
    ".......G",
]
```
Then switch your tie-break back (smaller cost first) and see what changes.

### Hints for the official Project 0 (hints only)
The official CS50 AI Project 0 has two parts: Degrees and Tic-Tac-Toe. Do them yourself. Copying solutions breaks CS50's academic honesty rules.
- **Degrees:** think of people as states and shared movies as the actions. Which search guarantees the fewest steps?
- **Tic-Tac-Toe:** write small helper functions first (whose turn, possible moves, who won, is the game over). When you try a move, work on a copy so the real board is not changed.
- Test each small function alone before combining them.

---

# ANSWER KEY

Stop. Only scroll down after you have tried the questions. Seeing the answer too early takes away the learning.

---

# PART 1 ANSWERS

## Level 0: Quick quiz
- **PyQ1.** A function is an action (a verb) that a program can run, like `print`. Python has built-in ones, and you can write your own with `def`.
- **PyQ2.** An argument is the input you give a function. A side effect is what the function does, like showing text on the screen.
- **PyQ3.** It stores the value on the right inside the variable on the left.
- **PyQ4.** `input` always gives text (a string). `int()` or `float()` turns it into a number so you can do maths.
- **PyQ5.** `print` only shows something on the screen. `return` sends a value back to the code that called the function so it can be used.
- **PyQ6.** Scope is where a variable can be used. A variable made inside a function only exists inside that function.

## Level 1: Reader
- **PyR1.** `hello, Ada`
- **PyR2.** `3.5` then `9`
- **PyR3.** `a-b-c` then `go!now` (`end="!"` stops the new line)
- **PyR4.** `23` then `5` (strings join, numbers add)
- **PyR5.** `8` then `12`
- **PyR6.** `3.14` then `1,234,567`
- **PyR7.** `Grace Hopper`
- **PyR8.** `8` then `4`
- **PyR9.**
```
a
b
say "hi"
```

## Level 2: Fixer
- **PyF1.** The f-string needs braces: `print(f"hello, {name}")`.
- **PyF2.** Convert with `int()`: `x = int(input("x: "))` and the same for `y`.
- **PyF3.** The function has no `return`, so it gives back `None`. Write `return n * n`.
- **PyF4.** `name` only exists inside `main` (scope). Pass it in: `hello(name)` and `def hello(name):`.
- **PyF5.** The closing bracket is missing: `print("hello, world")`.
- **PyF6.** Division happens first. Use `(a + b) / 2`.
- **PyF7.** `strip` needs brackets to be called: `.strip().title()`.
- **PyF8.** A function line must end with a colon: `def hello(to="world"):`.
- **PyF9.** The line inside the function must be indented: four spaces before `print`.
- **PyF10.** The function prints but does not return, so `result` is `None`, and `None + 1` fails with a TypeError. Fix: use `return n * 3` instead of `print(n * 3)`. Then it prints `12` and `13`.

## Level 3: Builder (sample solutions, yours may look different)

**PyB1**
```python
name = input("Name: ").strip().title()
age = int(input("Age: "))
print(f"{name} is {age} years old")
```

**PyB2**
```python
radius = float(input("Radius: "))
area = 3.14159 * radius * radius
print(f"Area: {round(area, 2)}")
```

**PyB3**
```python
def main():
    n = int(input("n: "))
    print(cube(n))


def cube(n):
    return n * n * n


main()
```

**PyB4**
```python
def main():
    price = float(input("Price: "))
    discount = float(input("Discount %: "))
    print(f"Final price: {final_price(price, discount):.2f}")


def final_price(price, discount):
    return price - price * discount / 100


main()
```

**PyB5**
```python
first = input("First name: ").strip().title()
last = input("Last name: ").strip().title()
print(f"{last}, {first}")
```

**PyB6**
```python
def main():
    a = float(input("a: "))
    b = float(input("b: "))
    print(round(average(a, b), 1))


def average(a, b):
    return (a + b) / 2


main()
```
Common mistake: writing `a + b / 2`. Division happens first, so you need brackets.

**PyB7**
```python
def main():
    weight = float(input("Weight in kg: "))
    height = float(input("Height in metres: "))
    print(round(bmi(weight, height), 1))


def bmi(weight, height):
    return weight / (height * height)


main()
```

**PyB8**
```python
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")


greet("Ada")
greet("Ada", "good morning")
```
Prints `hello, Ada` and `good morning, Ada`.

**PyB9**
```python
def main():
    principal = float(input("Principal: "))
    rate = float(input("Rate %: "))
    years = float(input("Years: "))
    interest = principal * rate * years / 100
    total = principal + interest
    print(f"Interest: {interest:,.2f}")
    print(f"Total: {total:,.2f}")


main()
```

## Level 4: Project (sample solutions)

**PyP1**
```python
def main():
    item = input("Item: ").strip().title()
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    subtotal = price * qty
    tax = subtotal * 0.05
    total = subtotal + tax

    print(f"Item: {item} x {qty}")
    print(f"Subtotal: {subtotal:,.2f}")
    print(f"Tax (5%): {tax:,.2f}")
    print(f"Total: {total:,.2f}")


main()
```

**PyP2**
```python
def km_to_miles(km):
    return km * 0.621371


def kg_to_pounds(kg):
    return kg * 2.20462


def main():
    km = float(input("Kilometres: "))
    kg = float(input("Kilograms: "))
    print(f"{km} km = {km_to_miles(km):.2f} miles")
    print(f"{kg} kg = {kg_to_pounds(kg):.2f} pounds")


main()
```

**PyP3**
```python
def main():
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    amount = total(price, qty)
    print(f"Amount: {amount:,.2f}")
    print(f"With 18% tax: {with_tax(amount):,.2f}")


def total(price, qty):
    return price * qty


def with_tax(amount):
    return amount * 1.18


main()
```

**PyP4**
This is the same as Example 6 in the worked examples. For 5 subjects, add two more `input` lines, add them to `total`, divide by 5, and use 500 as the whole.

## Level 5: Challenge (sample solutions)

**PyC1**
```python
def main():
    full = input("Full name: ").strip().title()
    first, last = full.split(" ")
    print(f"{first[0]}.{last[0]}.")


main()
```
For more than two words, split into a list and take the first letter of each word in a loop (you learn loops in Lecture 2).

**PyC2**
```python
def speed(distance_km, hours):
    return distance_km / hours


def main():
    distance = float(input("Distance in km: "))
    hours = float(input("Hours: "))
    print(f"Speed: {speed(distance, hours):.1f} km/h")


main()
```
With `0` hours Python raises a `ZeroDivisionError`. You will learn how to handle errors like this in Lecture 3 (Exceptions). Conditionals such as `if hours == 0:` come in Lecture 1.

---

# PART 2 ANSWERS

## Level 0: Quick quiz
- **AiQ1.** A state is one situation (configuration) the agent can be in, like a position in a maze.
- **AiQ2.** The frontier holds the nodes (or paths) waiting to be explored. The explored set remembers visited states so we do not visit them again and do not loop forever.
- **AiQ3.** Depth-first uses a stack (last in, first out) and goes deep along one path before backtracking. Breadth-first uses a queue (first in, first out) and explores level by level, so it finds the path with the fewest steps.
- **AiQ4.** A heuristic is a rule-of-thumb estimate of how close a state is to the goal. A* adds the cost so far to the heuristic guess.
- **AiQ5.** MAX tries to get the highest score. MIN tries to get the lowest score. Each assumes the other plays perfectly.
- **AiQ6.** It skips branches that cannot change the final answer, so minimax gives the same result with less work.

## Level 1: Reader
- **AiR1.** `C`, then `A`, then `['B']`. `pop()` takes the last item (stack). `pop(0)` takes the first (queue).
- **AiR2.** `['A', 'C', 'E', 'B', 'D']` for the stack (depth-first), then `['A', 'B', 'C', 'D', 'E']` for the queue (breadth-first).
- **AiR3.**
  1. Breadth-first: `S, A, B, C`
  2. Depth-first: `S, B, C, A`

  Why for depth-first: after S, the frontier holds A then B. The stack takes B first. B adds C, so C is taken next. Then A is taken, and its neighbour C was already visited.
- **AiR4.** Greedy picks Y (smallest guess, 2). A* picks X, because 2 + 3 = 5 is smaller than 8 + 2 = 10.
- **AiR5.** Greedy picks R (smallest guess, 1). A* picks P, because the totals are P = 9, Q = 10 and R = 10.
- **AiR6.** `3`. MIN of [3, 5] is 3, MIN of [2, 9] is 2, MAX of 3 and 2 is 3.
- **AiR7.** `5`. The MINs are 4, 1 and 5, and MAX of those is 5.
- **AiR8.** `5`.
  - First group: MAX of (3, 5) is 5 and MAX of (2, 9) is 9, so MIN is 5.
  - Second group: MAX of (0, 1) is 1 and MAX of (7, 4) is 7, so MIN is 1.
  - The root is MAX of 5 and 1, which is 5.
- **AiR9.** Leaves `4` and `6` are skipped. After the first group MAX already has 3. In the second group MIN sees 2 first, which is already worse than 3, so the rest of that group cannot matter. 7 of 9 leaves are checked.

## Level 2: Fixer (each fix is a full program you can run)

**AiF1.** Nothing remembers visited states, so it bounces between A and B forever. Add an explored set.
```python
graph = {"A": ["B"], "B": ["C", "A"], "C": []}


def dfs(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop()
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(dfs("A", "C"))
```
Prints `['A', 'B', 'C']`.

**AiF2.** `pop()` takes the newest path, which is depth-first. Breadth-first needs `frontier.pop(0)`.
```python
graph = {"A": ["C", "B"], "B": ["D"], "C": ["G"], "D": ["G"], "G": []}


def bfs(start, goal):
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(bfs("A", "G"))
```
Prints `['A', 'C', 'G']`. The buggy version printed `['A', 'B', 'D', 'G']`, which is longer.

**AiF3.** The children are called with `is_max` instead of the opposite. Players must switch each level. Use `not is_max`.
```python
def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


print(minimax([[3, 5], [2, 9]], True))
```
Prints `3`.

**AiF4.** The state is added to `explored` before the check, so every state looks already visited. Check first, then add.
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def bfs(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(bfs("A", "D"))
```
Prints `['A', 'B', 'D']`.

**AiF5.** There is no base case. When `node` is a number, the code tries to loop over it. Add a check at the top.
```python
def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


print(minimax([[3, 5], [2, 9]], True))
```

**AiF6.** The code adds `n` instead of the whole path. Append `path + [n]`.
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": [], "D": []}


def bfs(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(path + [n])
    return None


print(bfs("A", "D"))
```
Prints `['A', 'B', 'D']`.

**AiF7.** `min` and `max` are swapped. MAX should take `max` and MIN should take `min`. The buggy version printed `5`.
```python
def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


print(minimax([[3, 5], [2, 9]], True))
```

**AiF8.** The sort key uses only the guess `h[n]`. A* needs cost so far plus guess. With the low guess for C, greedy takes the longer route through C and E (cost 20).
```python
roads = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "F": 3},
    "E": {"C": 10, "F": 2},
    "F": {"D": 3, "E": 2, "G": 6},
    "G": {"F": 6},
}
guess = {"A": 15, "B": 12, "C": 1, "D": 8, "E": 7, "F": 5, "G": 0}


def a_star(start, goal, h, roads):
    frontier = [(h[start], 0, [start])]
    explored = set()
    while frontier:
        frontier.sort()
        _, cost, path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path, cost
        if state in explored:
            continue
        explored.add(state)
        for n, c in roads[state].items():
            new_cost = cost + c
            frontier.append((new_cost + h[n], new_cost, path + [n]))
    return None, None


print(a_star("A", "G", guess, roads))
```
Prints `(['A', 'B', 'D', 'F', 'G'], 18)`.

Note: a low guess like this one is still allowed, because it never overestimates the real distance, so A* stays correct. Greedy has no such protection, because it ignores the cost so far. A guess that is too high would be the real problem for A*.

**AiF9.** The depth is never reduced in the recursive call, so `depth == 0` is never reached. Use `depth - 1`.
```python
def flatten(node):
    if isinstance(node, int):
        return [node]
    nums = []
    for child in node:
        nums += flatten(child)
    return nums


def depth_limited(node, is_max, depth):
    if isinstance(node, int):
        return node
    if depth == 0:
        nums = flatten(node)
        return sum(nums) / len(nums)
    scores = [depth_limited(c, not is_max, depth - 1) for c in node]
    return max(scores) if is_max else min(scores)


deep = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
print(depth_limited(deep, True, 1))
```
Prints `5.75`. A full minimax on the same tree gives `5`, so the depth-1 guess is close.

## Level 3: Builder (sample solutions)

**AiB1**
```python
roads = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "F": 3},
    "E": {"C": 10, "F": 2},
    "F": {"D": 3, "E": 2, "G": 6},
    "G": {"F": 6},
}


def path_cost(path, roads):
    total = 0
    for i in range(len(path) - 1):
        total += roads[path[i]][path[i + 1]]
    return total


print(path_cost(["A", "B", "D", "F", "G"], roads))
```
Prints `18`.

**AiB2**
```python
def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


def best_move(tree):
    best_index = 0
    best_score = float("-inf")
    for i, child in enumerate(tree):
        score = minimax(child, False)     # the next player is MIN
        if score > best_score:
            best_score = score
            best_index = i
    return best_index, best_score


print(best_move([[3, 12, 8], [2, 4, 6], [14, 5, 2]]))
```
Prints `(0, 3)`.

**AiB3**
```python
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


print(heuristic((0, 0), (3, 4)))
```
Prints `7`.

**AiB4**
```python
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}


def bfs_count(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path, len(explored)
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(path + [n])
    return None, len(explored)


print(bfs_count("A", "D"))
```
Prints `(['A', 'B', 'D'], 3)`. The explored states are A, B and C.

**AiB5**
```python
def neighbours(cell, rows, cols):
    r, c = cell
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            result.append((nr, nc))
    return result


print(neighbours((0, 0), 3, 3))
print(neighbours((1, 1), 3, 3))
```

**AiB6**
```python
def dfs(graph, start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop()           # take from the end (stack)
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(path + [n])
    return None


graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(dfs(graph, "A", "D"))
```
Prints `['A', 'C', 'D']`, because the stack takes C before B. If you add neighbours in a different order you may get `['A', 'B', 'D']`. Both are valid paths.

**AiB7**
```python
def shortest_steps(graph, start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)          # take from the front (queue)
        state = path[-1]
        if state == goal:
            return len(path) - 1
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            frontier.append(path + [n])
    return None


graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
print(shortest_steps(graph, "A", "D"))
print(shortest_steps(graph, "D", "A"))
```
Prints `2` then `None`.

**AiB8**
```python
def choose_best(options):
    best_name = None
    best_total = float("inf")
    for name, cost, guess in options:
        total = cost + guess
        if total < best_total:
            best_total = total
            best_name = name
    return best_name


print(choose_best([("P", 5, 4), ("Q", 3, 7), ("R", 9, 1)]))
```
Prints `P`.

## Level 4: Project (sample solutions)

**AiP1: Maze solver (BFS)**
```python
maze = [
    "S.#.....",
    ".##.###.",
    "....#...",
    ".####.#.",
    "......#G",
]


def find(maze, char):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == char:
                return (r, c)


def neighbours(maze, cell):
    r, c = cell
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            result.append((nr, nc))
    return result


def bfs(maze):
    start, goal = find(maze, "S"), find(maze, "G")
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        cell = path[-1]
        if cell == goal:
            return path, len(explored)
        if cell in explored:
            continue
        explored.add(cell)
        for n in neighbours(maze, cell):
            frontier.append(path + [n])
    return None, len(explored)


path, count = bfs(maze)
print("steps:", len(path) - 1)
print("cells explored:", count)

grid = [list(row) for row in maze]
for r, c in path[1:-1]:
    grid[r][c] = "*"
for row in grid:
    print("".join(row))
```
Prints 15 steps and 26 explored cells (counted when a cell is first expanded). Your count may differ by a little depending on how you count.

**AiP2: Nim bot**
```python
def can_win(stones):
    # True if the player to move can force a win
    if stones == 0:
        return False      # the other player took the last stone
    for take in [1, 2, 3]:
        if take <= stones and not can_win(stones - take):
            return True
    return False


def best_take(stones):
    for take in [1, 2, 3]:
        if take <= stones and not can_win(stones - take):
            return take
    return 1              # losing anyway, take any legal amount


print(best_take(5))
print(best_take(8))
```
Prints `1` and `1`. With 5 stones, taking 1 leaves 4, which is a losing pile for the other player. With 8 stones there is no winning move, because every move leaves 7, 6 or 5, and each of those lets the other player win. Pattern: if the pile is a multiple of 4, the player to move loses against perfect play.

**AiP3: Number puzzle**
A state is the current number. The actions are add 1 or multiply by 2. The goal test is whether the number equals the goal.
```python
def fewest_steps(goal):
    frontier = [(1, 0)]                 # (number, steps so far)
    seen = {1}
    while frontier:
        number, steps = frontier.pop(0)
        if number == goal:
            return steps
        for nxt in [number + 1, number * 2]:
            if nxt <= goal and nxt not in seen:
                seen.add(nxt)
                frontier.append((nxt, steps + 1))
    return None


print(fewest_steps(1))
print(fewest_steps(10))
print(fewest_steps(15))
```
Prints `0`, `4` (1, 2, 4, 5, 10) and `6` (1, 2, 3, 6, 7, 14, 15).

## Level 5: Challenge (sample solutions)

**AiC1 and AiC4: A\* compared with BFS**
```python
maze = [
    "S.#.....",
    ".##.###.",
    "....#...",
    ".####.#.",
    "......#G",
]

open_grid = [
    "S.......",
    "........",
    "...##...",
    "........",
    ".......G",
]


def find(maze, char):
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == char:
                return (r, c)


def neighbours(maze, cell):
    r, c = cell
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]) and maze[nr][nc] != "#":
            result.append((nr, nc))
    return result


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs(maze):
    start, goal = find(maze, "S"), find(maze, "G")
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)
        cell = path[-1]
        if cell == goal:
            return len(path) - 1, len(explored)
        if cell in explored:
            continue
        explored.add(cell)
        for n in neighbours(maze, cell):
            frontier.append(path + [n])


def astar(maze):
    start, goal = find(maze, "S"), find(maze, "G")
    frontier = [(heuristic(start, goal), 0, [start])]
    best_cost = {}
    count = 0
    while frontier:
        # smallest total first; on a tie, prefer the larger cost so far
        frontier.sort(key=lambda item: (item[0], -item[1]))
        _, cost, path = frontier.pop(0)
        cell = path[-1]
        if cell == goal:
            return len(path) - 1, count
        if cell in best_cost and best_cost[cell] <= cost:
            continue
        best_cost[cell] = cost
        count += 1
        for n in neighbours(maze, cell):
            new_cost = cost + 1
            frontier.append((new_cost + heuristic(n, goal), new_cost, path + [n]))


for name, m in [("maze", maze), ("open grid", open_grid)]:
    print(name, "BFS (steps, explored):", bfs(m), "A* (steps, explored):", astar(m))
```
With my counting: the maze gives BFS `(15, 26)` and A* `(15, 20)`. The open grid gives BFS `(11, 37)` and A* `(11, 11)`. Both find a shortest path, but A* explores fewer cells because the heuristic points it toward the goal.

The tie-break matters. If A* prefers the smaller cost on ties, it explores cells in a more breadth-first order. When I ran that version, A* explored the same 26 cells as BFS in the maze and 37 in the open grid, so it gave no saving. Many cells have the same total on an open grid, so how you break ties decides how much you save.

**AiC2: Alpha-beta**
```python
visited = 0


def minimax(node, is_max):
    if isinstance(node, int):
        return node
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


def alphabeta(node, is_max, alpha, beta):
    global visited
    if isinstance(node, int):
        visited += 1
        return node
    if is_max:
        best = float("-inf")
        for child in node:
            best = max(best, alphabeta(child, False, alpha, beta))
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, alphabeta(child, True, alpha, beta))
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best


tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
print(minimax(tree, True))
print(alphabeta(tree, True, float("-inf"), float("inf")))
print("leaves checked:", visited, "of 9")
```
Prints `3`, `3` and `leaves checked: 7 of 9`. Once MIN finds a 2 in the second group, MAX already has 3 from the first group, so the rest of that group cannot matter and is skipped.

**AiC3** There is no single answer. Check your own work like this:
- Did you write down the states, actions and goal first?
- Does your search avoid visiting the same state twice?
- Did you test on a tiny case you can solve by hand?

---

# SCORE SHEET

| Part | Level | Questions | Your correct count |
|---|---|---|---|
| 1 | 0: Quiz | 6 | |
| 1 | 1: Reader | 9 | |
| 1 | 2: Fixer | 10 | |
| 1 | 3: Builder | 9 | |
| 1 | 4: Project | 4 | |
| 1 | 5: Challenge | 2 | |
| 2 | 0: Quiz | 6 | |
| 2 | 1: Reader | 9 | |
| 2 | 2: Fixer | 9 | |
| 2 | 3: Builder | 8 | |
| 2 | 4: Project | 3 | |
| 2 | 5: Challenge | 4 | |

For each part:
- **80% or more:** well done. Move on to the next lecture and make your own versions of the programs.
- **50% to 79%:** go back to the video section for each wrong answer, then retry only those questions.
- **Below 50%:** rewatch the lecture slowly, pause often and type along. Then try again.

---

# WHAT I FIXED

Compared with the three drafts you pasted:

1. **Merged three overlapping drafts into one file** and removed the duplicate questions.
2. **Restored cut-off parts.** One draft's answer key stopped in the middle of a sentence at the second answer of the AI "Fix the bug" section, and another stopped in the middle of the last fix. Everything is rebuilt in full.
3. **Corrected a wrong claim about A\*.** The old challenge implied A* always explores fewer cells than BFS. When I ran it, the maze gave the same count (26) for both with the default tie-break. I changed the code to prefer the larger cost on ties, which gives 26 vs 20 on the maze and 37 vs 11 on an open grid, and I added a note about why.
4. **Fixed a confusing question.** The old "print vs return" question said it should print 12 then 13 but its fix only printed 13. The question now prints both values, and the answer explains the `None + 1` crash.
5. **Made every answer runnable.** Several "fix" answers were short fragments. Each is now a full program, and I ran them to confirm the printed outputs shown.
6. **Marked timestamps honestly.** Only 0:00, 3:19, 4:00 and 5:06 of the Python lecture were confirmed. All other times, and all AI lecture times, are marked unverified.
7. **Marked things that are not in the official notes.** `split` and `sep` are not in the written Lecture 0 notes (`split` is video-only, `sep` comes from the Python `print` docs). Depth-limited minimax is not in the official Week 0 topic list I checked, so it is marked unverified.
8. **Confirmed that `if __name__ == "__main__":` belongs to Lecture 5**, so it is not used in Lecture 0 code.
9. **Added missing Lecture 0 topics** from the official notes: bugs, comments, pseudocode, readability, the `%` operator, and a note on `end`.
10. **Used the right course wording.** CS50P calls them "Problem Sets". CS50 AI calls them "Projects". Hints for the official ones are hints only.
11. **Cleaned the code style** (two blank lines between functions) and made the explanations simpler.

Still unverified: all timestamps except the four above, and the video length of 1h 45m 38s for the Python lecture (the video page says about 1h 45m).

---

# SOURCES

- [CS50P Lecture 0 official notes](https://cs50.harvard.edu/python/notes/0/)
- [CS50P Lecture 5 official notes (Unit Tests, where `__name__` is used)](https://cs50.harvard.edu/python/notes/5)
- [CS50 AI Week 0 course page (topics and projects)](https://cs50.harvard.edu/ai/2023/weeks/0)
- [CS50 AI projects list (Degrees, Tic-Tac-Toe)](https://cs50.harvard.edu/summer/ai/2020/projects)
- [CS50 video player, Python Lecture 0](https://video.cs50.io/OvKCESUCWII)
- [Lecture 0 summary, rosetta.to (video length)](https://rosetta.to/u/cs50/cs50p-lecture-0-functions-variables)
- [Python docs: `print`](https://docs.python.org/3/library/functions.html#print)
- [CS50P academic honesty policy](https://cs50.harvard.edu/python/honesty/)