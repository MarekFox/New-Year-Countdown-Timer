from datetime import datetime, timedelta
import time
from colorama import Fore, init
import pyfiglet
import os 

# 1. Ustawienia
# Czcionka "doom" jest bardzo szeroka i blokowa
# Czcionka "big" jest duża i klasyczna
# jeszcze jest "banner"

FIGLET_FONT = 'big' 
TARGET_COLUMNS = 35 # <<< OPTYMALNA WARTOŚĆ WYMUSZAJĄCA MAKSYMALNY ROZMIAR
ORIGINAL_COLUMNS = 108 # Twoja domyślna szerokość Termux

# Inicjalizacja
init(autoreset=True)

# Ustawienie celu
new_year = datetime(datetime.now().year + 1, 1, 1)
# new_year = datetime(2025, 12, 12)

# Ustawienie szerokości kolumn
os.system(f"stty cols {TARGET_COLUMNS}") 

try:
    while datetime.now() < new_year:
        # Calculate remaining time
        remaining = new_year - datetime.now()
        remaining_str = str(remaining).split(".")[0] 
        
        # Generowanie figlet
        formatted_time = pyfiglet.figlet_format(remaining_str, font=FIGLET_FONT)

        # Czyszczenie ekranu
        print("\033[2J", end="") 

        # Wyświetlanie
        print(Fore.GREEN + formatted_time)

        time.sleep(1)
        
finally:
    # Ten blok GWARANTUJE, że komenda zostanie wykonana nawet po przerwaniu skryptu (np. Ctrl+C)
    
    # 2. Przywrócenie oryginalnej szerokości terminala
    os.system(f"stty cols {ORIGINAL_COLUMNS}") 
    
    # Czyszczenie ekranu po zakończeniu
    print("\033[2J", end="")

    # Wypisanie wiadomości końcowej (może być uruchomiona, jeśli pętla dobiegła końca)
    if datetime.now() >= new_year:
        new_year_msg = pyfiglet.figlet_format("Happy New Year!", font=FIGLET_FONT)
        print(Fore.YELLOW + new_year_msg)