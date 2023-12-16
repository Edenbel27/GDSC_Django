char = input("Enter a character: ")
for line in range(1, 6):
    if line % 2 == 0:
        print(char * line)
    else:
        print(char)