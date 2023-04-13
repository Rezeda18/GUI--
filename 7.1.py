from PIL import Image, ImageFilter
def z1():
    name = Image.open("барби.jpg")
    name.show()

    print("Размер: ", name.size)
    print("Формат: ", name.format)
    print("Цветовая иодель: ", name.mode)
z1()

def z2():
    name = Image.open("барби.jpg")
    name = name.reduce(3)
    name.save("бэйби_барбе.jpg")

    name1 = name.transpose(Image.FLIP_TOP_BOTTOM)
    name1.save("барбе1.jpg")
    name2 = name.transpose(Image.FLIP_LEFT_RIGHT)
    name2.save("барбе2.jpg")
z2()

def z3():
    imgg = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

    for i in imgg:
        with Image.open(i) as img:
            img.load()

            imgg1 = img.filter(ImageFilter.EMBOSS)
            imgg1.show()
            imgg1.save("C:/ИзменённыеИзб/img" + i)
z3()

def z4():
    img = Image.open("1.jpg")
    watermark = Image.open("Вотермарка.png")
    watermark = watermark.reduce(15)

    img.paste(watermark,(1,3), watermark)
    img.save("img_watermark.png")

z4()