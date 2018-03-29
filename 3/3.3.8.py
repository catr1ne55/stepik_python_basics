import sys, re

pattern = r"\b(\w)(\w)(\w*)\b"
for line in sys.stdin:
    line = line.rstrip()
    subs = re.findall(pattern, line)
    if len(subs) > 0:
        line2 = re.sub(pattern, r"\2\1\3", line)
        print(line2)