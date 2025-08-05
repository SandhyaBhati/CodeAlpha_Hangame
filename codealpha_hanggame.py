import random

words = ['red',"green","blue","white","black","silver","orange","yellow","pink","beige","grey","purple",]

word = random.choice(words)
guessed = ['_'] * len(word)
tries = 6

print("🎮 Welcome to Color Hangman!")

while tries > 0 and '_' in guessed:
    print("\nColor Name:", ' '.join(guessed))
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
    print(f"\n🎉 You won! The Color was: {word}")
else:

    print(f"\n💀 You lost! The Color was: {word}")
