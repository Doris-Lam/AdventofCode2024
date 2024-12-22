with open("/Users/dorislam/AdventofCode2024-1/Day2/test", "r") as data:
    content = [line.strip() for line in data.readlines()]

    safe = 0
    is_safe = True
    
    for line in content:
        report = list(map(int, line.split()))
        for x in range(len(report)-1):
            difference = abs(report[x] - report[x+1])
            if 1 <= difference <= 3:
                safe = True
            else:
                safe = False

        if is_safe:
            safe+=1       

print (safe)

 