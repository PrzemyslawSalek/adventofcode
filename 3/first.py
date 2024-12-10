import re

pattern = r"mul\((\d+),\s*(\d+)\)"

with open("input.txt", "r") as file:
    result = 0

    for line in file:
        line = line.strip()
        if not line:
            continue

        for match in re.finditer(pattern, line):
            num1, num2 = map(int, match.groups())
            result += num1 * num2

print(result)