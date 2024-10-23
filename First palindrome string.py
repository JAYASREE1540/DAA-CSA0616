words = ["apple", "banana", "civic", "domino"]

for word in words:
    if word == word[::-1]:  # Check if the word is a palindrome
        print("First palindrome string:", word)
        break
else:
    print("No palindrome found")
