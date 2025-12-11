# ⏳ New Year Countdown Timer (Python / Pyfiglet)

Projekt w języku Python, który wyświetla odliczanie do Nowego Roku. Odliczanie jest renderowane jako duży tekst ASCII Art za pomocą biblioteki `pyfiglet`.

Szczególny nacisk położono na optymalizację wyświetlania na ekranach urządzeń mobilnych (Android / Termux).

## 🚀 Uruchomienie na Urządzeniach Mobilnych (Android / Termux)

Aby uruchomić ten skrypt na smartfonie, zalecana jest instalacja emulatora terminala **Termux**, który pozwala na uruchamianie kodu Pythona w środowisku zbliżonym do Linuksa.

### Krok 1: Instalacja Termux i Narzędzi

1.  **Zainstaluj Termux:** Pobierz i zainstaluj aplikację Termux na swoim urządzeniu Android (np. Samsung lub Xiaomi).

2.  **Zainstaluj Pythona i Gita:** Po otwarciu Termux, zainstaluj niezbędne pakiety za pomocą komendy `pkg`:
    ```bash
    pkg update && pkg upgrade
    pkg install python
    pkg install git
    ```

### Krok 2: Klonowanie Repozytorium

Pobierz kod projektu z serwisu GitHub na swoje urządzenie mobilne:

1.  **Klonowanie:**
    ```bash
    git clone https://github.com/MarekFox/New-Year-Countdown-Timer.git
    ```
    *(Pamiętaj, aby zastąpić adresem URL swojego repozytorium!)*

2.  **Przejdź do katalogu projektu:**
    ```bash
    cd New-Year-Countdown-Timer
    ```

### Krok 3: Konfiguracja i Instalacja Zależności

1.  **Instalacja bibliotek:** Zainstaluj zależności (`pyfiglet`, `colorama`) używając pliku `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

### Krok 4: Optymalizacja Wyświetlania i Uruchomienie

Projekt wykorzystuje specjalny skrypt `countdown-2.py`, który dostosowuje szerokość terminala, aby zmaksymalizować rozmiar czcionki **'doom'**.

#### 4.1. Ustawienie Optymalnego Rozmiaru (Kluczowe!)

W pliku `countdown-2.py` optymalna wartość dla większości smartfonów to `TARGET_COLUMNS = 35` (dla telefonu z 108 kolumnami). Możesz ją zmodyfikować, jeśli tekst będzie się łamać:

1.  **Otwórz plik** w Termuxie (np. za pomocą edytora `nano`):
    ```bash
    nano countdown-2.py
    ```
2.  **Zmień wartość** zmiennej `TARGET_COLUMNS` (np. na 40, jeśli 35 jest zbyt duże, lub na 30, jeśli nadal jest za małe).
3.  **Zapisz i wyjdź** (Ctrl+O, Enter, Ctrl+X).

#### 4.2. Uruchomienie Programu

Upewnij się, że telefon jest w **orientacji poziomej** (krajobrazowej), a następnie uruchom:

```bash
python countdown-2.py