with open('input_5.txt', 'r') as f:
    data = [line.replace('[', ' ').replace(']', ' ').replace('\n', '') for line in f.readlines()]

grid = []
for i in range(0, 8):
    grid.append([])
    for j in range(1, len(data[0]), 4):
        
        if not data[i][j] == ' ':
            grid[i].append(data[i][j])

grid = [list(row) for row in zip(*grid[::-1])]

grid