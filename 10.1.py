import json
def z12():
    with open('products.json', 'r', encoding='utf8') as file:
        data = json.load(file)
    for product in range(len(data['products'])):
        a = data['products'][product]
        print('Название: ' + str(a['name']))
        print('Цена: ' + str(a['price']))
        print('Вес: ' + str(a['weight']))
        if a['available'] == 'да':
            print('В наличии')
        else:
            print('Нет в наличии', '\n')
    plus = {}
    plus['name'] = input('Название продукта: ')
    plus['price'] = input('Цена: ')
    plus['weight'] = input('Вес: ')
    plus['available'] = input('Есть в наличии?(да/нет): ')

    data['products'].append(plus)

    with open('products.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
z12()


def z3():
    ru_en = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        for line in file:
            en_word, ru_words = line.strip().split('-')
            for ru_word in ru_words.split(', '):
                if ru_word not in ru_en:
                    ru_en[ru_word] = [en_word]
                else:
                    ru_en[ru_word].append(en_word)
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for ru_word in sorted(ru_en):
            en_words = ', '.join(sorted(ru_en[ru_word]))
            file.write(f'{ru_word} - {en_words}\n')
z3()


