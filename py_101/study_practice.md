# Exercise 1
Descibe this code:

```python
def replace(string, value):
    while True:
        break

    string = value

greet = 'Hey!'
replace(greet, 'Hello')
print(greet)
```

The code defines a function called `replace` that takes 2 **arguments**; string and value as inputs. The function attempts to **mutate the string** however this does not succeed because strings are **immutable**. However, **reassignment of a variable** never mutates the value it contains, so it has no effect on the string contained by greet.

# Exercise 2
Descibe this code:

```python
hello = "Hello, world!"

def my_func():
    print(hello)

my_func()
```
The code assigns a the string "Hello world!" to the global variable `hello`. A function is then defined that takes no argumnets that prints the global variable `hello` and returns `None`. Since **functions in python have access to variables defined in the outer scope**  then this function prints "Hello, world!" when it is **run** at the end of the code.

# Exercise 3
Describe this code:
```python
def append_to(str1, str2):
    for char in str2:
        str1 += char

    return str1
```

The function definition takes 2 strings as arguments and attempts to cycle through the characters in the string passed in the second argument and add them to the string passed in the first argument. A local variable called `str1` is created and modified with each iteration of the for loop with a new character appeneded to the end. The local variable `str1` is then returned by the funciton.

# Exercise 4

Describe this code:

```python

string_1 = 'Test'

def append_to(str2):
    for char in str2:
        string_1 += char

    return string_1
```

The function `append_to` takes a single string as an argument `str2` and attempts to modify a global variable `string_1` by cycling through the characters of `str2` using a for loop and incrementally adding them onto the back of `string 1`. However pyhton cannot modify the global variable `string_1` from inside the function unless `global string_1` is referenced so this function will **raise an error**.

# Exercise 5

Will the code below raise an error?

```python
numbers = [1, 2, 3]
numbers[6] = 5
```

Yes this code will raise an error because it attempts to retrieve the seventh item in `numbers` list but the `numbers` list only has 3 items so the seventh item is **out of range index**. Any attempt to access or modify an element at an index that does not exist will result in an **IndexError** exception.

# Exercise 6

How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.

```python
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False
```

The following code will print true or false if the string ends with an exclaimation mark:

```python
print(str1.endswith('!'))
```

# Exercise 7

Starting with the string below Show two different ways to create a new string with "Four score and " prepended to the front of the string.

```python
famous_words = "seven years ago..."
```

Method 1:

```python
print("Four score and" + famous_words)
```

Method 2:

```python
print(f'Four score and {famous_words}')
```

# Exercise 8

Using the following string, print a string that contains the same value, but using all lowercase letters except for the first character, which should be capitalized.

```python
munsters_description = "the Munsters are CREEPY and Spooky."
```

Answer:

```python
print(munsters_description.capitalize())
```

# Exercise 9

Starting with the string below print the string with the case of all letters swapped:

```python
munsters_description = "The Munsters are creepy and spooky."
```

Answer:
```
print(munsters_description.swapcase())
```

# Exercise 10

Determine whether the name Dino appears in the strings below -- check each string separately:

```python
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
```

Answer
```python
print('Dino' in  str1)
```

# Exercise 11

How can we add the family pet, "Dino", to the following list?

```python
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
```

Answer:

```python
flintstones.append("Dino")
```

# Exercise 12

How can we add multiple items to our list in the previous example (e.g., 'Dino' and 'Hoppy')? Replace the call to append with another method invocation.

Answer:

```python
flintstones.extend(['Dino', 'Hoppy'])
```

# Exercise 13

Print a new version of the sentence given by advice that ends just before the word house. Don't worry about spaces or punctuation: remove everything starting from the beginning of house to the end of the sentence.

```python
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
```

Answer:

```python
print(advice.split('house')[0])
```

# Exerise 14

Print the following string with the word important replaced by urgent:

```python
advice = "Few things in life are as important as house training your pet dinosaur."
```

Answer:

```python
advice.replace('important', 'urgent')
```

# Exercise 15

Write two distinct ways of reversing the list without mutating the original list.

```python
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
```

Answer:

```python
numbers[::-1]
list(reversed(numbers))
```

# Exercise 16

Given a number and a list, determine whether the number is included in the list.

```python
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
```

Answer:

```python
print(number1 in numbers)
```

# Exercise 17

Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.

```python
print(42 > 10  and 42 < 100)
print (42 in range (10,101))
```

# Exercise 18

Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number at index 2, so that the list becomes [1, 2, 4, 5].

Answer:

```python
numbers_list = [1, 2, 3, 4, 5]
numbers_list.pop(2)
```

# Exercise 19
How would you verify whether the data structures assigned to the variables numbers and table are of type list?

```python
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
```

Answer:

```python
type(numbers) is list
```

# Exercise 20
Write a one-liner to count the number of lower-case t characters in each of the following strings:

```python
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
```

Answer:

```python
statement1.count('t')
```

# Exercise 21

Determine whether the following dictionary of people and their age contains an entry for 'Spot':

```python
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
```

Answer:

```python
'spot' in ages
```

# Exercise 22

Write two different ways to remove all of the elements from the following list:

```python
numbers = [1, 2, 3, 4]
```

Answer:

```python
numbers.clear()
```

```python
while numbers:
   numbers.pop()
```

# Exercise 23

What will the following code output?

```python
print([1, 2, 3] + [4, 5])
```

Answer:

In Python, you can use the + operator to concatenate two lists. This operation merges the second list into the first one, producing a new combined list.

# Exercise 24

What will the following code output?

```python
str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
```

Answer: 

The following code will output `"hello there'` because the variable `str1` is assigned to the string `"hello there"` and while a second variable `str2` is then assigned to point to `str1` it is subsequently reassigned to `"goodbye!"` without altering the original value of `str1`. So when `str1` is printed at the end of the code it is still assigned to the string `"hello there"`.

# Exercise 25

What will the following code output?

```python
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
```

Answer:
The code will output `my_list1` with the first dictionaries value for the key `"first"` altered to `42`. This is because the `copy()` method creates a *shallow copy* of the list and only copies the outermost list but the items within the list are pointers to the original dictionaries and integers in `my_list1` so when the dictionary within the `my_list2` is mutated on line 4, this points to the same dictionary referenced in `my_list`.

# Exercise 26

The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?

```python

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
```

Answer 1:

```python
def is_color_valid(color):
    return (color == "blue" or color == "green")
```

Answer 2:

```python
def is_color_valid(color):
    colours = ["blue", "green"]
    return color in colours
```

# Exercise 27

Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. 

Answer:

```python

for i in range(1,11):
    print('-'*i + 'The Flintstones Rock!')
```

# Exercise 28

Alan wrote the following function, which was intended to return all of the factors of number:

```python
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
```
Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.

Answer

The while loop can be fixed by fixing the operator `!=` to `>` this ensures that the code will only run when the `divisor` is greater than 0 and therefore not negative.
The `number % divisor == 0` gets the modulus by dividing the number by the divisor and outputting the remainder. It then checks whether this remainder is equal to zero i.e. the result of the division is an integer with no remainder.

# Exercise 29

Alyssa was asked to write an implementation of a rolling buffer. You can add and remove elements from a rolling buffer. However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.

She wrote two implementations of the code for adding elements to the buffer:

```python
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer
```
Answer
The first function uses the append method that mutates the `buffer` list. Since the argument in the function passes the `buffer` list by reference object then the global list will be modified by the function.

The second function creates a new local list and assigns it to `buffer` list and mutates it locally within the function so the global `buffer` list is not modified by the funciton.

# Exercise 30

What do you think the following code will output?

```python

nan_value = float("nan")

print(nan_value == float("nan"))
```

Answer

The code will return `False` because nan values can be tested for equality because it is not a number. the `math.isnan()` can be used to test wether a value is nan.

# Exercise 31

What is the output of the following code?

```python
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)
```

Answer:

The code will return 36 because the result from the function `mess_with_it` is assigned to the new variable `new_answer` and not to the original `answer` variable that is printed at the end of the code.  

# Exercise 32

One day, Spot was playing with the Munster family's home computer, and he wrote a small program to mess with their demographic data:

```python
munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)
```

 Did the family's data get ransacked? Why or why not?

 Answer:

 The data did get ransacked because dictionaries are mutable and when passed to a function, a reference to the disctionary is passed, not a copy.

 # Exercise 33

 Function and method calls can take expressions as arguments. Suppose we define a function named rps as follows, which follows the classic rules of the rock-paper-scissors game, but with a slight twist: in the event of a tie, it just returns the choice made by both players.

 ```python
 def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
```

What does the following code output?

```python
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))
```

# Exercise 34

Consider these two simple functions:

```python
def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")
```
What will the following function invocation return?
```python
bar(foo())
```

Answer:

That code will return `False` because the `foo` function returns 'yes' when run regardless of the input arguments. Since the `foo` function is passed as an argument to the `bar` function, the `param` argument is assigned to 'yes'. Therfore the `param == "no"` evaluates to `False` in the `bar` function, the right hand part of the *expression* is not run and `False` is returned.

# Exercise 35


Given the following code, predict the output:

```python
a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
```

Answer:

The code will return `True` because the first variable `a` is pointing towards the integer 42 stored in the memeory. The variable `b` is assigned the same value of 42 so Python will point towards the same part of the memory where 42 is stored that `a` is referencing due to *interning* therefore they will have the same id. Variable `c` is assigned variable `a` so it will be pointing to the same locaion that variable `a` is pointing to. So all 3 variables will have the same lcoation id.

# Exercise 36

What does the last line in the following code output?

```python
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
```

Answer: 

The last line of the code will print the disctionary assinged to the `dictionary` variable with the value of the list stored under the key `first` modfied to include `2` in it. This is because the `num_list` variable is a pointer to the list stored under the key `first` in the dictionary and any changes that mutate `num_list` such as the `append` method will also mutate the list within `dictionary`.

# Exericise 37

Given the following similar sets of code, what will each code snippet print?

A)
```python
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

B)
```python
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

C)
```python
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
```

Answer:

Code A defines a function called `mess_with_vars` that takes 3 lists as arguments and assignes them to locally defined variables within the fucntion with the same name as the input arguments. This is known as *variable shadowing*. However since these variables are locally defined, they do not change the global lists so the code will print:

```python
'one is one'
'two is two'
'three is three'
```

Code B defines a similar function called `mess_with_vars` which similary only assigns values to locally defined variables wihtout impacting the global variables so this will print a similar output to code A.

Code C defines a function called `mess_with_vars` that assigns new string values to indexs within the lists passed as arguments. Since lists are mutable and passed into functions by reference then the original global lists are mutated. So the final output of the code is:

```python
'one is two'
'two is three'
'three is one'
```
# Exercise 38

Ben was tasked to write a simple Python function to determine whether an input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11.

Alyssa supplied Ben with a function named is_an_ip_number. It determines whether a string is a numeric string between 0 and 255 as required for IP numbers and asked Ben to use it. Here's the code that Ben wrote:

```python
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True
```

Alyssa reviewed Ben's code and said, "It's a good start, but you missed a few things. You're not returning a false condition, and you're not handling the case when the input string has more or less than 4 components, e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

Help Ben fix his code.

Answer:
```python
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    
    result = False
    
    while len(dot_separated_words) = 4:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            result = False
            break
        else:
            result = True

    return result
```

# Exercise 39

What do you expect to happen when the greeting variable is referenced in the last line of the code below?

```python
if False:
    greeting = "hello world"

print(greeting)
```

Answer

Python will throw an error since the viable greeting is never created because the `if` block is not executed due to its false condition so the vairable is never initialized. 


