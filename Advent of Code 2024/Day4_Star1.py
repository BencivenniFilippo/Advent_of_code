# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!
# 
# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.
# 
# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
# 
# 
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:
# 
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:
# 
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?


def count_xmas_occurrences(grid):
    # (row, col)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-Right
        (1, -1), # Down-Left
        (-1, 1), # Up-Right
        (-1, -1) # Up-Left
    ]
    
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(start_row, start_col, direction):
        for i in range(word_length):
            new_row = start_row + direction[0] * i
            new_col = start_col + direction[1] * i
            if not is_valid(new_row, new_col) or grid[new_row][new_col] != word[i]:
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            for direction in directions:
                if check_direction(row, col, direction):
                    count += 1

    return count

with open('input_4.txt', 'r') as file:
    lines = file.readlines()

grid = [list(line.strip()) for line in lines]

print(count_xmas_occurrences(grid))