vowels = 'aeiouAEIOU'
print("enter any text in English:")
user_input = input(">")
vowel_letters = []
consonant_letters = []
for letter in user_input:
    if letter in vowels:
        vowel_letters.append(letter)
    elif letter.isalpha():
        consonant_letters.append(letter)
result = (
    ''.join(vowel_letters),
    len(vowel_letters),
    ''.join(consonant_letters) 
)

print("Result:")
print(f"1. Vowel letters: {result[0]}")
print(f"2. Number of vowels: {result[1]}")
print(f"3. Consonant letters: {result[2]}")
