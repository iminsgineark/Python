print("Enter The Numbers Of Rows")
row = int(input())
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")
