with open("/Users/dorislam/AdventofCode2024-1/Day2/test.txt", "r") as data:
    content = [line.strip() for line in data.readlines()]

    safe = 0

    for line in content:
        report = list(map(int, line.split()))

        is_safe = True
        increasing = None
        
        for x in range(len(report) - 1):
            difference = abs(report[x] - report[x + 1])
            if not (1 <= difference <= 3): 
                is_safe = False
                break
            
            if report[x] < report[x + 1]:
                if increasing is None:
                    increasing = True
                elif increasing is False:
                    is_safe = False
                    break
            elif report[x] > report[x + 1]: 
                if increasing is None:
                    increasing = False
                elif increasing is True:
                    is_safe = False
                    break

        if is_safe:
            safe += 1
            continue  

        for x in range(len(report)):
            new_report = report[:x] + report[x+1:]
            increasing = None
            removal = True
            
            for y in range(len(new_report) - 1):
                difference = abs(new_report[y] - new_report[y + 1])
                if not (1 <= difference <= 3):  
                    removal = False
                    break

                if new_report[y] < new_report[y + 1]:  
                    if increasing is None:
                        increasing = True
                    elif increasing is False:
                        removal = False
                        break
                elif new_report[y] > new_report[y + 1]:  
                    if increasing is None:
                        increasing = False
                    elif increasing is True:
                        removal = False
                        break
            
            if removal:
                safe += 1
                break  

print (safe)
