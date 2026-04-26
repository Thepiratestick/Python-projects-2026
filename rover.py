x = 1
y = 1

command = input("Rover moves: ").strip().lower()
if command == ("up"):
    y = y -1
elif command == ("down"):
    y = y +1
elif command == ("right"):
    x = x+1
elif command == ("left"):
    x = x-1
elif command == ("up+left"):
    x, y = x -1, y -1
elif command == ("down+left"):
    x, y = x -1, y +1
elif command == ("up+right"):
    x, y = x +1, y -1
elif command == ("down+right"):
    x, y = x +1, y +1
else: print ("please write either up, down, left or right for the rover to move")

grid = [
[".", ".", "."],
[".", ".", "."],
[".", ".", "."]
]

grid[y][x] = "R"

for row in grid:
    print(row)
