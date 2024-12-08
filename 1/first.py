list1 = []
list2 = []


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

    count2 = 0
    if len(list2) == 0:
        list2.insert(0, num[1])
    else:
        for idx, x in enumerate(list2):
            if x >= num[1]:
                break
            count2+=1
        list2.insert(count2, num[1])

result = 0
for idx, x in enumerate(list1):
    result = result + (abs(list1[idx] - list2[idx]))

print(result)