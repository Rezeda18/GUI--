import os, csv
from PIL import Image

def z12():
    path = "C:/saffas/"
    new_path = "C:/saffas/newImg"
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for filename in os.listdir(path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img = Image.open(os.path.join(path,filename))
            new_filename = '1_' + filename
            img.save(os.path.join(new_path,new_filename))

def z3():
    total_expenses = 0
    with open('food.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        print('Нужно купить:')
        for row in reader:
            product, kol, price = row
            product_cost = int(kol) * int(price)
            total_expenses += int(product_cost)
            print(f'{product} - {kol} шт. за {price} руб.')

        print(f'Итоговая сумма:{total_expenses} руб.')''
z3()