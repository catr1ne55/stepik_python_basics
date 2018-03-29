objects = [1, 2, 1, 2, 3]
ans = []
for obj in objects:
    if obj not in ans:
        ans.append(obj)
print(len(ans))