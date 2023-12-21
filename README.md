# Lorem_Ipsum_Generator
# Generátor Lorem Ipsum v Pythonu

Tento skript vytváří náhodně generovaný text ve stylu Lorem Ipsum v češtině. Text je generován na základě váhy jednotlivých písmen, které jsou určeny na základě četnosti v českém jazyce.

## Použití

1. Spusťte skript v Pythonu (verze 3.x):
    ```
    python lorem_ipsum_generator.py
    ```

2. Zadejte počet odstavců a počet slov na odstavec, když je to požadováno.

3. Vygenerovaný text bude zobrazen na obrazovce a uložen do souboru 'lorem_ipsum.txt'.

## Konfigurace

Váhy jednotlivých písmen jsou definovány v proměnné `vahy_pismen` ve skriptu. Můžete upravit tyto váhy podle potřeby.

```python
vahy_pismen = {
    'a': 8.61, 'á': 1.46, 'b': 2.52, ...
    # Další písmena a jejich váhy
}
Příklad použití ve vašem kódu
python
Copy code
from lorem_ipsum_generator import generuj_lorem_ipsum, uloz_do_souboru

vygenerovany_text = generuj_lorem_ipsum()

print("\nVygenerovaný text:\n")
print(vygenerovany_text)

uloz_do_souboru(vygenerovany_text)
print(f"\nText byl uložen do souboru 'lorem_ipsum.txt'.")
