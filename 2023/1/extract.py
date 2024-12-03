######################
####### PART 1 #######
######################
with open('data') as f:
    lines = f.read().splitlines()

digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result_lines = []

for line in lines:
    kept_line = []
    for caracter in line:
        if caracter in digit:
            kept_line.append(caracter)
    calibration_value = int(kept_line[0]) * 10 + int(kept_line[-1])
    result_lines.append(calibration_value)

sum_results = sum(result_lines)
print("Le résultat est : " + str(sum_results))

######################
####### PART 2 #######
######################

digit_letters = {'zerone': '01', 'oneight': '18', 'twone': '21', 'threeight': '38', 'fiveight': '58',  'sevenine' : '79', 'eightwo': '82', 'eighthree': '83', 'nineight': '98',
                 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
                 }
result_lines_replaced = []

def replace_digit(line):
    line_replaced = line
    for str_digit in digit_letters.keys():
        line_replaced = line_replaced.replace(str_digit, digit_letters[str_digit])
    return line_replaced

for line in lines:
    print(line)
    line_replaced = replace_digit(line)
    print(line_replaced)
    kept_line = []
    for caracter in line_replaced:
        if caracter in digit:
            kept_line.append(caracter)
    print(kept_line)
    calibration_value = int(kept_line[0]) * 10 + int(kept_line[-1])
    print(calibration_value)
    result_lines_replaced.append(calibration_value)

sum_results = sum(result_lines_replaced)
print("Le résultat est : " + str(sum_results))

