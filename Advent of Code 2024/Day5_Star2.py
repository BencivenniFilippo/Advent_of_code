# --- Part Two ---
# While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.
# 
# For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:
# 
# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13.
# After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.
# 
# Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?


def find_wrong_updates(rules, updates):

    wrong_update = []
    
    for update in updates:

        for rule in rules:
            x,y = rule
            if x in update and y in update:

                if update.index(x) > update.index(y):
                    wrong_update.append(update)
                    break

    return wrong_update


def fix_wrong_update(updates):
    





with open('input_test.txt', 'r') as file:
    lines = file.readlines()

# Split the lines into two groups based on the blank line
blank_line_index = lines.index('\n')  # Find the index of the blank line
group1_lines = lines[:blank_line_index]
group2_lines = lines[blank_line_index + 1:]

# Process the first group into a list of tuples
rules = []
for line in group1_lines:
    X, Y = map(int, line.split('|'))
    rules.append((X, Y))

# Process the second group into a list of lists
updates = [list(map(int, line.split(','))) for line in group2_lines]

print(fix_wrong_update(find_wrong_updates(rules, updates)))