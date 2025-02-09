start_word = input()

vowels = 'AEIOUY'  # Гласные буквы верхнего регистра
consonant_count = 0
vowel_count = 0

for i in range(len(start_word)):
    # Если первый символ подстроки - гласная
    if start_word[i] in vowels:
        vowel_count += len(start_word) - i  # Количество подстрок, начинающихся с этой гласной
    else:
        consonant_count += len(start_word) - i  # Количество подстрок, начинающихся с этой согласной

print(f'Стюарт {consonant_count}' if consonant_count > vowel_count else f'Кевин {vowel_count}')
