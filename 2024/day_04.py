import aoc_lube
import re

def transpose_string(string):
    lines = string.splitlines()
    transposed = zip(*lines)
    return '\n'.join(''.join(row) for row in transposed)

def diagonalize_string(string):
    diagonals = str()
    lines = string.splitlines()
    n = len(lines)

    # From top right to top left
    for j in range(n-1, -1, -1):
        for i in range(n):
            if j > n-1:
                break
            diagonals += lines[i][j]
            j += 1
        diagonals += "\n"
    # From top left to bottom left
    for i in range(1, n):
        for j in range(n):
            if i > n-1:
                break
            diagonals += lines[i][j]
            i += 1
        diagonals += "\n"

    #from bottom right to bottom left
    for j in range(n-1, -1, -1):
        for i in range(n-1, -1, -1):
            if j > n-1:
                break
            diagonals += lines[i][j]
            j += 1
        diagonals += "\n"
    #from bottom left to top left
    for i in range(n-2, -1, -1):
        for j in range(n):
            if i < 0 :
                break
            diagonals += lines[i][j]
            i -= 1
        diagonals += "\n"
    return diagonals

RAW = aoc_lube.fetch(year=2024, day=4)

RAW_TRANSPOSED = transpose_string(RAW)

RAW_DIAGONALIZED = diagonalize_string(RAW)
XMAS_RE = re.compile(r"XMAS")

def part_one():
    total = 0
    for match in XMAS_RE.finditer(RAW):
        total += 1
    for match in XMAS_RE.finditer(RAW[::-1]):
        total += 1
    for match in XMAS_RE.finditer(RAW_TRANSPOSED):
        total += 1
    for match in XMAS_RE.finditer(RAW_TRANSPOSED[::-1]):
        total += 1
    for match in XMAS_RE.finditer(RAW_DIAGONALIZED):
        total += 1
    for match in XMAS_RE.finditer(RAW_DIAGONALIZED[::-1]):
        total += 1
    return total

def part_two():
    ...

part_one()
aoc_lube.submit(year=2024, day=4, part=1, solution=part_one)
# aoc_lube.submit(year=2024, day=4, part=2, solution=part_two)