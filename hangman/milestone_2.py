import random
fruits = ["apple", "banana", "kiwi", "strawberry", "orange"]
word_list = fruits
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please select a random single letter")
print(guess)

if len(guess) == 1:
    print ("Good guess!")
else:
    print("Oops! That is not a valid input.")
