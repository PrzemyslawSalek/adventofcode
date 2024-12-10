import re

pattern = r"mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\)"

with open("input.txt", "r") as file:
    result = 0
    do = True
    for line in file:
        line = line.strip()
        if not line:
            continue

        for match in re.finditer(pattern, line):
            if match.group(1) and match.group(2) and do is True:
                num1, num2 = map(int, match.groups())
                result += num1 * num2
            elif match.group(0) == "do()":
                do = True
            elif match.group(0) == "don't()":
                do = False

print(result)