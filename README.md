## Generátor Lorem Ipsum

Tento program generuje náhodný text ve stylu Lorem Ipsum v češtině a umožňuje uživateli uložit vygenerovaný text do souboru.

## Jak používat

1. Spusťte skript v Pythonu pomocí příkazu:
   ```bash
   python generuj_lorem_ipsum.py
Zadávejte počet odstavců a počet slov na odstavec, jak je požadováno.

Vygenerovaný text bude zobrazen na obrazovce a zároveň uložen do souboru lorem_ipsum.txt ve stejném adresáři.

Popis kódu
generuj_slovo(): Funkce generuje náhodné slovo s určeným počtem slabik.

generuj_lorem_ipsum(): Funkce generuje text Lorem Ipsum s požadovaným počtem odstavců a slov na odstavec.

uloz_do_souboru(text, nazev_souboru='lorem_ipsum.txt'): Funkce ukládá vygenerovaný text do souboru.

Příklad použití
python
Copy code
vygenerovany_text = generuj_lorem_ipsum()

print("\nVygenerovaný text:\n")
print(vygenerovany_text)

uloz_do_souboru(vygenerovany_text)
print(f"\nText byl uložen do souboru 'lorem_ipsum.txt'.")
