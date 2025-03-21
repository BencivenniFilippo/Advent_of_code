# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?
# 
# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:
# 
# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.
# 
# Here's the same example from before, but this time all of the X-MASes have been kept instead:
# 
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.
# 
# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

def upLeft_downRight_Match(grid, row, col):
    # Checks both valid permutations: M-S or S-M
    return ((grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or
            (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'))

def upRight_downLeft_Match(grid, row, col):
    # Checks both valid permutations: M-S or S-M
    return ((grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S') or
            (grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M'))

def count_xmas_patterns(grid):
    count = 0
    # Traverse the grid, avoiding edges
    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            # Check for the 'A' at the center of an X
            if grid[row][col] == 'A':
                # Check both diagonals for valid X-MAS patterns
                if (upLeft_downRight_Match(grid, row, col) and
                    upRight_downLeft_Match(grid, row, col)):
                    count += 1
    return count

# . M . S . . . . . .
# . . A . . M S M S .
# . M . S . M A A . .
# . . A . A S M S M .
# . M . S . M . . . .
# . . . . . . . . . .
# S . S . S . S . S .
# . A . A . A . A . .
# M . M . M . M . M .
# . . . . . . . . . .

 
 # Import grid from file
with open('input_4.txt', 'r') as file:
    lines = file.readlines()

# Prepare the grid
grid = [list(line.strip()) for line in lines]

# Count occurrences of X-MAS patterns
print(count_xmas_patterns(grid))