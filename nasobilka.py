import random #Importujeme knihovnu s funkcema pro náhodné generování čísel

def nasobeni(a, b):
    vysledek = a * b
    return vysledek

def vyhodnoceni(vysledek, porovnani):
    odpoved = False
    if vysledek == porovnani:
        print("Ty jsi ale šikulka, máš správně")
        odpoved = True
    else:
        print("Ahh, zrovna jsi se spletl, příště to bude lepší")
    return odpoved

x = random.randint(1,10)
y = random.randint(1,10)


porovnani = input(f"{x} * {y} = ")
