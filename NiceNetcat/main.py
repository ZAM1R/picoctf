import re
lines = []
with open("list.txt") as file_in:
    for line in file_in:
        lines.append(re.sub(r"[\n\t\s]*",'',line))

res = ''
for line in lines:
    res = res + chr(int(line))

print(res)
