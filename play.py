print("NUM\tDIV BY 2 OR 3")
print("---\t-------------")
for num in range(2, 21):
    if num % 2 == 0 and num % 3 == 0:
        print(num, "\tboth"
    elif num % 2 == 0:
        print(num, "\tdiv by 2")
    elif num % 3 == 0:
        print(num, "\tdiv by 3")
    else:
        print(num, "\tneither")

