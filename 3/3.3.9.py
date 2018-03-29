import sys, re

pattern = r"\b(.*?)(\w)(\2+)(.*?)\b"
for line in sys.stdin:
    line = line.rstrip()
    subs = re.findall(pattern, line)
    if len(subs) > 0:
        line2 = re.sub(pattern, r"\1\2\4", line)
        print(line2)