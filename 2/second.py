result = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        numbers = list(map(int, line.split()))
        copy_numbers = numbers.copy()
        for i in range(len(numbers)):
            del copy_numbers[i]
            reverse = None
            correct = True
            for j in range(len(copy_numbers)):
                if j + 1 < len(copy_numbers):
                    if abs(copy_numbers[j] - copy_numbers[j+1]) >= 1 and abs(copy_numbers[j] - copy_numbers[j+1]) <= 3:
                        if copy_numbers[j+1] > copy_numbers[j] and (reverse is None or reverse is False):
                            reverse = False
                        elif copy_numbers[j+1] < copy_numbers[j] and (reverse is None or reverse is True):
                            reverse = True
                        else:
                            correct = False
                            continue
                    else:
                        correct = False
                        continue
            if correct is True:
                result += 1
                break
            copy_numbers = numbers.copy()

print(result)
