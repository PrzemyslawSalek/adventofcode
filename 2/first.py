result = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        prev = None
        reverse = None
        correct = False
        for num in line.split():
            curr = int(num)
            if prev is not None:
                if abs(prev - curr) >= 1 and abs(prev - curr) <= 3:
                    if curr > prev and (reverse is None or reverse is False):
                        reverse = False
                        correct = True
                    elif curr < prev and (reverse is None or reverse is True):
                        reverse = True
                        correct = True
                    else:
                        correct = False
                        break
                else:
                    correct = False
                    break
            prev = curr
        if correct is True:
            result += 1

print(result)


