def sudetis(a, b):
    return a + b
def atimtis(a, b):
    return a - b 
def daugyba(a, b):
    return a * b
def dalyba(a , b):
    return a / b 
print("pasirinkite veiksma")
print("1. sudetis")
print("2. dalyba")
print("3. daugyba")
print("4. dalyba")
while True:
    pasirinkimas = input("parasykite veiksma (1/2/3/4) ")
    if pasirinkimas in ('1', '2', '3', '4'):
        x = float(input("pasirinkite pirma skaiciu: "))
        y = float(input("pasirinkite antra skaiciu : "))
    if pasirinkimas == "1":
        print(x, '+' , y ,  sudetis(x, y))
    elif pasirinkimas == "2":
        print (x , "-" , y, atimtis(x, y))
    elif pasirinkimas == "3":
        print(x , "*" , y, daugyba(x, y))
    elif pasirinkimas == "4":
        print(x , "/" , y, dalyba(x, y))