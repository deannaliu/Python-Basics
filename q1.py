import keyword
import re

reader = input()
special = re.compile('[@!#$%^&*()<>?/\|}{~:]')

if reader.isidentifier() and not keyword.iskeyword(reader):
    print("True")
else:
    print ("False")

