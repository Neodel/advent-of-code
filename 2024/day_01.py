import aoc_lube

RAW = aoc_lube.fetch(year=2024, day=1)

# Listes pour stocker les variables
list1 = []
list2 = []

def part_one():
    for line in RAW.split("\n"):
        part1, part2 = line.split()
        list1.append(int(part1))
        list2.append(int(part2))

    list1.sort()
    list2.sort()
    differences = [abs(a - b) for a, b in zip(list1, list2)]

    results = sum(differences)
    return results

def part_two():
    similarity_score = 0
    for item in list1: # lists already existing as global value
        similarity_score += (list2.count(item) * item)
    return similarity_score

aoc_lube.submit(year=2024, day=1, part=1, solution=part_one)
aoc_lube.submit(year=2024, day=1, part=2, solution=part_two)
