kol = int(input('Введите количество слов, которое собираетесь ввести: '))
text = ''

for i in range(1, kol + 1):
    word = input()
    text = text + word + ' '
    word =''

print(text)