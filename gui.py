from tkinter import *

tuscia = ""

def paspaudimas(skaicius):
    global tuscia
    tuscia = tuscia + str(skaicius)
    stringas.set(tuscia)

def lygu():
    try:
        global tuscia
        striwar = str(eval(tuscia))
        stringas.set(striwar)
        tuscia = ""
    except:
        stringas.set("klaida")
        tuscia = ""

def isvalyti():
    global tuscia
    tuscia = ""
    stringas.set("")

langas = Tk()
langas.configure()
langas.title("Skaiciuotuvas")

stringas = StringVar()

tuscia_field = Entry(langas, textvariable=stringas)
tuscia_field.grid(columnspan=4, ipadx=70)

mygtukas1 = Button(langas, text="1", command=lambda: paspaudimas(1), height=1, width=7)
mygtukas1.grid(row=2, column=0)
mygtukas2 = Button(langas, text="2", command=lambda: paspaudimas(2), height=1, width=7)
mygtukas2.grid(row=2, column=1)
mygtukas3 = Button(langas, text="3", command=lambda: paspaudimas(3), height=1, width=7)
mygtukas3.grid(row=2, column=2)
mygtukas4 = Button(langas, text="4", command=lambda: paspaudimas(4), height=1, width=7)
mygtukas4.grid(row=3, column=0)
mygtukas5 = Button(langas, text="5", command=lambda: paspaudimas(5), height=1, width=7)
mygtukas5.grid(row=3, column=1)
mygtukas6 = Button(langas, text=' 6 ', command=lambda: paspaudimas(6), height=1, width=7)
mygtukas6.grid(row=3, column=2)
mygtukas7 = Button(langas, text=' 7 ', command=lambda: paspaudimas(7), height=1, width=7)
mygtukas7.grid(row=4, column=0)
mygtukas8 = Button(langas, text=' 8 ', command=lambda: paspaudimas(8), height=1, width=7)
mygtukas8.grid(row=4, column=1)
mygtukas9 = Button(langas, text=' 9 ', command=lambda: paspaudimas(9), height=1, width=7)
mygtukas9.grid(row=4, column=2)
mugtukas0 = Button(langas, text=' 0 ', command=lambda: paspaudimas(0), height=1, width=7)
mugtukas0.grid(row=5, column=0)
plusas = Button(langas, text=' + ', command=lambda: paspaudimas("+"), height=1, width=7)
plusas.grid(row=2, column=3)
minusas = Button(langas, text=' - ', command=lambda: paspaudimas("-"), height=1, width=7)
minusas.grid(row=3, column=3)
dauginti = Button(langas, text=' * ', command=lambda: paspaudimas("*"), height=1, width=7)
dauginti.grid(row=4, column=3)
dalinti = Button(langas, text=' / ',  command=lambda: paspaudimas("/"), height=1, width=7)
dalinti.grid(row=5, column=3)
lygus = Button(langas, text=' = ', command=lygu, height=1, width=7)
lygus.grid(row=5, column=2)
isvalys = Button(langas, text='Isvalyti', command=isvalyti, height=1, width=7)
isvalys.grid(row=5, column=1)
taskas = Button(langas, text='.', command=lambda: paspaudimas('.'), height=1, width=7)
taskas.grid(row=6, column=0)
langas.mainloop()
