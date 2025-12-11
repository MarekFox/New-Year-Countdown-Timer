from datetime import datetime, timedelta
import time
from colorama import Fore, init
import pyfiglet
import os # NOWY IMPORT

# 1. Ustawienia
# Czcionka "doom" jest bardzo szeroka i blokowa
# Czcionka "big" jest duża i klasyczna
# jeszcze jest "banner"
FIGLET_FONT = 'doom' 
TARGET_COLUMNS = 35 # <<<<< KLUCZOWA ZMIENNA: Wymuś mniejszą liczbę kolumn (np. 55 zamiast 108)

# Inicjalizacja
init(autoreset=True)

# Ustawienie celu
new_year = datetime(datetime.now().year + 1, 1, 1)

# Ustawienie szerokości kolumn (zanim rozpocznie się pętla)
# Ta komenda wymusi na Termux renderowanie znaków szerzej, by zmieściły się w 55 kolumnach
os.system(f"stty cols {TARGET_COLUMNS}") 


while datetime.now() < new_year:
    # ... (reszta obliczeń czasu bez zmian)
    remaining = new_year - datetime.now()
    remaining_str = str(remaining).split(".")[0] 
    
    # 2. Generowanie figlet z czcionką 'doom'
    formatted_time = pyfiglet.figlet_format(remaining_str, font=FIGLET_FONT)

    # Czyszczenie ekranu (lepiej działa \033[2J w Termux)
    print("\033[2J", end="") 

    # Wyświetlanie
    print(Fore.GREEN + formatted_time)

    time.sleep(1)

# Czyszczenie ekranu po zakończeniu
print("\033[2J", end="")

# Wypisanie wiadomości końcowej
new_year_msg = pyfiglet.figlet_format("Happy New Year!", font=FIGLET_FONT)
print(Fore.YELLOW + new_year_msg)

# *** ODCZYTANIE ZMIAN: Przywrócenie oryginalnej szerokości terminala ***
os.system("stty cols 108") # Przywrócenie kolumn do domyślnej wartości (108)