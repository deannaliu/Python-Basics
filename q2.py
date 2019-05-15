import ast
import sys

reader = input()
try:
    temp = ast.literal_eval(reader)
except:
    print("None")
    sys.exit(0)

if isinstance(temp, int):
    print("int")
elif isinstance(temp, float):
    print("float")
else:
    print("None")
