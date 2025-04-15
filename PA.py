num_rows = int(input("Enter the number of rows :"))
row = 1
while row <= num_rows:
    col = 1
    while col <= row:
        print(row, end= "")
        col = col + 1
    print()
    row = row + 1