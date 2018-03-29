import os

dirr = []
for root, dirs, files in os.walk("/home/catr1ne55/main"):
    for file in files:
        if file.endswith(".py"):
            d = os.path.abspath(file)
            if d not in dirr:
                dirr.append(d)
dirr.sort()
print([di for di in dirr])