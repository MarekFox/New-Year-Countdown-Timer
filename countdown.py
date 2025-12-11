from datetime import datetime, timedelta
import time
from colorama import Fore, init
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Set New Year's target
new_year = datetime(datetime.now().year + 1, 1, 1)

while datetime.now() < new_year:
    # Calculate remaining time
    remaining = new_year - datetime.now()

    # Format remaining time as a string
    remaining_str = str(remaining).split(".")[0]  # Remove microseconds for clarity
    formatted_time = pyfiglet.figlet_format(remaining_str)

    # Clear the screen (works on most terminals)
    print("\033c", end="")

    # Display remaining time in figlet font
    print(Fore.GREEN + formatted_time)

    # Delay for 1 second
    time.sleep(1)

# Clear the screen one last time
print("\033c", end="")

# Print Happy New Year message
new_year_msg = pyfiglet.figlet_format("Happy New Year!")
print(Fore.YELLOW + new_year_msg)