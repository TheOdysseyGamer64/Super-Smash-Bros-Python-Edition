###########################################################################################################################################################################################################################
# THIS GAME IS NOW OBSOLETE. THE INABILITY TO ADD FINAL SMASH MECHANICS IN THIS VERSION OF THE CODE MAKES IT UNVIABLE TO BE AN ACCCURATE REPRESENTATION OF SUPER SMASH BROS ULTIMATE'S UNIQUE AND NEW MECHANICS FOR MOVES # 
# PLEASE NOW SEE reworked_smash.py TO SEE THE FINAL SMASH MECHANICS IN ACTION WHILE WORKING PROPERLY ALONG WITH SAFE AND TRUE INTEGRATION OF THE SPECIAL ABILITY MOVES OF PUNCHOUT'S LITTLE MAC AND FINAL FANTASY'S CLOUD #
############################################################################################################################################################################################################################



"""
Super Smash Bros Ultimate - Python Edition
A text-based fighting game where players choose characters and execute moves.
Uses selection, iteration, and sequences as programming constructs.
"""

import random
import time
MOVESETS = {
    "Cloud": {
        "neutral": "Slash (5 damage)",
        "side": "Limit Break Cross Slash (15 damage)",
        "up": "Climhazzard (8 damage)",
        "down": "Limit Break Final Heaven (20 damage)",
        "final": "Omnislash Version Five (45 damage)"
    },
    "Mii Swordfighter": {
        "neutral": "Jab Combo (4 damage)",
        "side": "Blade Counter (12 damage)",
        "up": "Rising Slash (7 damage)",
        "down": "Neutral Special (10 damage)",
        "final": "Final Edge (38 damage)"
    },
    "Mario": {
        "neutral": "Fireball (6 damage)",
        "side": "Cape Spin (8 damage)",
        "up": "Super Jump Punch (9 damage)",
        "down": "F.L.U.D.D (11 damage)",
        "final": "Mario Finale (40 damage)"
    },
    "Sora": {
        "neutral": "Keyblade Slash (5 damage)",
        "side": "Sonic Blade (13 damage)",
        "up": "Spiral Slice (8 damage)",
        "down": "Sealing Spell (16 damage)",
        "final": "Seeing the Keyhole (37 damage)"
    },
    "Luigi": {
        "neutral": "Fireball (5 damage)",
        "side": "Green Missile (14 damage)",
        "up": "Super Jump Punch (10 dammage)",
        "down": "Luigi Cyclone (12 damage)",
        "final": "Poltergust 3000 (38 damage)"
    },

    "Little Mac": {
        "neutral": "Straight Lunge (10 damage)",
        "side": "Jolt Haymaker (13 damage)",
        "up": "Rising Uppercut (12 damage)",
        "down": "Slip Counter (16 damage)",
        "final": "Big Mac (52 damage)"
    }
    
}


CHARACTERS = {
    "Cloud": {"name": "Cloud", "hp": 100, "attack_speed": 0.8, "description": "A mercenary with powerful limit break abilities"},
    "Mii Swordfighter": {"name": "Mii Swordfighter", "hp": 85, "attack_speed": 1.0, "description": "A customizable fighter with balanced stats"},
    "Mario": {"name": "Mario", "hp": 90, "attack_speed": 0.9, "description": "The classic hero with fire-based attacks"},
    "Sora": {"name": "Sora", "hp": 95, "attack_speed": 0.95, "description": "A keyblade master with magical abilities"},
    "Luigi": {"name": "Luigi", "hp": 90, "attack_speed": 0.9, "description": "The cowardly brother of Mario, yet brave to fight even monsters"},
    "Little Mac": {"name": "Little Mac", "hp": 90, "attack_speed": 0.85, "description": "One of Smash's most hated characters; buff, yet weak, and a boxer that really cooks you"}
    
}

MOVE_OPTIONS = {
    "1": "neutral",
    "2": "side",
    "3": "up",
    "4": "down",
    "5": "final"
}


def display_title():
    """Display the game title and instructions."""
    print("\n" + "="*60)
    print("     SUPER SMASH BROS ULTIMATE - PYTHON EDITION")
    print("="*60)
    print("Welcome to the ultimate fighting experience!")
    print("Choose your fighter and battle for victory!\n")


def display_characters():
    """Display all available characters using iteration."""
    print("--- SELECT YOUR CHARACTER ---")
    print("Available Fighters:\n")
    
   
    for index, (character_name, stats) in enumerate(CHARACTERS.items(), 1):
        print(f"{index}. {character_name}")
        print(f"   HP: {stats['hp']} | Attack Speed: {stats['attack_speed']}")
        print(f"   {stats['description']}\n")


def select_character():
    """Selection construct: Player chooses their character."""
    valid_choices = ["1", "2", "3", "4", "5", "6"]
    character_list = list(CHARACTERS.keys())
    
    while True: 
        display_characters()
        choice = input("Enter the number of your fighter (1-6): ").strip()
        
        if choice in valid_choices:
            selected_character = character_list[int(choice) - 1]
            print(f"You selected {selected_character}!")
            return selected_character
        else:
            print("Invalid choice! Please enter 1-6.")


def display_moves(character):
    print(f"--- {character.upper()}'S MOVESET ---")
    print("Choose your move:")
    print("1. Neutral Special (Fast, Low Damage)")
    print("2. Side Special (Medium Speed, Medium Damage)")
    print("3. Up Special (Medium Speed, Medium Damage)")
    print("4. Down Special (Slow, High Damage)")

    if final_ready:
        print("5. FINAL SMASH")


def select_move(character):
    """Selection construct: Player selects a move."""
    valid_moves = ["1", "2", "3", "4"]

    if final_ready:
        valid_moves.append("5")
    
    while True: 
        display_moves(character, final_ready)
        choice = input("Choose your move: ").strip()
        
        if choice in valid_moves:

            if choice == "5":
                move_info = MOVESETS[character]["final"]
                damage = int(move_info.split("(")[1].split()[0])
                return "final", move_info, damage
                
            direction = MOVE_OPTIONS[choice]
            move_info = MOVESETS[character][direction]
            damage = int(move_info.split("(")[1].split()[0])
            

            damage = int(move_info.split("(")[1].split()[0])
            
            return direction, move_info, damage
        
        print("Invalid move!")


def battle_round(player_character, player_hp, enemy_character, enemy_hp, round_num):
    """Execute one round of battle with sequence and selection constructs."""
    print("=" * 60)
    print(f"ROUND {round_num}")
    print("=" * 60)
    print(f"Your HP: {player_hp} | Enemy HP: {enemy_hp}")
    
   
    print(f"Your turn! Playing as {player_character}!")
    _, player_move, player_damage = select_move(player_character)
    player_used_counter = (
        player_character == "Little Mac"
        and "Slip Counter" in player_move
    )
    
    print(f"You used: {player_move}")
    
   
    enemy_move_direction = random.choice(list(MOVESETS[enemy_character].keys()))
    enemy_move_info = MOVESETS[enemy_character][enemy_move_direction]
    enemy_damage = int(enemy_move_info.split("(")[1].split()[0])
    
    print(f"Enemy used: {enemy_move_info}")
    

    time.sleep(0.5)
    player_hits = random.random() < 0.8
    enemy_hits = random.random() < 0.8
    
    if player_used_counter:
        print("Little Mac is waiting to counter...")
    else:
        
        if player_hits:
            enemy_hp -= player_damage
            print(f"Hit! Dealt {player_damage} damage!")
        else:
            print("Missed!")
    
    time.sleep(0.3)
    
    if enemy_hits:
        player_hp -= enemy_damage
        print(f"Enemy hit! Took {enemy_damage} damage!")

        if player_used_counter:
            print("Slip Counter failed!")
    else:
        print("Enemy missed!")

        if player_used_counter:
            counter_damage = 20
            enemy_hp -= counter_damage
            print(f"Slip Counter activated! Little Mac dealt {counter_damage} damage!")
    
 
    player_hp = max(0, player_hp)
    enemy_hp = max(0, enemy_hp)
    
    return player_hp, enemy_hp


def get_enemy_character(player_choice):
    """Selection construct: Pick an opponent different from player choice."""
    available_opponents = [char for char in CHARACTERS.keys() if char != player_choice]
    opponent = random.choice(available_opponents)
    print(f"You face {opponent}!")
    return opponent


def play_battle(player_character):
    """Main battle loop using iteration and selection."""
    

    
    enemy_character = get_enemy_character(player_character)
    player_hp = CHARACTERS[player_character]["hp"]
    enemy_hp = CHARACTERS[enemy_character]["hp"]

    player_final_meter = 0
    enemy_final_meter = 0
    
    player_used_final = False
    enemy_used_final = False
    
    round_num = 1
    max_rounds = 15
    
 
    while player_hp > 0 and enemy_hp > 0 and round_num <= max_rounds:
        player_hp, enemy_hp = battle_round(player_character, player_hp, 
                                           enemy_character, enemy_hp, round_num)

        player_final_meter += 25
        enemy_final_meter += 25

        player_final_meter = min(player_final_meter, 100)
        enemy_final_meter = min(enemy_final_meter, 100)

        print(f"\nFinal Smash Meter: {player_final_meter}%")
        
        round_num += 1
        
        if player_hp > 0 and enemy_hp > 0:
            input("\nPress ENTER to continue to next round...")
    
   
    print("=" * 60)
    print("BATTLE OVER!")
    print("=" * 60)
    
    if player_hp > 0 and enemy_hp <= 0:
        print(f"VICTORY! {player_character} wins!")
        print(f"Remaining HP: {player_hp}")
        return True
    elif enemy_hp > 0 and player_hp <= 0:
        print(f"DEFEAT! {enemy_character} wins!")
        print(f"Enemy Remaining HP: {enemy_hp}")
        return False
    else:
        print("DRAW! Both fighters fall!")
        return None


def play_again():
    """Selection construct: Ask if player wants to play again."""
    while True:  
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main game loop using iteration and selection."""
    display_title()
    
    
    while True:  
        player_character = select_character()
        
        print(f"Character Selected: {player_character}")
        print(f"Description: {CHARACTERS[player_character]['description']}")
        print(f"Starting HP: {CHARACTERS[player_character]['hp']}")
        
        input("Press ENTER to begin battle...")
        
        
        victory = play_battle(player_character)
        
        
        if victory is True:
            print("Congratulations! You've achieved victory!")
        elif victory is False:
            print("Train harder and try again!")
        else:
            print("A worthy opponent!")
        
        
        if not play_again():
            print("\n" + "="*60)
            print("Thanks for playing Super Smash Bros Ultimate - Python Edition!")
            print("="*60 + "\n")
            break


if __name__ == "__main__":
    main()
