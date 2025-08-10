import csv
import random
import time
import sys
import os

fish_dict = {}
players = {}

with open('/home/daniel/dev/learning/python/python_project_1/CodeAcademy-Portfolio-Project-1/fish.csv') as fish_data_csv:
    fish_data = list(csv.DictReader(fish_data_csv))  # Convert to list first
    for idx, fish in enumerate(fish_data):
        fish_dict[idx] = fish  # Use numeric index as key

class Fish:
    def __init__(self):
        random_key = random.randint(0, len(fish_dict) - 1)  # Subtract 1 to avoid index error
        self.random_fish = fish_dict[random_key]  # Get fish using random key
        print("Random Fish Details:")
        for key, value in self.random_fish.items():
            print(f"{key}: {value}")

class Player:
    def __init__(self, name: str):
        self.name = name  # Fixed: Store name as instance attribute
        self.fish_caught = []
        players[len(players)] = self  # Fixed: Add player to dict with auto-incremented key

class StartGame:
    game_on = True



def get_key_press():
    """Cross-platform keypress detection without external modules"""
    if os.name == 'nt':  # Windows
        import msvcrt
        if msvcrt.kbhit():
            return msvcrt.getch()
    else:  # Linux/Mac
        import termios, fcntl
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
        try:
            return sys.stdin.read(1)
        except:
            return None
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
    return None

def animate_bar():
    max_width = 60
    try:
        while True:
            # Growing phase
            for i in range(1, max_width + 1):
                sys.stdout.write('\r' + '|' * i)
                sys.stdout.flush()
                time.sleep(0.03)
            
            # Shrinking phase
            for i in range(max_width, 0, -1):
                sys.stdout.write('\r' + '|' * i)
                sys.stdout.flush()
                time.sleep(0.03)
    except KeyboardInterrupt:
        sys.stdout.write('\r' + ' ' * max_width + '\r')

# Start immediately
print("Loading... (Press Ctrl+C to stop)")
animate_bar()