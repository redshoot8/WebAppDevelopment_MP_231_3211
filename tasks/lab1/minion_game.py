start_word = input()

vowels = 'AEIOUY'
consonant_count = 0
vowel_count = 0

for i in range(len(start_word)):
    if start_word[i] in vowels:
        vowel_count += len(start_word) - i
    else:
        consonant_count += len(start_word) - i

print(f'Стюарт {consonant_count}' if consonant_count > vowel_count else f'Кевин {vowel_count}')
