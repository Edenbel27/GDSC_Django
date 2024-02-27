def is_palindrome(word):
  #Returns True if the word is a palindrome, False otherwise.
  return word == word[::-1]

def main():
  # Prompts the user for a word and prints whether it is a palindrome.
  word = input("Enter a word: ")
  if is_palindrome(word):
    print(word, "is a palindrome.")
  else:
    print(word, "is not a palindrome.")

if __name__ == "__main__":
  main()