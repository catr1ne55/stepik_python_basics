with open('dataset_24465_4.txt', 'r') as inp, open('copy.txt', 'w') as out:
        out.writelines(reversed(inp.readlines()))