num = int(input("Enter The Number"))
for i in range(num):
    print(" " * (num - i - 1),end="")
    print("*" * (2 * i + 1),end="")
    print(" " * (num - i - 1))