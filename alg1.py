import random
import time

def create_efootball_draw():
    epics = [
        "Epic: Ronaldinho Gaucho", 
        "Epic: Steven Gerrard", 
        "Epic: Francesco Totti", 
        "Epic: Angelo Peruzzi", 
        "Epic: Cafu"
    ]
    base_players = []
    for i in range(1, 146): 
        base_players.append(f"Standard Player {i}")
        
    full_draw = epics + base_players
    random.shuffle(full_draw)
    return full_draw

def run_simulation():
    print("Welcome to the eFootball draw simulator!")
    print("Setting up a fresh 150-player Epic draw...")

    draw = create_efootball_draw()
    coins_spent = 0
    epics_found = 0  
    
    print(f"Draw initialised. Total players: {len(draw)}\n")
    time.sleep(1)     
    while epics_found < 5 and len(draw) > 0:
        input("Press ENTER to spend 100 coins on a spin...")
        drawn_player = draw.pop()
        coins_spent += 100
        
        print("\n" + "="*30)
        print(f"You pulled: {drawn_player}")
        print(f"Total coins spent: {coins_spent}")
        print(f"Players remaining in the draw: {len(draw)}")
        
        if "Epic" in drawn_player:
            epics_found += 1 
            print(f"🎉 CONGRATULATIONS! You have found {epics_found}/3 target Epics! 🎉")
        print("="*30 + "\n")
        
    if epics_found == 3:
        print(f"Success! You cleared your targets in {coins_spent} coins.")
    else:
        print("The box is empty!")

if __name__ == "__main__":
    run_simulation() 