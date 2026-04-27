x = 1
y = 1

while True:
    command = input("Rover moves: ").strip().lower()

    if command == "quit":
        break

    elif command == "up":
        y -= 1

    elif command == "down":
        y += 1

    elif command == "left":
        x -= 1

    elif command == "right":
        x += 1

    else:
        print("Use up, down, left or right")
        continue


    if x < 0:
        x = 0
    if x > 2:
        x = 2
    if y < 0:
        y = 0
    if y > 2:
        y = 2


    print("Position:", x, y)


    grid = [
        [".",".","."],
        [".",".","."],
        [".",".","."]
    ]

    grid[y][x] = "R"

    for row in grid:
        print(row)

    print()
