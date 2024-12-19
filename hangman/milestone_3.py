def ask_for_input():
  guess.lower()
  while True:
   guess = input("please guess a single letter: \t")
   if guess.isalpha() and len(guess) == 1:
      break
   else:
      print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
  if guess in word:
    print(f"Good guess!{guess} is in the word")
  else:
    print(f"Sorry, {guess} is not in the word. Try again!")
