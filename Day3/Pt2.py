import re

def process_memory(memory):
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    control_pattern = re.compile(r"(do\(\)|don\'t\(\))")

    total = 0
    enabled = True  

    for line in memory.split(" "):
        control_match = control_pattern.search(line)
        if control_match:
            if control_match.group() == "do()":
                enabled = True
            elif control_match.group() == "don't()":
                enabled = False

        mul_match = mul_pattern.search(line)
        if mul_match and enabled:
            x = int(mul_match.group(1))  
            y = int(mul_match.group(2))  
            total += x * y 

    return total

with open("/Users/dorislam/AdventofCode2024-1/Day3/test.txt", "r") as data:
    content = [line.strip() for line in data.readlines()]

memory = " ".join(content)

result = process_memory(memory)
print (result)
