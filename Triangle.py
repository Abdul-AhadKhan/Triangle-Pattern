rows = input("Enter the number of rows: ")
rows = int(rows)
start = rows - 1
end = rows + 1
for x in range(rows):
    for y in range(2 * rows - 1):
        if start - 1 < y < end - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
    start -= 1
    end += 1