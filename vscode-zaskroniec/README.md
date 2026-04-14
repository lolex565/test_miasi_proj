# Rozszerzenie VSCode dla języka Zaskroniec

Zapewnia ładne wsparcie, kolorowanie składni i rozróżnienie podstawowych mechanizmów, zmiennych, klas i słów kluczowych dialektu Zaskroniec.
Zbudowane przy okazji tworzenia interpretera opartego na ANTLR4.

## Uruchamianie plików `.zas`

Wtyczka dodaje przycisk **Uruchom plik Zaskroniec** (`▶`) w pasku tytułu edytora dla plików `.zas`.
Po kliknięciu uruchamiane jest polecenie:

`python zaskroniec.py <aktywny_plik.zas>`

w terminalu VS Code (z katalogu otwartego workspace).

Możesz zmienić polecenie Pythona ustawieniem:

`zaskroniec.pythonCommand` (np. `python3` albo `py`).
