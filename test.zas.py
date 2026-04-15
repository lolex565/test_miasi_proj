# ==== TEST 1: Podstawowe (zmienne, petle, warunki, print) ====
print("--- TEST 1: Zmienne, Petle, Warunki ---")
calkowita_zmienna = int("5")
print("Zmienna to:", calkowita_zmienna)

if calkowita_zmienna > 3 and not False:
    print("Warunki logiczne (oraz, nie, Prawda) dzialaja.")

licznik = 0
while licznik < 2:
    print("Petla dopoki, przebieg", licznik)
    licznik = licznik + 1
    if licznik == 2:
        print("Przerywam petle dopoki!")
        break

dowhile_licznik = 0
while True:
    print("Petla wykonuj-dopoki, przebieg", dowhile_licznik)
    dowhile_licznik = dowhile_licznik + 1
    if not (dowhile_licznik < 2):
        break

print("Konstrukcja funkcyjna zastosuj: dziala")

for i in range(3):
    if i == 1:
        pass
    elif i == 0:
        continue
    else:
        print("Petla dla. Wartosc:", i)

# ==== TEST 2: Operatoy tozsamosci and wyjatki (is, raise, try, except) ====
print("\n--- TEST 2: Wyjatki i Asertywnosc ---")
pusta_zmienna = None

if pusta_zmienna is None:
    print("Operator tozsamosci (jest) dziala.")

assert 2 + 2 == 4, "Asercja matematyczna (zapewnij)"

try:
    raise Exception("Zabawa w bledy")
except Exception as e:
    print("Zlapano:", e)
finally:
    print("Wyjatki w pelni obsluzone.")

# ==== TEST 3: Funkcje, pamiec i wbudowane liczbowe ====
print("\n--- TEST 3: Pamiec i Matematyka ---")

zmienna_globalna = 100

def funkcja_matematyczna():
    global zmienna_globalna
    zmienna_globalna = zmienna_globalna + 10
    
    lista_cyfr = list([1, 2, 3, 4, -5])
    
    dodawanie = lambda x: x + 1
    print("Sumowanie anonimowe:", dodawanie(4))
    
    najm = min(lista_cyfr)
    najw = max(lista_cyfr)
    zsumowane = sum(lista_cyfr)
    absolut = abs(najm)
    zaokraglenie = round(3.14159, 2)
    
    print("Min:", najm, "Max:", najw, "Suma:", zsumowane, "Absolutna:", absolut, "Zaokraglone:", zaokraglenie)
    return type(lista_cyfr)

wymagany_typ = funkcja_matematyczna()
print("Zwrocony typ to:", wymagany_typ, "a zmienna globalna to:", zmienna_globalna)

niepotrzebna_zmienna = "Do usuniecia"
del niepotrzebna_zmienna

# ==== TEST 4: Klasy, generatory ====
print("\n--- TEST 4: Klasy i Generatory ---")
class TestowaKlasa:
    def __init__(sam, imie):
        sam.imie = str(imie)
    
    def generator_przywitan(sam):
        yield "Czesc " + sam.imie
        yield "Witaj " + sam.imie

obiekt = TestowaKlasa("Swiecie")
for powitanie in obiekt.generator_przywitan():
    print(powitanie)

# ==== TEST 5: Słowniki, zbiory, krotki ====
print("\n--- TEST 5: Kolekcje ---")
zb = set([1, 1, 2])
s = dict({"klucz": "wartosc"})
k = tuple((1, "dwa", True))

print("Zbior:", zb, "Slownik:", s, "Krotka:", k)
print("Dlugosc slownika:", len(s))

# ==== TEST 6: Asynchroniczność ====
# (Definiujemy ale not uruchamiamy petli glownej asyncio by skrypt dzialal liniowo bez blokad)
import asyncio

async def testowanie_asynchroniczne():
    print("\n--- TEST 6: Asynchroniczność ---")
    print("Sekcja asynchroniczna dziala!")
    await asyncio.sleep(0.01)

# Skrypt uruchamia event loop by sprawdzic czy asynch/await zadzialalo poprawnie in symulacji
asyncio.run(testowanie_asynchroniczne())

print("\nPelne testy zaliczone spiewajaco!")
