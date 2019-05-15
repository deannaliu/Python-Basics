# Mei Deanna Liu
# 111041152

import datetime

reader = input()
sep = reader.split("/")

today = datetime.date(int(sep[2]), int(sep[0]), int(sep[1]))
print (today.strftime("%A, %B %-d, %Y"))