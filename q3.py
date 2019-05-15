# Mei  Deanna Liu
# 111041152

import sys
line1 = input()
line2 = input()

result1 = True
result2 = True
if not line1 and not line2:
    print(False)
    sys.exit(0)

counter = 0

if line1 and line2:  # if there are two lines
    if line1.endswith('\\') and ((line1.startswith('\'') and line2.endswith('\'')) or (line1.startswith('\"') and line2.endswith('\"'))):
        linex = line1
        liney = line2
        line1 = line1[1:-1]  # take away the quotes and the ending \
        line2 = line2[0:-1]  # take away the ending of the second line
        previous = "a"  # a random letter
        for x in line1:
            if x == '\"' or x == '\'' or x == '\\':
                if previous == "\\" or (linex.startswith('\'') and x == '\"') or (linex.startswith('\"') and x == '\''):
                    result1 = True
                    counter = 2
                else:
                    result1 = False
            if counter == 2:
                counter = 0
                previous = ""
            else:
                previous = x
        previous = "a" # a random letter
        for x in line2:
            if x == '\"' or x == '\'' or x == '\\':
                if previous == "\\" or (linex.startswith('\'') and x == '\"') or (linex.startswith('\"') and x == '\''):
                    result2 = True
                    counter = 2
                else:
                    result2 = False
            if counter == 2:
                counter = 0
                previous = ""
            else:
                previous = x
    else:
        result1 = False
else: # if one of the lines are not there
    if not line2 and (line1.startswith('\'') and line1.endswith('\'')) or (line1.startswith('\"') and line1.endswith('\"')):
        linex = line1
        line1 = line1[1:-1]  # take away the quotes
        previous = "a"  # a random letter
        for x in line1:
            if x == '\"' or x == '\'' or x == '\\':
                if previous == "\\" or (linex.startswith('\'') and x == '\"') or (linex.startswith('\"') and x == '\''):
                    result1 = True
                    counter = 2
                else:
                    result1 = False
            if counter == 2:
                counter = 0
                previous = ""
            else:
                previous = x
    elif not line1 and (line2.startswith('\'') and line2.endswith('\'')) or (line2.startswith('\"') and line2.endswith('\"')): #line 1 is nothing
        liney = line2
        line2 = line2[1:-1]  # take away the quotes
        previous = "a"  # a random letter
        for x in line2:
            if x == '\"' or x == '\'' or x == '\\':
                if previous == "\\" or (liney.startswith('\'') and x == '\"') or (liney.startswith('\"') and x == '\''):
                    result2 = True
                    counter = 2
                else:
                    result2 = False
            if counter == 2:
                counter = 0
                previous = ""
            else:
                previous = x
    else:
        result1 = False
        result2 = False
print(result1 and result2)