f = open("UA.txt", "a")
a = f.write("\nI Hope All Of You Are doing Well\n ")
print(a)
f.close()
f = open("UA.txt", "r+")
print(f.read())
f.write("\n Bye Bye")