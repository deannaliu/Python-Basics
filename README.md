## Python Basics
* Python 3

### Program 1
* Reads a line from input and determines if it is a legal identifier.
  - A identifier starts with a letter A to Z or a to z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9), and it is not a keyword.
  - Keywords include: False, def, if, raise, None, del, import, return, True, elif, in, try, and, else, is, while, as, except, lambda, with, assert, finally, nonlocal, yield, break, for, not, class, from, or, continue, global, pass    
  
### Program 2
* Reads a line from input and determines if it is a legal number. 
* The program prints either int or float or None.
#### Example Input/Output
```
input: 10
output: int

input: 0o7289
output: None

input: 4.00000009000
output: float
```

### Program 3
* Reads two lines from input and determines if it is a legal string enclosed within single or double quotes.
* Escape Characters are accounted for as well.
#### Example Input/Output
```python
input line 1: ' " \\\\\\\\\\\\\\\\\\\\\\\\\\\\\"\
input line 2: testTesttest'
output: False

input line 1: ""
input line 2: 
output: True
```

### Program 4
* Reads a date in the format MM/DD/YYYY from input and print it out as Day, Month DD, Year. 
#### Example Input/Output
```
input: 02/08/2019
output: Friday, February 8, 2019.
```
