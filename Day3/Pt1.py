import re

def process_memory(memory):
    matches = re.findall(r"mul\((\d+),(\d+)\)", memory)
    
    total = 0
    
    for match in matches:
        x = int(match[0])  
        y = int(match[1]) 
        total += x * y     
    return total

with open("/Users/dorislam/AdventofCode2024-1/Day3/test.txt", "r") as data:
    content = [line.strip() for line in data.readlines()]

memory = " ".join(content)

result = process_memory(memory)
print (result)
