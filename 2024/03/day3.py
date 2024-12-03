######################
####### PART 1 #######
######################

import re

def process_mul_expressions(input_text):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_text)

    result = sum(int(x) * int(y) for x, y in matches)

    return result

filename = "data"
result = 0

with open(filename, "r") as f:
    for line in f:
        result += process_mul_expressions(line)

print("Le résultat est : " + str(result) + ".")

######################
####### PART 2 #######
######################

def process_mul_expressions_with_do_dont(input_text):
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, input_text)

    result = 0
    flag = True
    for match in matches:
        if match == "do()":
            flag = True
        elif match == "don't()":
            flag = False
        else:
            if flag:
                x, y = map(int, match[4:-1].split(','))
                result += x * y
    return result

result = 0
with open(filename, "r") as f:
    for line in f:
        result += process_mul_expressions_with_do_dont(line)

print("Le nouveau résultat est : " + str(result) + ".")