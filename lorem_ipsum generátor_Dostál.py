import random

vahy_pismen = {
    'a': 8.61, 'á': 1.46, 'b': 2.52, 'c': 4.15, 'č': 1.54,
    'd': 4.32, 'ď': 0.19, 'e': 7.41, 'é': 0.14, 'ě': 1.11,
    'f': 0.13, 'g': 1.20, 'h': 1.42, 'i': 6.94, 'í': 2.87,
    'j': 2.50, 'k': 3.08, 'l': 3.54, 'm': 2.54, 'n': 6.73,
    'ň': 0.31, 'o': 6.35, 'ó': 0.74, 'p': 2.62, 'q': 0.00,
    'r': 4.79, 'ř': 1.58, 's': 5.31, 'š': 1.01, 't': 5.20,
    'ť': 0.28, 'u': 2.99, 'ú': 0.59, 'ů': 0.16, 'v': 5.15,
    'w': 0.00, 'x': 0.02, 'y': 3.68, 'ý': 1.58, 'z': 4.97,
    'ž': 0.99,
}

def generuj_slovo():
    samohlasky = 'aeiouyáéíóúýěščřžďťň'
    souhlasky = 'bcdfghjklmnpqrstvwxz'
    
    pocet_slabik = random.randint(1, 3)
    
    slovo = ''.join([
        random.choices(list(souhlasky), weights=[vahy_pismen[s] for s in souhlasky])[0] +
        random.choices(list(samohlasky), weights=[vahy_pismen[v] for v in samohlasky])[0]
        for i in range(pocet_slabik)
    ])

    return slovo

def generuj_lorem_ipsum():
    pocet_odstavcu = None
    while pocet_odstavcu is None:
        try:
            pocet_odstavcu = int(input("Zadejte počet odstavců: "))
        except ValueError:
            print("Chyba: Zadávejte pouze celá čísla.")

    slov_na_odstavec = None
    while slov_na_odstavec is None:
        try:
            slov_na_odstavec = int(input("Zadejte počet slov na odstavec: "))
        except ValueError:
            print("Chyba: Zadávejte pouze celá čísla.")

    lorem_ipsum_text = []

    for i in range(pocet_odstavcu):
        odstavec = ' '.join([generuj_slovo() for i in range(slov_na_odstavec)])
        lorem_ipsum_text.append(odstavec)

    return '\n\n'.join(lorem_ipsum_text)

def uloz_do_souboru(text, nazev_souboru='lorem_ipsum.txt'):
    with open(nazev_souboru, 'w', encoding='utf-8') as soubor:
        soubor.write(text)

vygenerovany_text = generuj_lorem_ipsum()

print("\nVygenerovaný text:\n")
print(vygenerovany_text)

uloz_do_souboru(vygenerovany_text)
print(f"\nText byl uložen do souboru 'lorem_ipsum.txt'.")