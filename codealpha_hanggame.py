import random

words = ['tiger', 'elephant', 'giraffe', 'lion', 'zebra', 'kangaroo',
         'monkey', 'panda', 'rabbit', 'cheetah', 'leopard', 'wolf',
         'fox', 'hippopotamus', 'rhinoceros', 'buffalo', 'deer', 'camel',
         'bear', 'donkey']

word = random.choice(words)
guessed = ['_'] * len(word)
tries = 6

print("🎮 Welcome to Animal Hangman!")

while tries > 0 and '_' in guessed:
    print("\nAnimal Name:", ' '.join(guessed))
    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
        print("✔️ Correct!")
    else:
        tries -= 1
        print(f"❌ Wrong! Tries left: {tries}")

if '_' not in guessed:
    print(f"\n🎉 You won! The animal was: {word}")
else:
    print(f"\n💀 You lost! The animal was: {word}")