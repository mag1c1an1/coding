import sys

lines = sys.stdin.readlines()

for i, line in enumerate(lines):
    f = ""
    if i != len(lines) - 1:
        f = f'"{line.rstrip()}",'
    else:
        f = f'"{line.rstrip()}"'
    print(f)
