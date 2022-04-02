import math , logging

def sudetis(x, y):
    return x + y
def atimtis(x, y):
    return x - y
def daugyba(x, y):
    return x * y
def dalyba(x, y):
    return x / y
def saknis(x):
    return math.sqrt(x)
def laipsnis(x):
    return ( x**y)
def pi(x):
    return math.pi * x
def sinusas(x):
    return math.sin(x)
def logiritmas(x):
    return math.log(x)
def cossinusas(x):
    return math.cos(x)
def desimtlaipsniu(x):
    return 10**x

while True:
    pasirinkimas = input("Iveskite pasirinkima \n 1: sudetis \n 2: atimtis \n 3: daugyba \n 4: dalyba \n 5: saknis "
                         "\n 6: kelimas laipsniu \n 7: π \n 8: sinusas \n 9: logoritmas \n 10: cosinusas \n 11: 10 pakelta laipsniu \n ")
    if pasirinkimas in ("1", "2", "3", "4", "5", "6", "7", "8","9","10","11" ):



        if pasirinkimas == '1':
            x = float(input("iveskite pirma skaiciu \n "))
            y = float(input("iveskite antra skaiciu \n "))
            print(x, "+", y, "=", sudetis(x, y))

        elif pasirinkimas == '2':
            x = float(input("iveskite pirma skaiciu \n "))
            y = float(input("iveskite antra skaiciu \n "))
            print(x, "-", y, "=", atimtis(x, y))

        elif pasirinkimas == '3':
            x = float(input("iveskite pirma skaiciu \n "))
            y = float(input("iveskite antra skaiciu \n "))
            print(x, "*", y, "=", daugyba(x, y))

        elif pasirinkimas == '4':
            x = float(input("iveskite pirma skaiciu \n "))
            y = float(input("iveskite antra skaiciu \n "))
            print(x, "/", y, "=", dalyba(x, y))
        elif pasirinkimas == '5' :
            x = float(input("iveskite  skaiciu \n "))
            print (x , "saknis", "=", saknis(x))
        elif pasirinkimas == '6':
            x = float(input("iveskite pirma skaiciu \n "))
            y = float(input("iveskite antra skaiciu \n "))
            print (x , "^", y , "=" , laipsnis(x))
        elif pasirinkimas == '7':
            x = float(input("iveskite  skaiciu \n "))
            print(x , "*", "π" , "=" , pi(x))
        elif pasirinkimas == '8':
            x = float(input("Iveskite skaiciu \n"))
            print(x , "sinusas", "=", sinusas(x) )
        elif pasirinkimas == "9":
            x = float(input("Iveskite skaiciu \n"))
            print(x, "logoritmas","=", logiritmas(x))
        elif pasirinkimas == "10":
            x = float(input("iveskite skaiciu \n"))
            print(x, "cossinusas", "=", cossinusas(x))
        elif pasirinkimas == "11":
            x = float(input("iveskite skaiciu \n"))
            print("10 ^",x, "=" , desimtlaipsniu(x))
