list1 = []
counter = {}

while True:
    line = input()
    if not line:
        break
    num = list(map(int, line.split()))

    count1 = 0
    if len(list1) == 0:
        list1.insert(0, num[0])
    else:
        for idx, x in enumerate(list1):
            if x >= num[0]:
                break
            count1+=1
        list1.insert(count1, num[0])

    if num[1] in counter:
        counter[num[1]]+=1
    else:
        counter[num[1]] = 1

result = 0
for idx, x in enumerate(list1):
    result = result + (x * counter.get(x, 0))

print(result)