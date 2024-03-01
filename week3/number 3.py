word=input("Enter the word: ")
if word==word[::-1]:
  print(f'{word} is pallindrome.')
else:
  print(f'{word} is not pallindrome because {word} is not equal with {word[::-1]} ')


