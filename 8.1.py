from PIL import Image, ImageFilter, ImageDraw, ImageFont
def z1():
    name = Image.open("открытка.jpg")
    name.show()

    name_1 = name.crop((10, 20, 80, 100))
    name_1.show()
    name_1.save("ОбрезкаФото.png")
z1()

def z2():
    name_holiday = {"День победы":"9 мая.jpg",
                    "8 Марта":"8 марта.jpg",
                    "23 Февраля":"23 февраля.jpg",
                    "День знаний":"1 сентября.jpg",
                    "Новый год":"31 декабря.jpg"}

    for key in sorted(name_holiday):
        print(key, ' - ', name_holiday[key])
    name = input('Окрытку на какой праздник вы бы хотели увидеть? : ')
    if name in name_holiday:
        im = Image.open(name_holiday[name])
        im.show()
    else:
        print("Такой открытки нет(")
z2()

def z3():
    img = Image.open("3ZaD.jpg")
    name = input("Как вас зовут?: ")
    font = ImageFont.truetype("arial_bold.ttf", 50)
    drawer = ImageDraw.Draw(img)
    drawer.text((260,200), name + ", поздравляю!", font = font, fill = "violet")

    img.save("Поздравление.jpg")
    img.show()
z3()