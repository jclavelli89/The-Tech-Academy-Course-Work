###
### 2. Python Quick Start
###

# Selecting code with conditionals

# a, b = 0, 1
#
# if a < b:
#     print('a ({}) is less than b ({})'.format(a, b))
# else:
#     print('a ({}) is not less than b ({})'.format(a, b))
#
# print("foo" if a < b else "bar")

##
## Repeating code with a loop
##

# # simple fibonacci series
#
# a, b = 0, 1
# while b < 50:
#     print(b)
#     a, b = b, a + b
#
# print("Done")
#
# # for loop which works with iterators
# fh = open('lines.text')
# for line in fh.readlines()
#     print(line)

##
## Reusing code with a function
##

# def isprime(n):
#     if n == 1:
#         print("1 is special")
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             print("{} equals {} x {}".format(n, x, n // x))
#             return False
#     else:
#         print(n, "is a prime number")
#         return True
#
# for n in range(1, 30):
#     isprime(n)
 
##
## Creating sequence with generator functions
##

# def isprime(n):
#     if n == 1:
#         return False
#     for x in range(2, n):
#         if n % x == 0:
#             return False
#     else:
#         return True
#
# def primes(n = 1):
#     while(True):
#         if isprime(n): yield n
#         n += 1
#
# for n in primes():
#     if n > 100: break
#     print(n)

##
## Reusing code and data with a class
##

# class Fibonacci():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def series(self):
#         while(True):
#             yield(self.b)
#             self.a, self.b = self.b, self.a + self.b
#
# f = Fibonacci(0, 1)
# for r in f.series():
#     if r > 100: break
#     print(r, end = '  ')


##
## Greater reusability with inheritance and polymorphism
##

# class AnimalActions:
#     def quack(self): return self.strings['quack']
#     def feathers(self): return self.strings['feathers']
#     def bark(self): return self.strings['bark']
#     def fur(self): return self.strings['fur']
#
# class Duck(AnimalActions):
#     strings = dict(
#         quack = "Quaaaak!",
#         feathers = "The duck has gray and white feathers.",
#         bark = "The duck cannot bark.",
#         fur = "The duck has no fur"
#     )
#
# class Person(AnimalActions):
#     strings = dict(
#         quack = "The person imitates a duck.",
#         feathers = "The person takes a feather from the ground and shows it.",
#         bark = "The person says woof!",
#         fur = "The person puts on a fur coat."
#     )
#
# class Dog(AnimalActions):
#     strings = dict(
#         quack = "The dog cannot quack.",
#         feathers = "The dog has no feathers.",
#         bark = "Arf!",
#         fur = "The dog has white fur with black spots."
#     )
#
# def in_the_doghouse(dog):
#     print(dog.bark())
#     print(dog.fur())
#
# def in_the_forest(duck):
#     print(duck.quack())
#     print(duck.feathers())
#
# def main():
#     donald = Duck()
#     john = Person()
#     fido = Dog()
#
#     print("- In the forest: ")
#     for o in ( donald, john, fido):
#         in_the_forest(o)
#
#     print("- In the doghouse: ")
#     for o in ( donald, john, fido):
#         in_the_doghouse(o)
#
# if __name__ == "__main__": main()

###
### Another OOP way
###

# # -- VIEW --
#
# class AnimalActions:
#     def bark(self): return self._doAction('bark')
#     def fur(self): return self._doAction('fur')
#     def quack(self): return self._doAction('quack')
#     def feathers(self): return self._doAction('feathers')
#
#     def _doAction(self, action):
#         if action in self.strings:
#             return self.strings[action]
#         else:
#             return 'The {} has no {}'.format(self.animalName(), action)
#
#     def animalName(self):
#         return self.__class__.__name__.lower()
#
# # -- MODEL --
#
# class Duck(AnimalActions):
#     strings = dict(
#         quack = "Quaaaaak!",
#         feathers = "The duck has gray and white feathers."
#     )
#
# class Person(AnimalActions):
#     strings = dict(
#         bark = "The person says woof!",
#         fur = "The person puts on a fur coat.",
#         quack = "The person imitates a duck.",
#         feathers = "The person takes a feather from the ground and shows it."
#     )
#
# class Dog(AnimalActions):
#     strings = dict(
#         bark = "Arf!",
#         fur = "The dog has white fur with black spots.",
#     )
#
# # -- CONTROLLER --
#
# def in_the_doghouse(dog):
#     print(dog.bark())
#     print(dog.fur())
#
# def in_the_forest(duck):
#     print(duck.quack())
#     print(duck.feathers())
#
# def main():
#     donald = Duck()
#     john = Person()
#     fido = Dog()
#
#     print("-- In the forest:")
#     for o in ( donald, john, fido ):
#         in_the_forest(o)
#
#     print("-- In the doghouse:")
#     for o in ( donald, john, fido ):
#         in_the_doghouse(o)
#
# if __name__ == "__main__": main()

##
## Handling errors with exceptions
##

# fh = open('xlines.txt')
# for line in fh.readlines():
#     print(line)

# try:
#     fh = open('xlines.txt')
#     for line in fh.readlines():
#         print(line)
#
# except IOError as e:
#     print("Something bad happened ({}".format(e))
#
# print("after badness")

##
## 3. Setting up Python
##

# Done

##
## 4. General Syntax
##

##
## Creating a main script (helps let you call functions anytime
##

# def main():
#     print("This is the syntax.py file.")
#     egg()
#
# def egg():
#     print("egg")
#
# if __name__ == "__main__": main()

##
## Understanding whitespace in Python
##

# four spaces standard indent

## def main():
##     print("This is an example.")
##     print("another line, has to be at same indentation")

# Indenting is important if you have multiple commands, but if you have only one, than the function cna reside on one line
## def main(): print("This is the example.")

##
## Commenting Code
##

# comments use hash tag
# Don't comment too much, its purpose is to make the code clear

##
## Assigning Values
##

# def main():
#     # a = "one"
#     # a, b = 0, 1
#     # a, b = b, a
#     # a = True
#     a = [1, 2, 3, 4, 5]   # This is  tuple where you have list assigned to a variable. A tuple is a finite ordered list of elements
#     print(type(a), a)
#
# if __name__ == "__main__": main()

##
## Selecting code and values with conditionals
##

## Conditional Executions (traditional)
# def main():
#     a, b = 1, 1
#     if a < b:
#         print("a is less than b")
#     elif a > b:
#         print("a is greater than b")
#     else:
#         print("a is equal b")
#
# if __name__ == "__main__": main()

## Conditional Expressions Test
# def main():
#     a, b = 1, 1
#     s = "Less than" if a < b else "not less than"
#     print(s)
#
# if __name__ == "__main__": main()

##
## Creating and using functions
##

# def main():
#     func(1)
#     func(5)
#     func(7)
#
# def func(a):
#     for i in range(a, 10):
#         print(i, end=' ')
#     print() # prints an empty line
#
# if __name__ == "__main__": main()
#


##
## Creating and using objects
##

# class Egg:
#     def __init__(self, kind = "fried"):
#         self.kind = kind
#
#     def whatKind(self):
#         return self.kind
#
#
# def main():
#     fried = Egg()
#     scrambled = Egg('scrambled')
#     print(fried.whatKind())
#     # print(scrambled.whatKind())
#
#
# if __name__ == "__main__": main()

##
## 5. Variables, Objects, and Values.
##

##
## Understanding variables and objects in Python
##

# Everything in Python is an object. Every object has a ID, Type and a value
#
# X = 42 the 42 is the value
# x
# 42
# id(x)
# a unique number that is as an Identifer
# type(x)
# <class 'int'>

##
## Distingquishing mutable and immutable objects
##

# mutable objects can change
#
# immutable objects can not change (the distinction is found by the id(x) which provides a unique number )

##
## Using numbers
##

# def main():
#     num = 42 // 5 # this is integer division
#     print(num)
#     print(type(num), num)

# if __name__ == "__main__": main()


##
## Using strings (They are immutable objects)
##

# def main():
#     n = 42
#     # s = r'This is a\n string!' # The r before the string tells the system to display it "as is"
#     # s = "This is a {} string!".format(n) # Python 3 way of doing it
#     # s = "This is a %s string!" % n # This is the Python 2 way of doing the line above DONT USE, it will be deprecated
#     # s = ''' this is a string ''' # Allows to have a string that spans several lines like example below
#     s = '''\      # the \ escapes the extra line
#     This is a string
#     line after line
#     of text and more
#     text.
#     '''
#     print(s)
#
#
# if __name__ == "__main__": main()

##
## Aggregating values with lists and tuples
##

# def main():
#     # x = (1, 2, 3) # Tuple is an immutable object (cant be changed, must be fixed)
#     # x = [1, 2, 3]    # It is mutable object (can append or insert to list)
#     # x.append(5)
#     # x.insert(2, 7)
#     # x = 'string'
#     # print(type(x), x[2:4]) # slicing
#     x = 'String'
#     for i in x:
#         print(i)
#
#
#
# if __name__ == "__main__": main()


##
## Creating associative lists with dictionaries
##

# def main():
#     # d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
#     # for k in sorted(d.keys()):
#     #     print(k, d[k])
#     d = dict(
#         one = 1, two = 2, three = 3, four = 4, five = 'five'
#     )
#     d['seven'] = 7  # dict ionaries are mutable
#     for k in sorted(d.keys()):
#         print(k, d[k])
#
# if __name__ == "__main__": main()

##
## Finding the type and identity of a variable
##

# >>> x =  42
# >>> x
# 42
# >>> id(x)
# 1386935376
# >>> id(42)
# 1386935376
# >>> id(x)
# 1386935376
# >>> y = 42
# >>> x == y
# True
# >>> x is y
# True
# >>> x = dict(x = 42)
# >>> {'x':42}
# {'x': 42}
# >>> type(x)
# <class 'dict'>
# >>> id(x)
# 1596882536840
# >>> y = dict( x = 42)
# >>> id(y)
# 1596882465672
# >>> id(x)
# 1596882536840
# >>> y == x
# True
# >>> y is x
# False
# >>>

##
## Specifying logical values with True and False
##

# >>> a, b = 0, 1
# >>> a == b
# False
# >>> a < b
# True
# >>> a > b
# False
# >>> a = True
# >>> a
# True
# >>> type(a)
# <class 'bool'>
# >>> id(a)
# 1386679984
# >>> b = True
# >>> id(b)
# 1386679984
# >>> id(True)
# 1386679984
# >>>

##
## 6. Conditionals
##

##
## Selecting Code with if and else conditional statements
##

# def main():
#     a, b = 0, 1
#     if a < b:
#         print('This is true')
#     else:
#         print('This is not true')
#
#
# if __name__ == "__main__": main()

##
## Selecting multiple choice with elif
##

# def main():
#     v = 'seven'
#     if v == 'one':
#         print('v is one')
#     elif v == 'two':
#         print('v is two')
#     elif v == 'three':
#         print('v is three')
#     else:  # catch all command in event all of above are not true
#         print('v is someother thing')
#
#
# if __name__ == "__main__": main()

##
## Understanding other strategies for muliptle choice
##

# Python does not have "switch" or "case" that allows to select from multiple choice of variable
# Pythons way of doing it below

# def main():
#     choices = dict(
#         one = 'first',
#         two = 'second',
#         three = 'third',
#         four = 'fourth',
#         five = 'fifth'
#     )
#     v = 'seven'
#     print(choices.get(v, 'other'))
#
# if __name__ == "__main__": main()

##
## Using the conditional expression
##

# def main():
#     a, b = 1, 1
#     if a < b:
#         v = 'This is true'
#     else:
#         v = 'This is not true'
#     print(v)
#
# if __name__ == "__main__": main()

# Easier way

# def main():
#     a, b = 1, 1
#     v = 'this is true' if a < b else 'this is not true'
#     print(v)
#
# if __name__ == "__main__": main()

##
## 7. Loops
##

##
## Creating loops with while
##

# def main():
#     # simple fibonacci series
#     # the sum of two elements defines the next set
#     a, b = 0, 1
#     while b < 150:
#         print(b, end=' ')
#         a, b = b, a + b
#
# if __name__ == "__main__": main()

##
## Iterating with for
##

# #!/usr/bin/python3
# # for.py by Bill Weinman [http://bw.org]
# # This is an exercise file from Python 3 Essential Training lynda.com
# # Copyright 2010 The BearHeart Group, LLC
#
# def main():
#     for line in [1, 2, 3, 4, 5]:
#         print(line, end=' ')
#
# if __name__ == "__main__": main()

## Enumerating iterators
#def main():
#    s = 'this is a string'
#    for i, c in enumerate(s):
#        if c == 's': print('index {} is an s'.format(i))
#
#if __name__ == "__main__": main()


## Controlling loop flow with break, continue, and else

## def main():
#     s = 'this is a string'
#     i = 0
#     while (i < len(s)):
#        print(s[i], end='')
#        i += 1
#     else:
#        print('else')
#
#if __name__ == "__main__": main()

## 8. Operators
##

##
## Performing simple arithmetic
##

# >>> 5 + 5
# 10
# >>> 5 * 5
# 25
# >>> 5 - 3
# 2
# >>> 5 / 3
# 1.6666666666666667
# >>> 5 // 3
# 1
# >>> 5 % 3
# 2
# >>> divmod(5, 3)
# (1, 2)
# >>> num = 5
# >>> num += 1
# >>> num
# 6
# >>> num -= 1
# >>> num
# 5
# >>> num *= 5
# >>> num
# 25
# >>> num // = 5
# SyntaxError: invalid syntax
# >>> num //= 5
# >>> num
# 5
# >>> num *= 5
# >>> num /= 5
# >>> num
# 5.0
# >>>

## Operating on bitwise values
##

# >>> 5
# 5
# >>> 0b0101
# 5
# >>> def b(n): print('{:08b}'.format(n))
#
# >>> b(5)
# 00000101
# >>> b(10)
# 00001010
# >>> b(100)
# 01100100
# >>> x, y = 0x55, 0xaa
# >>> b(x)
# 01010101
# >>> b(y)
# 10101010
# >>> b(x | y)
# 11111111
# >>> b(x & y)
# 00000000
# >>> b(x ^ y)
# 11111111
# >>> b(x ^ 0)
# 01010101
# >>> b(x ^ 0xff)
# 10101010
# >>> b(x << 4)
# 10101010000
# >>> b(x >> 4)
# 00000101
# >>> b(~ x)
# -1010110
# >>>

## Comparison Operators 

# >>> 5 < 6
# True
# >>> 6 < 5
# False
# >>> 5 <= 6
# True
# >>> 5 <= 5
# True
# >>> 6 >= 5
# True
# >>> 6 >= 6
# True
# >>> 6 >= 7
# False
# >>> 5 == 5
# True
# >>> 5 == 6
# False
# >>> 6 != 7
# True
# >>> 6 != 6
# False
# >>> x, y = 5, 6
# >>> id(x)
# 1568356176
# >>> id(y)
# 1568356192
# >>> x is y
# False
# >>> x is not y
# True
# >>> y = 5
# >>> id(y)
# 1568356176
# >>> x is y
# True
# >>> x, y = [5], [5]
# >>> id(x)
# 51663136
# >>> id(y)
# 51663096
# >>> x == y
# True
# >>> x is y
# False
# >>>

## Operating on Boolean Values

# >>> 5 == 5
# True
# >>> 7 < 5
#  False
#  >>> type(True)
#  <class 'bool'>
#  >>> True and False
#  False
#  >>> True and True
#  True
#  >>> True or False
#  True
#  >>> False or False
#  False
#  >>> True & True
#  True
#  >>> a, b = 0, 1
#  >>> x, y = 'zero', 'one'
#  >>> x < y
#  False
#  >>> a < b
#  True
#  NameError: name 'n' is not defined
#  >>> 
#  >>> if a < b and x < y: print('yes')
#  else: print('no')

#  no
#  >>>

## Operating on parts of a container with the slice operator
##
# Slices = part of container

# >>> list = []
# >>> list = [1,2,3,4,5,6,7,8,9,10]
# >>> list[0]
# 1
# >>> list[1]
# 2
# >>> list[9]
# 10
# >>> list[0:5]
# [1, 2, 3, 4, 5]
# >>> list[4]
# 5
# >>> list[0:5]
# [1, 2, 3, 4, 5]
# >>> range(0, 10)
# range(0, 10)
# >>> for i in range(0,10): print(i)
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# >>> list[0:10]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list[:] = range(100)
# >>> 
# >>> list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# >>> list[27]
# 27
# >>> list[27]
# 27
# >>> list[27:42]
# [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
# >>> list[27:42:3]
# [27, 30, 33, 36, 39]
# >>> list[27:43:3]
# [27, 30, 33, 36, 39, 42]
# >>> for i in list[27:43:3] : print(i)
#
# 27
# 30
# 33
# 36
# 39
# 42
# >>> list[27:43:3] = (99,99,99,99,99,99)
# >>> list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 99, 28, 29, 99, 31, 32, 99, 34, 35, 99, 37, 38, 99, 40, 41, 99, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

## Understanding Operator Precedence:
#

# >>> 5 * 25 + 14 / 2 # Precedence 1. * 2. / 3. + 4. -
# 132.0
# >>> 5 * (25 + 14) / 2 # Parenthesis used to explicit state your intentions
# 97.5
# >>> # If code is written poorly where the intent is not clear, than refer to the Python Operator Precedence chart to help understand the order
# >>> # Be kind and use paranthesis to clearly state the intent of your code
# >>>

## 9. Regular Expressions

# Using the re module 

# - Regular expressions are a very powerful method of matching patterns in text
# - Actually a small language in itself, regexes can be very simple or very complex
# - Implemented in Python with the "re" module

# import re

# pattern = re.compile(r'\d\d\d')
#      if re.search(regex, line): print(line)

## Searching with regular expressions

## Used to show all lines that contain Lenore and Nevermore
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         if re.search('(Len|Neverm)ore', line):
#             print(line, end='')
#
# if __name__ == "__main__": main()

# Example below for finding matches - good for finding patterns and replacing
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         match = re.search('(Len|Neverm)ore', line)
#         if match:
#             print(match.group())
#
# if __name__ == "__main__": main()

##
## Searching with regular expressions
##

# Find and replace
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         print(re.sub('(Len|Neverm)ore', '###', line), end='')
#
# if __name__ == "__main__": main()

# Search and replace modules
# import re
#
# def main():
#     fh = open('raven.txt')
#     for line in fh:
#         match = re.search('(Len|Neverm)ore', line)
#         if match:
#             print(line.replace(match.group(),'happy'), end='')
#
# if __name__ == "__main__": main()

##
## Reusing regular expressions with re compile
##

# A way to improve efficiency by putting search string in "pattern"
# adding re.IGNORECASE will ignore case
# import re
#
# def main():
#     fh = open('raven.txt')
#     pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
#     for line in fh:
#         if re.search(pattern, line):
#             print(pattern.sub('super happy', line), end='')
#
# if __name__ == "__main__": main()

##
## 10. Exceptions
##

##
## Learning how exceptions work
##

# -Exceptions are the key method of handling errors in Python
# -"try" something, then catch an exception with "except"

# try:
#     fh = open('filename')
# except IOError as e:
#     print(e)
# else:
#     for | in fh:print(|)

# You may raise your own exceptions with "raise"

##
## Handling exceptions
##

# def main():
#     fh = open('lines.txt')
#     for line in fh: print(line.strip())
#
# if __name__ == "__main__": main()

# Exmpale of try and catch
# def main():
#     try:
#         fh = open('lines.txt')
#     except:
#         print('could not open the file. come back in 2000 years')
#     else:
#         for line in fh: print(line.strip())
#
# if __name__ == "__main__": main()

##
## Raising exceptions
##

# def main():
#     try:
#         for line in readfile('lines.doc'): print(line.strip())
#     except IOError as e:
#         print('cannot read file:', e)
#     except ValueError as e:
#         print('bad filename', e)
#
# def readfile(filename):
#     if filename.endswith('.txt'):
#         fh = open(filename)
#         return fh.readlines()
#     else: raise ValueError('Filename must end with .txt')
#
# if __name__ == "__main__": main()

##
## 11. Functions
##

##
## Defining functions
##

# def main():
#     testfunc(42)
#
# def testfunc(number):
#     print('This is a test function', number)
#
# if __name__ == "__main__": main()

# def main():
#     testfunc(42, 43, 75)
#
# def testfunc(number, another, onemore):
#     print('This is a test function', number, another, onemore)
#
# if __name__ == "__main__": main()

# You can set default values that will deploy if no arguments are provided. This keeps the code working
# You don't have to have a value, use None like below as well. It is special value you can test for.
# def main():
#     testfunc(42, 43, 75)
#
# def testfunc(number, another = None, onemore = 0):
#     print('This is a test function', number, another, onemore)
#
# if __name__ == "__main__": main()

# You can uss pass to be a filler/placeholder for a function to keep an error from generating

# def main():
#     testfunc()
#
# def testfunc():
#     pass
#
# if __name__ == "__main__": main()


##
## Using lists in arguments
##

# def main():
#     testfunc(1, 2, 3, 42, 43, 45, 46)
#
# def testfunc(this, that, other, *args):
#     print(this, that, other)
#     for n in args: print(n, end=' ')
#
# if __name__ == "__main__": main()

##
## Using named function arguments
##

# kwargs = Keyword Arguments

# def main():
#     testfunc(one = 1, two = 2, four = 42)
#
# def testfunc(**kwargs):
#     print('This is is a test function', kwargs['one'], kwargs['two'], kwargs['four'])
#
# if __name__ == "__main__": main()

# The only rule for arguments and calling them is that they are in the same order, but any combination there of is ok

# def main():
#     testfunc(5, 6, 7, 8, 9, 10, one = 1, two = 2, four = 42)
#
# def testfunc(this, that, other, *args, **kwargs):
#     print('This is is a test function',
#           this, that, other, args,
#           kwargs['one'], kwargs['two'], kwargs['four'])
#
# if __name__ == "__main__": main()

##
## Returning values from functions
##

# The keyword return returns any type/object

# def main():
#     for n in testfunc(): print(n, end=' ')
#
# def testfunc():
#     #return 'This is a test function'
#     return range(25)
#
# if __name__ == "__main__": main()

##
## Creating a sequence with a generator function
##

# A generator function is a function that returns an iterator object.

# def main():
#     print('This is the function.py file.')
#     for i in inclusive_range(0, 25, 1):
#         print(i, end = ' ')
#
# def inclusive_range(start, stop, step):
#     i = start
#     while i <= stop:
#         yield i
#         i += step
#
# if __name__ == "__main__": main()

# def main():
#     print('This is the function.py file.')
#     for i in inclusive_range(25):
#         print(i, end = ' ')
#
# def inclusive_range(*args):
#         numargs = len(args)
#         if numargs < 1: raise TypeError('requires at least one argument')
#         elif numargs == 1:
#             stop = args[0]
#             start = 0
#             step = 1
#         elif numargs == 2:
#             (start, stop) = args
#             step = 1
#         elif numargs == 3:
#             (start, stop, step) = args
#         else: raise TypeError('inclusive_range expected at most three arguments, got {}.format(numargs)')
#         i = start
#         while i <= stop:
#             yield i
#             i += step
#
# if __name__ == "__main__": main()

##
## 12. Classes
##

##
## Understanding classes and objects
##


# The classes themselves are the
# blueprint for how an object is created.
#
# An object is an instance of a class.

##
## Using Methods
##

# Methods are functions, but within the object
# (self) is reference to the object, not the class
# Constructor __init__(self):


# Methods are functions, but within the object
# (self) is reference to the object, not the class
# Constructor __init__(self):


# class Duck:
#     def __init__(self, value):
#         # print('constructor')
#         self._v = value
#     def quack(self):
#         print('Quaaack!', self._v)
#
#     def walk(self):
#         print('walk like a duck.', self._v)
#
# def main():
#     donald = Duck(57)
#     frank = Duck(115)
#     donald.quack() # The empty parenthesis is as if donald was in them.
#     donald.walk()
#     frank.quack()
#     frank.walk()
#
# if __name__ == "__main__": main()

##
## Using Object Data
##

# class Duck:
#     def __init__(self, color = 'white'):
#         self._color = color
#
#
#     def quack(self):
#         print('Quaaack!')
#
#     def walk(self):
#         print('walk like a duck.')
#
# def main():
#     donald = Duck()
#     donald.quack()
#     donald.walk()
#
# if __name__ == "__main__": main()

# class Duck:
#     def __init__(self, **kwargs):
#         self.variables = kwargs
#     
#     def quack(self):
#         print('Quaaack!')
# 
#     def walk(self):
#         print('Walks like a duck.')
#
#     def set_variable(self, k, v):
#         self.variables[k] = v
# 
#     def get_variable(self, k):
#         return self.variables.get(k, None)
# 
# def main():
#     donald = Duck(feet = 2)
#     donald.set_variable('color', 'blue')
#     print(donald.get_variable('feet'))
#     print(donald.get_variable('color'))
# 
#
#
# if __name__ == "__main__": main()

##
## Understanding Inheritance
##

# class Animal:
#     def talk(self): print('I have something to say!')
#     def walk(self): print('Hey! I''m walkin'' here!')
#     def clothes(self): print('I have nice clothes')
#
# class Duck(Animal):
#     def quack(self):
#         print('Quaaack!')
#
#     def walk(self):
#         super().walk() # super() tells it to add in the parent def
#         print('walk like a duck.')
#
# class Dog(Animal):
#     def clothes(self):
#         print('I have brown and white fur')
#
# def main():
#     donald = Duck()
#     donald.quack()
#     donald.walk()
#     donald.clothes()
#
#     fido = Dog()
#     fido.walk()
#     fido.clothes()
#
#
# if __name__ == "__main__": main()

##
## Applying Polymorphism to classes
##

# class Duck():
#     def quack(self):
#         print('Quaaack!')
#
#     def walk(self):
#         print('walk like a duck.')
#
#     def bark(self):
#         print('The duck can not bark')
#
#     def fur(self):
#         print('The duck has feathers')
#
# class Dog():
#     def bark(self):
#         print('Woof!')
#
#     def walk(self):
#         print('Walks like a dog')
#
#     def fur(self):
#         print('The dog has brown and white fur')
#
#     def quack(self):
#         print('Dog can not quack')
#
# def main():
#     donald = Duck()
#     fido = Dog()
#     in_the_forest(donald)
#     in_the_pond(fido)
#
# def in_the_forest(dog):
#     dog.bark()
#     dog.fur()
#
# def in_the_pond(duck):
#     duck.quack()
#     duck.walk()
#
#     # for o in (donald, fido):
#     #     o.quack()
#     #     o.walk()
#     #     o.bark()
#     #     o.fur()
#
# if __name__ == "__main__": main()

##
## Using Generators
##

# class inclusive_range:
#     def __init__(self, *args):
#         numargs = len(args)
#         if numargs < 1: raise TypeError('requires at least one argument')
#         elif numargs == 1:
#             self.stop = args[0]
#             self.start = 0
#             self.step = 1
#         elif numargs == 2:
#             (self.start, self.stop) = args
#             self.step = 1
#         elif numargs == 3:
#             (self.start, self.stop, self.step) = args
#         else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))
#            
#            
#     def __iter__(self):
#         i = self.start
#         while i <= self.stop:
#             yield i
#             i += self.step
#
# def main():
#     for i in inclusive_range(25): print(i, end = ' ')
#
# if __name__ == "__main__": main()

##
## Using decorators
##

# Decorators are special functions that return other functions and they are used to modify the way that a function works

# class Duck:
#     def __init__(self, **kwargs):
#         self.properties = kwargs
#
#     def quack(self):
#         print('Quaaack!')
#
#     def walk(self):
#         print('Walks like a duck')
#
#     def get_properties(self):
#         return self.properties
#
#     def get_property(self, key):
#         return self.properties.get(key, None)
#
#     @property # This is an accessor
#     def color(self):
#         return self.properties.get('color', None)
#
#     @color.setter
#     def color(self, c):
#         self.properties['color'] = c
#
#     @color.deleter
#     def color(self):
#         del self.properties['color']
#
# def main():
#     donald = Duck()
#     donald.color = 'orange'
#     print(donald.get_property('color'))
#
# if __name__ == "__main__": main()

##
## 13. String Methods
##

# >>> 'This is a string'
# 'This is a string'
# >>> s = 'This is a string'
# >>> s
# 'This is a string'
# >>> s.upper()
# 'THIS IS A STRING'
# >>> 'This is a string'.upper()
# 'THIS IS A STRING'
# >>> 'I am not shouting'.upper()
# 'I AM NOT SHOUTING'
# >>>
# >>> 'This is a string {}'.format(42)
# 'This is a string 42'
# >>> 'This is a string %d' % 42
# 'This is a string 42'

##
## Working with common string methods
##

# >>> s = "this is a string"
# >>> s
# 'this is a string'
# >>> s.capitalize()
# 'This is a string'
# >>> s.upper()
# 'THIS IS A STRING'
# >>> s.lower()
# 'this is a string'
# >>> 'THIS IS A STRING.'.lower()
# 'this is a string.'
# >>> 'tHIS iS A String'.swapcase()
# 'This Is a sTRING'
# >>> s
# 'this is a string'
# >>> s.find('is')
# 2
# >>> s.find('ring')
# 12
# >>> s.replace('this', 'that')
# 'that is a string'
# >>> id(s)
# 50861504
# >>> newstring = s.upper()
# >>> newstring
# 'THIS IS A STRING'
# >>> id(newstring)
# 53427568
# >>> s.strip()
# 'this is a string'
# >>> '	This is a string      '.strip()
# 'This is a string'
# >>> '	this is a string      '.rstrip()
# '\tthis is a string'
# >>> '	this is a string      '.rstrip()
# '\tthis is a string'
# >>> s1 = 'this is a string\n'
# >>> s1
# 'this is a string\n'
# >>> s1.strip()
# 'this is a string'
# >>> s1.rstrip('\n')
# 'this is a string'
# >>> s.isalnum()
# False
# >>> 'thisisastring'.isalnum()
# True
# >>> 'thisisastring'.isalpha()
# True
# >>> '12345'.isdigit()
# True
# >>> s.isdigit()
# False
# >>> s.isprintable()
# True
# >>>

##
## Formatting Strings with str.format
##

# >>> a, b = 5, 42
# >>> print(a, b)
# 5 42
# >>> 'this is {}, that is {}'.format(a, b)
# 'this is 5, that is 42'
# >>> s = 'this is {}, that is {}'
# >>> s
# 'this is {}, that is {}'
# >>> s.format(a,b)
# 'this is 5, that is 42'
# >>> id(s)
# 53831200
# >>> new = s.format(a, b)
# >>> id(new)
# 53831104
# >>> 'this is %d, that is %d' % ( a,b )
# 'this is 5, that is 42'
# >>> 'this is {}, that is {}'.format(b, a)
# 'this is 42, that is 5'
# >>> 'this is {1}, that is {0}'.format(a, b)
# 'this is 42, that is 5'
# >>> 'this is {1}, that is {0}, this too is {1}'.format(a, b)
# 'this is 42, that is 5, this too is 42'
# >>> 'this is {bob} and that is {fred}'.format(bob = a, fred = b)
# 'this is 5 and that is 42'
# >>> d = dict(bob = a, fred = b)
# >>> 'this is {bob} and that is {fred}'.format(**d)
# 'this is 5 and that is 42'
# >>>

##
## Splitting and joining strings
##

# >>> s = 'This is a string of words'
# >>> s.split()
# ['This', 'is', 'a', 'string', 'of', 'words']
# >>> 'This     is     a     string      of      words'.split()
# ['This', 'is', 'a', 'string', 'of', 'words']
# >>> s.split('i')
# ['Th', 's ', 's a str', 'ng of words']
# >>> words = s.split()
# >>> words
# ['This', 'is', 'a', 'string', 'of', 'words']
# >>> for w in words: print(w)
#
#  This
#  is
#  a
#  string
#  of
#  words
#  >>> new = ':'.join(words)
#  >>> new
#  'This:is:a:string:of:words'
#  >>> ', '.join(words)
#  'This, is, a, string, of, words'
#  >>> 

##
## Finding and using standard string methods
##

# Python documentation: string methods

# >>> s = 'this is a string'
# >>> new = s.center(80)
# >>> new
# '                                this is a string                                '
# >>> len(new)
# 80
# >>>

##
## Creating sequences with tuples and lists 
##

# >>> t = 1,2,3,4,5
# >>> t
# (1, 2, 3, 4, 5)
# >>> t[0]
# 1
# >>> t[4]
# 5
# >>> t[-1]
# 5
# >>> len(t)
# 5
# >>> min(t)
# 1
# >>> max(t)
# 5
# >>> t = (1, 2, 3, 4, 5)
# >>> t = (1)
# >>> t
# 1
# >>> type(t)
# <class 'int'>
# >>> t = (1,)
# >>> x = [1,2,3,4,5]
# >>> type(x)
# <class 'list'>
# >>> x[0]
# 1
# >>> x[-1]
# 5
# >>> len(x)
# 5
# >>> t = tuple(range(25))
# >>> t
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
# >>> t[10] = 42
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     t[10] = 42
# TypeError: 'tuple' object does not support item assignment
# >>> x = list(range(25))
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# >>> type(x)
# <class 'list'>
# >>> x[10] = 42
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 42, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
# >>>

##
## Operating on sequences with built-in methods
##

# >>> t = tuple( range(25) )
# >>> t
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
# >>> type(t)
# <class 'tuple'>
# >>> 10 in t
# True
# >>> 50 in t
# False
# >>> 50 not in t
# True
# >>> t[10]
# 10
# >>> len(t)
# 25
# >>> for i in t: print(i)
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# >>> x = list(range(20))
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> 10 in x
# True
# >>> 20 in x
# False
# >>> for i in x: print(i)
# 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# >>> t[10] = 25
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     t[10] = 25
# TypeError: 'tuple' object does not support item assignment
# >>> x[10] = 25
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> t.count(5)
# 1
# >>> t.index(5)
# 5
# >>> t
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
# >>> t.append(100)
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     t.append(100)
# AttributeError: 'tuple' object has no attribute 'append'
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> x.append(100)
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
# >>> len(x)
# 21
# >>> x.extend(range(20))
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> x.insert(0, 25)
# >>> x
# [25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> x.insert(12, 100)
# >>> 
# >>> x
# [25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> x.remove(12)
# >>> x
# [25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 100, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> del x[12]
# >>> x
# [25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# >>> x.pop()
# 19
# >>> x
# [25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# >>> x.pop(0)
# 25
# >>> x
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 25, 11, 13, 14, 15, 16, 17, 18, 19, 100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# >>> 

##
## Organizing data with dictionaries
## 

# >>> d = { 'one': 1, 'two': 2, 'three': 3}
# >>> d
# {'two': 2, 'three': 3, 'one': 1}
# >>> d = dict( one = 1, two = 2, three = 3 )
# >>> d
# {'two': 2, 'three': 3, 'one': 1}
# >>> x = dict(four = 4, five = 5, six = 6)
# >>> x
# {'five': 5, 'four': 4, 'six': 6}
# >>> d = dict( one  1, two = 2, three = 3, **x )
# SyntaxError: invalid syntax
# >>> d = dict( one = 1, two = 2, three = 3, **x )
# >>> d
# {'five': 5, 'four': 4, 'six': 6, 'two': 2, 'three': 3, 'one': 1}
# >>> 'four' in x
# True
# >>> 'three' in x
# False
# >>> for k in d: print(k)
# 
# five
# four
# six
# two
# three
# one
# >>> for k, v in d.items(): print(k, v)
# 
# five 5
# four 4
# six 6
# two 2
# three 3
# one 1
# >>> d['three']
# 3
# >>> x['three']
# Traceback (most recent call last):
#   File "<pyshell#17>", line 1, in <module>
#     x['three']
# KeyError: 'three'
# >>> x.get('three')
# >>> 
# >>> 
# >>> d.get('three')
# 3
# >>> x.get('three', 'not found')
# 'not found'
# >>> x
# {'five': 5, 'four': 4, 'six': 6}
# >>> del x['four']
# >>> x
# {'five': 5, 'six': 6}
# >>> x.pop('five')
# 5
# >>> x
# {'six': 6}
# >>> 

##
## Operating on character data with bytes and byte arrays 
##

# often used for converting strings
# Do not have the file with characters


# def main():
#     fin = open('utf8.txt', 'r', encoding = 'utf_8') # utf_8 tells Python to ignore default encoder and decode the file
#     fout = open('utf8.html', 'w')
#     outbytes = bytearray()  # bytearrays are mutable
#     for line in fin:
#         for c in line:
#             if ord(c) > 127:
#                 outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
#             else: outbytes.append(ord(c))
#     outstr = str(outbytes, encoding='utf_8')
#     print(outstr,  file = fout)
#     print(outstr)
#     print('Done.')
#
# if __name__ == "__main__": main()

##
## 15. File I/O
##

##
## Opening files
##

# def main():
#     f = open('lines.txt', 'r') # Write arguments r=read(default) w=write a=append  modifiers to R r+ = read/write  rt=text file mode or rb=binary mode
#     for line in f: # you can also use a method .readlines() which reads the line of text
#         print(line, end='')
#
# if __name__ == "__main__": main()

##
## Reading and Writing text Files
##

# def main():
#     infile = open('lines.txt', 'r')
#     outfile = open('new.txt', 'w')
#     for line in infile:
#         print(line, file = outfile, end = '')
#     print('done')
#
# if __name__ == "__main__": main()


# Reading bigger files using a buffer 

# def main():
#     buffersize = 50000 
#     infile = open('bigfile.txt', 'r')
#     outfile = open('new.txt', 'w')
#     buffer = infile.read(buffersize)
#     while len(buffer):
#         outfile.write(buffer)
#         print('.', end = '')
#         buffer = infile.read(buffersize)
#     print()
#     print('done')
#
# if __name__ == "__main__": main()

##
## Reading and Writing Binary Files
##

# def main():
#     buffersize = 50000
#     infile = open('olives.jpg', 'rb')
#     outfile = open('new.jpg', 'wb')
#     buffer = infile.read(buffersize)
#     while len(buffer):
#         outfile.write(buffer)
#         print('.', end = ' ')
#         buffer = infile.read(buffersize)
#     print()
#     print('Done.')
# 
# if __name__ == "__main__": main()

##
## Databases
##

##
## Creating a database with SQLite 3
##

# import sqlite3
# 
# def main():
#     db = sqlite3.connect('test.db')  #connects to the database (if it doesn't exist)
#     db.execute('drop table if exists test') #db.execute is the object with which we interact
#     db.execute('create table test(t1 text, i1 int)')
#     db.execute('insert into test(t1, i1) values(?, ?)', ('one', 1))
#     db.execute('insert into test(t1, i1) values(?, ?)', ('two', 2))
#     db.execute('insert into test(t1, i1) values(?, ?)', ('three', 3))
#     db.execute('insert into test(t1, i1) values(?, ?)', ('four', 4))
#     db.commit() # after you change any data, you commit()
#     cursor = db.execute('select * from test order by t1') #use the cursor object to step through as an iterator to print the data, you can change '*' to i1, t1 if you want them printed in that order. 
#     for row in cursor:
#         print(row) #data returns in tuples 
#
# if __name__ == "__main__": main()
# 
# Using row factory to return them as a dictionary is very useful:

# import sqlite3
#
# def main():
#    db = sqlite3.connect('test.db')
#    db.row_factory = sqlite3.Row
#    db.execute('drop table if exists test')
#    db.execute('create table test(t1 text, i1 int)')
#    db.execute('insert into test(t1, i1) values(?, ?)', ('one', 1))
#    db.execute('insert into test(t1, i1) values(?, ?)', ('two', 2))
#    db.execute('insert into test(t1, i1) values(?, ?)', ('three', 3))
#    db.execute('insert into test(t1, i1) values(?, ?)', ('four', 4))
#    db.commit()
#    cursor = db.execute('select i1, t1 from test order by t1')
#    for row in cursor:
#        print(dict(row))

# if __name__ == "__main__": main()
