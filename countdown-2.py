from datetime import datetime, timedelta
import time
from colorama import Fore, init
import pyfiglet

# 1. Ustawienia
# Zmień wartość zmiennej FIGLET_FONT na "doom" lub "big"
# Czcionka "doom" jest bardzo szeroka i blokowa
# Czcionka "big" jest duża i klasyczna
FIGLET_FONT = 'doom'  # <<< Zmień na 'big', aby przetestować inną opcję

# Initialize colorama
init(autoreset=True)

# Set New Year's target
new_year = datetime(datetime.now().year + 1, 1, 1)

while datetime.now() < new_year:
    # Calculate remaining time
    remaining = new_year - datetime.now()

    # Format remaining time as a string (remove microseconds)
    # Format: D days, H:MM:SS
    remaining_str = str(remaining).split(".")[0] 

    # 2. Generowanie formatu figlet z użyciem wybranej czcionki
    formatted_time = pyfiglet.figlet_format(remaining_str, font=FIGLET_FONT)

    # Clear the screen (works on most terminals, might not work in all Android environments)
    # Używamy \033[2J, które lepiej działa w Termux niż \033c
    print("\033[2J", end="") 

    # Display remaining time in figlet font
    print(Fore.GREEN + formatted_time)

    # Delay for 1 second
    time.sleep(1)

# Clear the screen one last time
print("\033[2J", end="")

# Print Happy New Year message
# Używamy tej samej czcionki
new_year_msg = pyfiglet.figlet_format("Happy New Year!", font=FIGLET_FONT)
print(Fore.YELLOW + new_year_msg)