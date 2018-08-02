Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.getcwd()
'/Users/aizh/Documents'
>>> os.chdir("/Users/aizh/Documents/GitHub/my_first_project")
>>> os.getcwd()
'/Users/aizh/Documents/GitHub/my_first_project'
>>> os.listdir(os.curdir)
['.DS_Store', '.git', 'myfile.txt', 'README.md']
>>> f = open("myfile.txt")
>>> text = f.read()
>>> f.close()
>>> print(text)
Apple
Orange
Watermelon 
Lemon
Apricot 
Cherry



>>> with open("myfile.txt") as f:
	text = f.read()

	
>>> print(text)
Apple
Orange
Watermelon 
Lemon
Apricot 
Cherry



>>> fruits = ["Plum", "Banana"]
>>> with open("myfile.txt", "w") as f:
	for fruit in fruits:
		f.write(fruit)
		f.write("\n")

		
4
1
6
1
>>> with open("myfile.txt") as f
SyntaxError: invalid syntax
>>> with open("myfile.txt") as f:
	text = f.read()

	
>>> print(text)
Plum
Banana

>>> with open("myfile.txt", "a") as f:
	print(["Apple", "Orange"], file = f)

	
>>> with open("myfile.txt", "a") as f:
	print("Apple", "Orange")

	
Apple Orange
>>> print(text)
Plum
Banana

>>> print("Apple", "Orange", file = f)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print("Apple", "Orange", file = f)
ValueError: I/O operation on closed file.
>>> with open("myfile.txt", "a" as f:
	      
SyntaxError: invalid syntax
>>> with open("myfile.txt", "a") as f:
	      print("Lemon", file = f)

	      
>>> print(text)
	      
Plum
Banana

>>> with open("myfile.txt") as f:
	      text = f.read()

	      
>>> print(text)
	      
Plum
Banana
['Apple', 'Orange']
Lemon

>>> Juice = ["Apple Juice", "Orange Juice", "Kiwi Juice"]
	      
>>> with open("myfile.txt", "w") as fobj:
	      for juicetype in juice:
	      fobj.write(juicetype)
	      
SyntaxError: expected an indented block
>>> f.write(juicetype)
	      
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    f.write(juicetype)
NameError: name 'juicetype' is not defined
>>> with open("myfile.txt", "w") as fobj:
	      for juicetype in Juice:
	      fobj.write(juicetype)
	      
SyntaxError: expected an indented block
>>> with open("myfile.txt", "w") as fobj:
	      for juicetype in Juice:
	      f.write(juicetype)
	      
SyntaxError: expected an indented block
>>> juice = ["Apple Juice", "Orange Juice", "Kiwi Juice"]
	      
>>> with open("myfile.txt", "w") as f:
	      for juicetype in juice:
	      f.write(fruit)
	      
SyntaxError: expected an indented block
>>> 
	      
>>> 
	      
>>> with open("myfile.txt") as f:
	text = f.read()

	      
>>> print(text)
	      
Plum
Banana
['Apple', 'Orange']
Lemon

>>> juice = ["Apple Juice", "Orange Juice", "Kiwi Juice"]
	      
>>> with open("myfile.txt", "w") as f:
	      for juicetype in juice:
		      f.write(juicetype)
		      f.write("\n")

	      
11
1
12
1
10
1
>>> 
	      
>>> print(text)
	      
Plum
Banana
['Apple', 'Orange']
Lemon

>>> with open("myfile.txt") as f:
	      text = f.read()

	      
>>> print(text)
	      
Apple Juice
Orange Juice
Kiwi Juice

>>> print(text)
	      
Apple Juice
Orange Juice
Kiwi Juice

>>> print(text.rstrip())
	      
Apple Juice
Orange Juice
Kiwi Juice
>>> print(rstrip(text))
	      
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print(rstrip(text))
NameError: name 'rstrip' is not defined
>>> for line in reversed(list(open("myfile.txt"))):
	      print(line.rstrip())

	      
Kiwi Juice
Orange Juice
Apple Juice
>>> print[::,text]
	      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print[::,text]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> string[:len(open("myfiles.txt")):-1]
	      
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    string[:len(open("myfiles.txt")):-1]
NameError: name 'string' is not defined
>>> string = "Hello World"
	      
>>> string = [::-1]
	      
SyntaxError: invalid syntax
>>> 
	      
>>> print(text)
	      
Apple Juice
Orange Juice
Kiwi Juice

>>> print(2:text)
	      
SyntaxError: invalid syntax
>>> print(2:len(text))
	      
SyntaxError: invalid syntax
>>> with open("myfile.txt") as f:
	      text = f.read()

	      
>>> print(text)
	      
Apple Juice
Orange Juice
Kiwi Juice

>>> for line in reversed(list(open("myfile.txt"))):
	      print(line.rstrip())

	      
Kiwi Juice
Orange Juice
Apple Juice
>>> 
	      
>>> def reverse(text):
	      text = text[::-1]
	      return text

	      
>>> print(text)
	      
Apple Juice
Orange Juice
Kiwi Juice

>>> s = "chocolate"
	      
>>> print (reverse(s))
	      
etalocohc
>>> print(3:s)
	      
SyntaxError: invalid syntax
>>> print(2::s)
	      
SyntaxError: invalid syntax
>>> print(text)
	      
Apple Juice
Orange Juice
Kiwi Juice

>>> print(reverse(text))
	      

eciuJ iwiK
eciuJ egnarO
eciuJ elppA
>>> 
	      
>>> for line in open("myfile.txt"):
	      print(reverse(line))

	      

eciuJ elppA

eciuJ egnarO

eciuJ iwiK
>>> 
