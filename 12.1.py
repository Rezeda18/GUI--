from tkinter import *
def z1():
    class Restaurant:
        def __init__(self, kafe, c_t):
            self.kafe = kafe
            self.c_t = c_t

        def describe_restaurant(self):
            print(f"Название кафе: {self.kafe}, кухня: {self.c_t}")
    class IceCreamStand(Restaurant):
        def __init__(self, kafe, c_t, flavors, time, local):
            super().__init__(kafe, c_t)
            self.flavors = flavors
            self.local = local
            self.time = time
        def doby(self):
            print("Виды:")
            print(*self.flavors, sep="\n")
        def noydoby(self):
            e = input()
            s.append(e)
            s.pop(0)
            print("Новый вид")
            print(*self.flavors, sep="\n")
        def proverka(self):
            e2 = input()
            for i in s:
                if e2 == i:
                    print("есть")
    class LOL(IceCreamStand):
        def __init__(self, kafe, c_t, flavors, time, local, vidupak):
            super().__init__(kafe, c_t, flavors, time, local)
            self.vidupak = vidupak
        def sss(self):
            self.vidupak = "пластиковая упаковка"
            print("Вид упаковки:")
            print(self.vidupak)
    class OL(IceCreamStand):
        def __init__(self, kafe, c_t, flavors, time, local, vidupaki):
            super().__init__(kafe, c_t, flavors, time, local)
            self.vidupaki = vidupaki
        def ss(self):
            self.vidupaki = "пломбир"
            print("Вкус:")
            print(self.vidupaki)
    s =["шоколадное", "клубничное"]
    p = IceCreamStand(" Ларек", "Мороженное ", s, "c 8:00 до 20:00", "Санкт-Петербург")
    x = LOL(" Ларек", "Мороженное ", s, "c 8:00 до 20:00", "Санкт-Петербург", " ")
    y = OL(" Ларек", "Мороженное ", s, "c 8:00 до 20:00", "Санкт-Петербург", " ")
    p.describe_restaurant()
    p.doby()
    p.noydoby()
    x.sss()
    y.ss()
    p.proverka()
z1()
def z3():
    class Restaurant:
        def __init__(self, kafe, c_t):
            self.kafe = kafe
            self.c_t = c_t

        def describe_restaurant(self):
            print(f"Название кафе: {self.kafe}, кухня: {self.c_t}")
    class IceCreamStand(Restaurant):
        def __init__(self, kafe, c_t, flavors, time, local):
            super().__init__(kafe, c_t)
            self.flavors = flavors
            self.local = local
            self.time = time
        def doby(self):
            print(*self.flavors, sep="\n")

        def noydoby(self):
            e = input()
            s.append(e)
            s.pop(0)
            print("Новое")
            print(*self.flavors, sep="\n")

    s = ["банановое", "мятное", "ванильное"]
    p = IceCreamStand(" Айскримация", "Мороженное ", s, "c 8:00 do 20:00", "Санкт-Петербург")
    p.describe_restaurant()
    p.doby()
    u = Tk()
    u['bg'] = "lightgreen"
    u.title("Мороженное")
    u.geometry('300x250')

    t = Label(u, text = "Виды мороженного", bg = "lightgreen", font = 35)
    t.place(relx=0.05, rely=0.05, relwidth=0.05, relheight=0.05)
    t.pack()

    for i in s:
           e = i
           o = Label(u, text=e, bg="lightgreen", font=29)
           o.pack()
    u.mainloop()
z3()
