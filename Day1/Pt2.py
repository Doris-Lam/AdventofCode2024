with open("/Users/dorislam/AdventofCode2024-1/Day1/Pt1data", "r") as data:
    content = data.readlines()

left_list = []
right_list = []

for line in content:
    line = line.strip()
    if not line:
        continue
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

sum = 0

for x in left_list:
    for y in right_list:
        if x == y:
            sum += x

print (sum)


