import math , logging

logger = logging.getLogger(__name__)
file_handler =  logging.FileHandler('Skaiciuotuvo_logas.log')
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

formater = logging.Formatter('%(levelname)s:%(message)s')

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
def logoritmas(x):
    return math.log(x)
def cossinusas(x):
    return math.cos(x)
def desimtlaipsniu(x):
    return 10**x

while True:
    isjungimas = input("1: testi\n2: nustoti\n")

    if isjungimas == "1":
        pasirinkimas = input("Iveskite pasirinkima \n 1: sudetis \n 2: atimtis \n 3: daugyba \n 4: dalyba \n 5: saknis "
                             "\n 6: kelimas laipsniu \n 7: π \n 8: sinusas \n 9: logoritmas \n 10: cosinusas \n 11: 10 pakelta laipsniu \n ")
        if pasirinkimas in ("1", "2", "3", "4", "5", "6", "7", "8","9","10","11" ):



            if pasirinkimas == '1':
                x = float(input("iveskite pirma skaiciu \n "))
                y = float(input("iveskite antra skaiciu \n "))
                print(x, "+", y, "=", sudetis(x, y))
                sudeta = sudetis(x, y)
                logger.info(f"Sudetis: {x} + {y} ={sudeta}")

            elif pasirinkimas == '2':
                x = float(input("iveskite pirma skaiciu \n "))
                y = float(input("iveskite antra skaiciu \n "))
                print(x, "-", y, "=", atimtis(x, y))
                atimta = atimtis(x, y)
                logger.info(f"Atimtis: {x} - {y} ={atimta}")

            elif pasirinkimas == '3':
                x = float(input("iveskite pirma skaiciu \n "))
                y = float(input("iveskite antra skaiciu \n "))
                print(x, "*", y, "=", daugyba(x, y))
                dauginta = daugyba(x, y)
                logger.info(f"Daugyba: {x} * {y} ={dauginta}")

            elif pasirinkimas == '4':
                x = float(input("iveskite pirma skaiciu \n "))
                y = float(input("iveskite antra skaiciu \n "))
                print(x, "/", y, "=", dalyba(x, y))
                dalinta = daugyba(x, y)
                logger.info(f"Dalinta: {x} / {y} ={dalinta}")

            elif pasirinkimas == '5' :
                x = float(input("iveskite  skaiciu \n "))
                print (x , "√", "=", saknis(x))
                sakniss = saknis(x)
                logger.info(f"Saknis: {x}  ={sakniss}")

            elif pasirinkimas == '6':
                x = float(input("iveskite pirma skaiciu \n "))
                y = float(input("iveskite antra skaiciu \n "))
                print (x , "^", y , "=" , laipsnis(x))
                laipsnis1 = laipsnis(x)
                logger.info(f"Laipsnis: {x} ^ {y}  ={laipsnis1}")

            elif pasirinkimas == '7':
                x = float(input("iveskite  skaiciu \n "))
                print(x , "*", "π" , "=" , pi(x))
                pie = saknis(x)
                logger.info(f"Pi: {x} pi ={pie}")

            elif pasirinkimas == '8':
                x = float(input("Iveskite skaiciu \n"))
                print(x , "sinusas", "=", sinusas(x) )
                sin = sinusas(x)
                logger.info(f"Sinusas: sin({x}) ={sin}")


            elif pasirinkimas == "9":
                x = float(input("Iveskite skaiciu \n"))
                print(x, "logoritmas", "=", logoritmas(x))
                log = logoritmas(x)
                logger.info(f"Logoritmas: log({x}) ={log}")

            elif pasirinkimas == "10":
                x = float(input("iveskite skaiciu \n"))
                print(x, "cossinusas", "=", cossinusas(x))
                cos = cossinusas(x)
                logger.info(f"Cossinusas: cos{x} ={cos}")

            elif pasirinkimas == "11":
                x = float(input("iveskite skaiciu \n"))
                print("10 ^",x, "=" , desimtlaipsniu(x))
                des = desimtlaipsniu(x)
                logger.info(f"Desimutoju: 10^{x} = {des}")
    if isjungimas == '2':
        break
    if isjungimas == '':
        break
