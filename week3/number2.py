char = input("Enter a character: ")
if len(char)!=1:
    print ('The length of character should be 1.')
elif char.lower() in ['a','e','i','o','u']:
    print ("Vowels are not allowed in the input.")
elif type(char)!=str:
    print('only characters are allowed to input.')
else:
    for line in range(1, 10):
        if line % 2 != 0:
            print(f'{char*line}')
        else:
            pass