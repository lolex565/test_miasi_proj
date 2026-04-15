# Rozszerzenie VSCode dla języka Zaskroniec

Zapewnia kolorowanie składni dla języka zaskroniec

## Uruchamianie plików `.zas`

Dodano przycisk **Uruchom plik Zaskroniec** (`▶`) w pasku edytora dla plików `.zas`.
Po kliknięciu uruchamiane jest polecenie:

`python zaskroniec.py <aktywny_plik.zas>`

w terminalu VS Code (z katalogu otwartego workspace).

Możesz zmienić polecenie Pythona ustawieniem:

`zaskroniec.pythonCommand` (np. `python3` albo `py`).


W aktualnej wersji do działania uruchamiania przyciskiem potrzeba umieścić w katalogu roboczym plik zaskroniec.py oraz jego dependencje