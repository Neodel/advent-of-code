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

