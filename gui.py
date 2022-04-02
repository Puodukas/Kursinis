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


if __name__ == "__main__":
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

    button6 = Button(langas, text=' 6 ', command=lambda: paspaudimas(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(langas, text=' 7 ', command=lambda: paspaudimas(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(langas, text=' 8 ', command=lambda: paspaudimas(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(langas, text=' 9 ', command=lambda: paspaudimas(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(langas, text=' 0 ', command=lambda: paspaudimas(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(langas, text=' + ', command=lambda: paspaudimas("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(langas, text=' - ', command=lambda: paspaudimas("-"), height=1, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(langas, text=' * ', command=lambda: paspaudimas("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(langas, text=' / ',  command=lambda: paspaudimas("/"), height=1, width=7)
    divide.grid(row=5, column=3)
    equal = Button(langas, text=' = ', command=lygu, height=1, width=7)

    equal.grid(row=5, column=2)
    clear = Button(langas, text='Clear', command=isvalyti, height=1, width=7)
    clear.grid(row=5, column=1)
    Decimal = Button(langas, text='.', command=lambda: paspaudimas('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    langas.mainloop()
