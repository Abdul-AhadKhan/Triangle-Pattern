TriangleRows = input("Enter the rows for triangle: ")
TriangleRows = int(TriangleRows)
start = -1
end = 2 * TriangleRows - 1
for rows in range(TriangleRows):
    for cols in range(2 * TriangleRows - 1):
        if start < cols < end:
            print("*", end="")
        else:
            print(" ", end="")
    start = start + 1
    end = end - 1
    print()

