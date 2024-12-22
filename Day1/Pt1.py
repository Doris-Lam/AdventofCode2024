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

left_list.sort()
right_list.sort()

total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
print(total_distance)
