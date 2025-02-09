with open('tasks/lab1/files/example.txt', encoding='UTF-8') as f:
    text = f.read().lower()

words = []
cur_word = ''
for char in text:
    if char.isalpha():
        cur_word += char
    elif char == ' ':
        words.append(cur_word)
        cur_word = ''

    if cur_word:
        words.append(cur_word)

words = list(sorted(words, key=lambda x: len(x)))
for word in words:
    if len(word) == len(words[-1]):
        print(word)
