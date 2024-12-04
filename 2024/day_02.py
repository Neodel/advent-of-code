import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=2)

REPORTS = []

def is_safe(report):
    report = [int(x) for x in report]
    is_increasing = all(report[level] < report[level + 1] <= report[level] + 3 for level in range(len(report) - 1))
    is_decreasing = all(report[level] > report[level + 1] >= report[level] - 3 for level in range(len(report) - 1))
    return is_increasing or is_decreasing

def is_almost_safe(report):
    if not is_safe(report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                return True
        return False
    return True

def part_one():
    safe_count = 0
    for line in RAW.split("\n"):
        REPORTS.append(line.split())

    for report in REPORTS:
        if is_safe(report):
            safe_count += 1

    return safe_count

def part_two():
    safe_count = 0
    for report in REPORTS:
        if is_almost_safe(report):
            safe_count += 1
    return safe_count

aoc_lube.submit(year=2024, day=2, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=2, part=2, solution=part_two)