x = 1
y = 1
obstaclex = 2
obstacley = 2

while True:
    command = input("Rover moves: ").strip().lower()

    next_x = x
    next_y = y

    if command == "quit":
        break

    elif command == "up":
        next_y -= 1

    elif command == "down":
        next_y += 1

    elif command == "left":
        next_x -= 1

    elif command == "right":
        next_x += 1

    else:
        print("Use up, down, left or right")
        continue


    if next_x == obstaclex and next_y == obstacley:
        print ("OBSTACLE AHEAD!!")
    else:
        x = next_x
        y = next_y


    if x < 0:
        x = 0
    if x > 3:
        x = 3
    if y < 0:
        y = 0
    if y > 3:
        y = 3


    print("Position:", x, y)


    grid = [
        [".",".",".","."],
        [".",".",".","."],
        [".",".",".","."],
        [".",".",".","."]
    ]

    grid[obstacley][obstaclex] = "#"
    grid[y][x] = "R"

    for row in grid:
        print(row)

    print()
