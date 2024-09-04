import random  # Importujeme knihovnu s funkcemi pro náhodné generování čísel.

def nasobeni(a, b):
    # Funkce, která násobí dvě čísla a vrací výsledek.
    vysledek = a * b
    return vysledek  # Vrací výsledek násobení.

def vyhodnoceni(vysledek, porovnani):
    # Funkce, která vyhodnocuje, zda se zadaný výsledek shoduje s výsledkem násobení.
    odpoved = False  # Přednastavíme odpověď jako False (nesprávně).
    if vysledek == porovnani:  # Pokud výsledek odpovídá zadané hodnotě:
        print("Ty jsi ale šikulka, máš správně")  # Uživatel dostane pochvalu.
        odpoved = True  # Odpověď je True (správně).
    else:
        print("Ahh, zrovna jsi se spletl, příště to bude lepší")  # Pokud je špatně, vytiskne se povzbuzení.
    return odpoved  # Vrací, zda byla odpověď správná (True) nebo ne (False).

x = random.randint(1, 10)  
# Vygeneruje náhodné číslo od 1 do 10 a přiřadí ho k proměnné x.

y = random.randint(1, 10)  
# Vygeneruje náhodné číslo od 1 do 10 a přiřadí ho k proměnné y.

porovnani = input(f"{x} * {y} = ")  
# Zeptá se uživatele na výsledek násobení dvou čísel x a y a uloží ho do proměnné porovnani.
