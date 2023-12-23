# Python quick note

---

## Variable

Python do not require to declare the type of varibles. The variable's type and value are initialized at the moment of assignment. Variable assignment is performed with the equal sign (=).

**Example:**

```python
a = 231
s = "Hello guys"
b = a + 2.1
```
The “= 231” portion of the above definition is called initialization.

## Augmented assignment

```python
x = 1.2
x += 1 # Equal to x = x + 1
x *= 2 # Equal to x = x * 2
x /= 4 # Equal to x = x / 4
```

---

## Conditional

### Boolean

```python
x = False
y = True
```

### and, or and not

```python
x = False
y = True

print(x and y)  # java: System.out.println(x && y)
print(x or y)   # java: System.out.println(x || y)
print(not x)    # java: System.out.println(! x)
```



### Conditional Statement

Python use `:` and indent to decide which code block belows to `if`

```python
if (boolean statement):
    inside if statement
    some action           

outside the if statement
```

This is equals to:
```java
if (boolean statement){
    inside if statement
    some action       
}    

outside the if statement
```


**Example:**

If any of A, B, C, D, or F are entered, an appropriate message will be written, and control will go to the statement immediately following the extended if statement. If any other string is entered, the final else is invoked, and the message Invalid grade will be written.

```python
grade = 'C'; 

if (grade == "A"):
    print("Excellent!")
elif (grade == "B"):
    print("Good")
elif (grade == "C" or grade == "D"):
    print("Poor")
elif (grade == "F"):
    print("Egregious!")
else :
    print("Invalid grade")
```

This is equals to:
```java
String grade = 'C'; 

if (grade.equals("A")){
    print("Excellent!")
} else if (grade.equals("B")){
    print("Good")
} else if (grade.equals("C") || grade.equals("D")){
    print("Poor")
} else if (grade.equals("F")){
        print("Egregious!")
} else {
    print("Invalid grade")
}
```

---

## Input

Python use fucntion `input()` to get user input from keyboard, the `input` function will always return a `string` object. Onee call  `input()`, it will real one line from the user input.

### User Input to a python Program

```python
n = input()

x = input("Where is your hometown?")
```

**Example**:


```python
n = input()          # read user input, the type is String
n = int (n)          # Cast n into int
if (n > 0):
    if (n % 2 == 0) :
        print(n)
else :
    print(n , "is not positive")
```

---

## Function
### Function Defination
In python, we use `def` keyword to indicate we are going to define a new function, the `function name` should be followed to the `def` keyword. The code block under the function defination with a indent is the function body.

```python
def my_sqr(x) :
    # Function Body Starts
    return x * x
    # Function Body Ends

# Not inside the Func Body
```

The ```return``` keyword is placed before the expression to be returned.

### Function Parameter
```python
def my_add(x, y): 
    return x + y

def my_num():
    return my_add(40, 2)
```

```Parameters``` are separated by a comma (,) in the function definition and calling syntax.

The header of a method defines the `parameters` of that method. For example, consider the withdraw method:

```python
def withdraw(acctPassword, amount):
    ...
```

Think of them as placeholders for the pair of actual parameters or arguments that will be supplied by a particular method call.

```python
withdraw("123456", 20)
```

Here "123456" and 20 are the `actual parameters` that match up with acctPassword and amount for the withdraw method.

---

## Loop

### iterator range()
`range(start, end, step_size)`

```python
range (1, 5, 1) # Generate [1, 2, 3, 4]
range (1, 5, 2) # Generate [1, 3]

range (1, 5)    # if no step_size is input, the step_size
                # will be set to 1

range (5, 1, -1)    # Generate [5, 4, 3, 2]

range (1, 5, -1)    # Nothing
```

### For Loop

The general form of the for loop is

```python
for i in range (a, b) :
    # loop body starts
    statements
    # loop body ends

# Outside the loop body
```

`i` is the Loop variable

The termination condition is tested at the top of the loop the update statement is performed at the bottom.

**Example**

```python
# outputs 1 2 3 4
for i in range (1, 5):
    print(i, end = ' ')
```

Here’s how it works. The `iterator` `range(a, b)` will generate the range `[a, a+1, ..., b - 1]`. 

The  ```loop variable i```  will take one number from the `range(a, b)` each loop. 

As soon as the ```loop variable i``` used all numbers in the iterator, control passes to the first statement following the loop.


### While Loop

The general form of the while loop is

```python
x = 10
while (boolean test) :
    # loop body starts
    statements 
    # loop body ends

# Outside the loop body
x = 100
```

The ```boolean test``` is performed at the beginning of the loop. If true, the loop body is executed. Otherwise, control passes to the first statement following the loop. After execution of the loop body, the test is performed again. If true, the loop is executed again, and so on.



## Array

In Python, an array is an object.

**Array Definition**

```Python
arr = []
```

```Python
arr = [1, 2, 3, 4, 5]
```

**Length of Array**

```Python
arr = [1, 2, 3, 4, 5, 6, 7]

print(len(arr)) # 7
```

**Traversing an Array**

Use a ```for-each``` loop whenever you need access to every element in an array ```without replacing or removing any elements```. Use a for loop in all other cases: to access the index of any element, to replace or remove elements, or to access just some of the elements.

```Python
# @return the number of even integers in array arr of integers

def countEven(arr):
    count = 0
    for num in arr :
        if ( num % 2 == 0):  #num is even 
            count+=1

    return count 
```

### List build-in Method

**Append: Append an element to the end of an array.**
```Python
numbers = [0, 1, 2, 3, 4, 5]
numbers.append(10)

print(numbers) # [0, 1, 2, 3, 4, 5, 10]

numbers.append(11)
print(numbers) # [0, 1, 2, 3, 4, 5, 10, 11]
```

**Extend: connect two array to a new array.**
```Python
arr1 = [1, 2, 3, 4]
arr2 = [10, 11, 12]

arr1.extenr(arr2)

print(arr1)    # [1, 2, 3, 4, 10, 11, 12]
print(arr2)    # [10, 11, 12]
```

**Add: add two array together**
```Python
arr1 = [1, 2, 3, 4]
arr2 = [10, 11, 12]

arr3 = arr1 + arr2

print(arr1)    # [1, 2, 3, 4]
print(arr2)    # [10, 11, 12]
print(arr3)    # [1, 2, 3, 4, 10, 11, 12]
```
**pop: remove the element from array**
```Python
arr1 = [1, 2, 3, 4]

arr1.pop(0)
print(arr1)    # [2, 3, 4]
arr1.pop(-1)
print(arr1)    # [2, 3]
```

```Python
arr1 = [1, 2, 3, 4]

arr1.pop()
print(arr1)    # [1, 2, 3]
```

**Slicing: Extract a portion of a sequence using the slice notation (start:stop:step).**
```Python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[1:-1]) # Output: [1, 2, 3, 4]
print(numbers[1:-1: 2])  # Output: [1, 3]
```

**Concatenation: Combine two sequences of the same type using the + operator.**
```Python
repeat_arr = [1, 2]
print(repeat_arr * 3)  # Output: [1, 2, 1, 2, 1, 2]
```

**Sort: Sort an array**
```Python
arr = [1, 3, 2]
print(sorted(arr)) # Output: [1, 2, 3]
```

---

## String

### Working with ASCII Codes in Python
Python provides two built-in functions to convert between characters and their corresponding ASCII codes:

**ord(char): Returns the ASCII value of the given char.**

```python
print(ord('A'))  # Output: 65
```

**chr(ascii_code): Returns the character corresponding to the given ascii_code.**

```python
print(chr(65))  # Output: 'A'
```

### String Methods

An object of type ```String``` is a sequence of ```characters```. 

A String object is unusual in that it can be initialized like a primitive type:

```Python
s1 = "abc"
s2 = ""
```

in the sense that in both cases s is a reference to a String object with contents "abc".

```Python
s = "John" 
s = "Harry"     #  It is possible to reassign a String reference:
```

Notice that this is consistent with the immutable feature of String objects. "John" has not been changed he has merely been discarded! The fickle reference s now refers to a new String, "Harry". It is also OK to reassign s as follows:


```Python
s = s + " Windsor"
```

**The Concatenation Operator**

```Python

five = 5

state = "Hawaii-"

tvShow = state + str(five) + "-0" # tvShow has value
                                    # "Hawaii-5-0"
x = 3, y = 4
sum = str(x) + str(y)
```

### String build-in Method

**Find: The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.**

```Python
message = 'Python is a fun programming language'
print(message.find('fun'))
print(message.rfind('language'))
```

**upper(): Converts all characters in the string to uppercase.**

```python
text = "hello world"
print(text.upper())  # Output: 'HELLO WORLD'
```

**lower(): Converts all characters in the string to lowercase.**


```python
text = "HELLO WORLD"
print(text.lower())  # Output: 'hello world'
```

**strip(): Removes leading and trailing whitespace from the string.**


```python
text = "  hello world  "
print(text.strip())  # Output: 'hello world'
```

**replace(old, new): Replaces all occurrences of the old substring with the new substring.**


```python
text = "hello world"
print(text.replace("world", "there"))  # Output: 'hello there'
```
**split(separator): Splits the string into a list of substrings based on the specified separator.**

```python
text = "hello world"
print(text.split(" "))  # Output: ['hello', 'world']
```
**join(list): join the sting in a list together**

```pyhton
myTuple = ["John", "Peter", "Vicky"]

x = "#".join(myTuple)

print(x)
```

**String compare**

```python
print("aa" < "ab")
```

It compares strings in dictionary (lexicographical) order:
* If `string1 < string2`,  then string1 precedes string2 in the dictionary.
* If `string1 > string2`,  then string1 follows string2 in the dictionary.
* If `string1 == string2`, then string1 and string2 are identical.


---

## Common usage of String and List
**Indexing: Access an individual item in a sequence using its index (zero-based).**

```Python
text = "hello"
print(text[1])  # Output: 'e'
```

**Slicing: Extract a portion of a sequence using the slice notation (start:stop:step).**
```Python
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]
print(numbers[1:-1]) # Output: [1, 2, 3, 4]
print(numbers[1:-1: 2])  # Output: [1, 3]
```

**Length: Determine the number of items in a sequence using the len() function.**
```Python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3
```

**Concatenation: Combine two sequences of the same type using the + operator.**
```Python
repeat_text = "ha"
print(repeat_text * 3)  # Output: 'hahaha'
```

**In and not in: check if the object is inside the sequence.**

```Python
seq_1 = "abc"
seq_2 = [1, 2, 3]
print('a' in seq_1) # Output: True
print(4 not in seq_2) # Output: True
```

---

## Dictionary

A dictionary in Python is an unordered collection of items. Each item stored in a dictionary has a key-value pair.

key-value pairs are basic to computer 
applications:

- Looking up someone in an online phonebook
- Logging onto a server with your userid and password
- Opening up a document by specifying its name

**Creating a Dictionary**

You can create a dictionary by placing items (key-value pairs) inside curly braces ```{}```, separated by commas. A key and its corresponding value are connected with a colon :

```python
student = {
    "name": "John",
    "age": 12,
    "grade": 7
}
```

In the above example, "name", "age", and "grade" are keys, while "John", 12, and 7 are their corresponding values.


**Find**


You can access a dictionary's value by referencing its key inside square brackets ```[]```.

```python
print(student["name"])  # Output: John
```

What if you want access a key does not exist in dictionary?

```python
print(student["adadadda"])
```

Python will raise a ```KeyError``` if you try to access a key that doesn't exist in the dictionary. To avoid this, you can use the ```get()``` method, which returns None (or a default value that you can set) if the key doesn't exist.

```python
print(student.get("GPA"))  # Output: None
print(student.get("GPA", 0.0))  # Output: 0.0
```

Or you can use keyword  ```in```.

```python
print("GPA" in student)  # Output: False
```

**Update**

You can update a dictionary's value by referencing its key and using the assignment operator =.

```python
student["age"] = 13
print(student)  # Output: {'name': 'John', 'age': 13, 'grade': 7}
```

**Add**

You can also add new key-value pairs the same way:

```python
student["GPA"] = 3.8
print(student)  # Output: {'name': 'John', 'age': 13, 'grade': 7, 'GPA': 3.8}
```

**Delete**

You can remove a key-value pair using the ```del``` keyword:

```python
del student["age"]
print(student)  # Output: {'name': 'John', 'grade': 7, 'GPA': 3.8}
```

You can also remove a key-value pair using ```pop```:

```python
student.pop("age")
print(student)  # Output: {'name': 'John', 'grade': 7, 'GPA': 3.8}
```


[def]: #python-quick-note