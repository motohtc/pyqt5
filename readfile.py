path = "test.py"
with open(path) as f:
    lines=f.readlines()
    for line in lines:
        print(line)