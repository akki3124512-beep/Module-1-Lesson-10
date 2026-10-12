word = input("Enter a word: ")
letter = input("Enter a letter: ")
sum = 0
for i in word:
  if i == letter:
    sum = sum+1
print("There are", sum, letter,"'s in your word.")