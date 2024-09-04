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

def spustit_hru():
    # Inicializace počtu správných odpovědí a počtu kol.
    spravne_odpovedi = 0
    # Náhodně určí počet kol (od 3 do 10).
    pocet_kol = random.randint(3, 10)

    # Smyčka pro zadaný počet kol.
    for kolo in range(pocet_kol):
        # Generujeme dvě náhodná čísla od 1 do 10.
        x = random.randint(1, 10)
        y = random.randint(1, 10)

        # Zeptáme se uživatele na výsledek násobení dvou čísel.
        porovnani = int(input(f"{x} * {y} = "))

        # Vyhodnotíme odpověď.
        if vyhodnoceni(nasobeni(x, y), porovnani):
            spravne_odpovedi += 1  # Pokud je odpověď správná, přičteme bod.

    # Po ukončení hry vypíšeme skóre.
    print("\n---------------------------")
    print(f"Hra skončila! Zde jsou vaše výsledky:")
    print(f"Počet kol: {pocet_kol}")
    print(f"Správně jste odpověděl {spravne_odpovedi} z {pocet_kol} otázek.")
    
    # Vypočítáme procentuální úspěšnost.
    procentualni_uspesnost = (spravne_odpovedi / pocet_kol) * 100
    print(f"Vaše úspěšnost je: {procentualni_uspesnost:.2f}%")
    print("---------------------------\n")

def privitani():
    # Uvítací zpráva pro uživatele.
    print("---------------------------")
    print("Vítejte v matematické hře!")
    print("Zde si procvičíte násobení náhodných čísel.")
    print("Na konci hry se dozvíte své skóre a úspěšnost.")
    print("---------------------------\n")

def main():
    # Přivítání uživatele na začátku programu.
    privitani()
    
    while True:
        spustit_hru()  # Spustíme hru.
        
        # Zeptáme se uživatele, zda chce hrát znovu.
        znovu = input("Chcete hrát znovu? (ano/ne): ").lower()
        
        # Pokud uživatel zadá "ne", ukončíme program.
        if znovu != "ano":
            print("Děkujeme za hraní! Nashledanou.")
            break

# Spuštění hlavního programu.
main()
