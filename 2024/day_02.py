######################
####### PART 1 #######
######################

filename = "data"

safe_count = 0
reports = []

def is_safe(report):
    report = [int(x) for x in report]
    is_increasing = all(report[level] < report[level + 1] <= report[level] + 3 for level in range(len(report) - 1))
    is_decreasing = all(report[level] > report[level + 1] >= report[level] - 3 for level in range(len(report) - 1))
    return is_increasing or is_decreasing

with open(filename, "r") as f:
    for line in f:
        reports.append(line.strip().split())

for report in reports:
        if is_safe(report):
            safe_count += 1

print("Le résultat est : " + str(safe_count) + ".")

######################
####### PART 2 #######
######################

def is_almost_safe(report):
    if not is_safe(report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                return True
        return False
    return True

safe_count = 0
for report in reports:
    if is_almost_safe(report):
        safe_count += 1

print("Le nouveau résultat est : " + str(safe_count) + ".")
