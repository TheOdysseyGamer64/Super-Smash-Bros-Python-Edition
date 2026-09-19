import random
import time

CHARACTERS = {
    "Cloud": {
        "hp": 100,
        "speed": 0.90,
        "moves": {
            "neutral": ("Slash", 5),
            "side": ("Cross Slash", 15),
            "up": ("Climhazzard", 10),
            "down": ("Limit Break", 18),
            "final": ("Omnislash Ver. 5", 55)
        },
        "description": "A mercenary who grows stronger through his Limit Gauge."
    },

    "Mario": {
        "hp": 95,
        "speed": 0.95,
        "moves": {
            "neutral": ("Fireball", 8),
            "side": ("Cape", 15),
            "up": ("Super Jump Punch", 14),
            "down": ("F.L.U.D.D.", 10),
            "final": ("Mario Finale", 65)
        },
        "description": "Nintendo's famous plumber."
    },

    "Luigi": {
        "hp": 92,
        "speed": 0.95,
        "moves": {
            "neutral": ("Fireball", 5),
            "side": ("Green Missile", 14),
            "up": ("Super Jump Punch", 10),
            "down": ("Luigi Cyclone", 11),
            "final": ("Poltergust G-00", 48)
        },
        "description": "A timid fighter with surprising power."
    },

    "Sora": {
        "hp": 97,
        "speed": 0.93,
        "moves": {
            "neutral": ("Keyblade Slash", 6),
            "side": ("Sonic Blade", 14),
            "up": ("Aerial Sweep", 9),
            "down": ("Magic Burst", 16),
            "final": ("Sealing the Keyhole", 41)
        },
        "description": "The Keyblade wielder."
    },

    "Mii Swordfighter": {
        "hp": 90,
        "speed": 1.0,
        "moves": {
            "neutral": ("Jab Combo", 5),
            "side": ("Gale Strike", 11),
            "up": ("Skyward Slash Dash", 10),
            "down": ("Blade Counter", 13),
            "final": ("Final Edge", 32)
        },
        "description": "A balanced sword fighter."
    },

    "Little Mac": {
        "hp": 90,
        "speed": 1.10,
        "moves": {
            "neutral": ("Straight Lunge", 18),
            "side": ("Jolt Haymaker", 8),
            "up": ("Rising Uppercut", 10),
            "down": ("Slip Counter", 0),
            "final": ("Giga Mac", 70)
        },
        "description": "A fearless boxer with devastating punches."
    },

    "Duck Hunt Duo": {
        "hp": 90,
        "speed": 1.5,
        "moves": {
            "neutral": ("Can", 13),
            "side": ("8-bit Frisbee", 20),
            "up": ("the duck", 0),
            "down": ("Gunman", 16),
            "final": ("Firing Squad", 52)
        },
        "description": "A silly duo of a dog and a duck."
    },

    "Ness": {
        "hp": 75,
        "speed": 1.5,
        "moves": {
            "neutral": ("PK Spark", 30),
            "side": ("PK Fire", 25),
            "up": ("PK Thunder", 5),
            "down": ("Magnet", 0),
            "final": ("PK Starstorm", 47)
        },
        "description": "A village boy who possesses ESPER powers."
    }
}

MOVE_KEYS = {
    "1": "neutral",
    "2": "side",
    "3": "up",
    "4": "down",
    "5": "final"
}

FIGHTER_ART = {
    "Cloud": ["  /\\_", " (o.o)", " /|_|\\", "  / \\"],
    "Mario": ["  ___", " (o o)", " /|M|\\", "  / \\"],
    "Luigi": ["  ___", " (o o)", " /|L|\\", "  / \\"],
    "Sora": ["  /\\", " (o_o)", " /|K|\\", "  / \\"],
    "Mii Swordfighter": ["  /\\", " (^-^)", " /|S|\\", "  / \\"],
    "Little Mac": ["  ___", " (O O)", " /|M|\\", "  / \\"],
    "Duck Hunt Duo": ["  ___", " (O O)", " /|D|\\", " / \\"]
}


def title():

    print(r"""
  _____ _   _ ____  _____ ____    ____  __  __    _    ____  _
 / ____| | | |  _ \| ____|  _ \  / ___||  \/  |  / \  / ___|| |__
 \___ \| | | | |_) |  _| | |_) | \___ \| |\/| | / _ \ \___ \| '_ \
  ___) | |_| |  __/| |___|  _ <   ___) | |  | |/ ___ \ ___) | | | |
 |____/ \___/|_|   |_____|_| \_\ |____/|_|  |_/_/   \_\____/|_| |_|
""")

    print("                         Python Edition")
    print()


def health_bar(fighter):

    maximum = CHARACTERS[fighter["name"]]["hp"]
    filled = round(20 * fighter["hp"] / maximum)

    return "[" + "#" * filled + "." * (20 - filled) + "]"


def fighter_sprite(name):

    return FIGHTER_ART.get(
        name,
        ["  /\\", " (o.o)", " /|_|\\", "  / \\"]
    )


def show_arena(player, enemy):

    player_art = fighter_sprite(player["name"])
    enemy_art = fighter_sprite(enemy["name"])

    print("+----------------------------------------------------------+")
    print(
        f"| {player['name']:<22} VS "
        f"{enemy['name']:<22}         |"
    )
    print("|                                                          |")

    for player_line, enemy_line in zip(
        player_art,
        enemy_art
    ):

        print(
            f"| {player_line:<25}      "
            f"{enemy_line:>15}           |"
        )

    print(
        "|___________________________      _________________________|"
    )

    print(
        " |__________________________/\\____/\\______________________|"
    )


def display_characters():

    print("Choose your fighter\n")

    number = 1

    for fighter in CHARACTERS:

        stats = CHARACTERS[fighter]

        print(f"{number}. {fighter}")
        print(f"   HP: {stats['hp']}")
        print(f"   Speed: {stats['speed']}")
        print(f"   {stats['description']}")
        print()

        number += 1


def choose_character():

    fighters = list(CHARACTERS.keys())

    while True:

        display_characters()

        choice = input(
            f"Select Fighter (1-{len(fighters)}): "
        )

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(fighters):

                fighter = fighters[choice - 1]

                print()
                print(f"You selected {fighter}!")
                print()

                return fighter

        print("Invalid choice.\n")


def create_fighter(name):

    return {
        "name": name,
        "hp": CHARACTERS[name]["hp"],
        "final_meter": 0,
        "limit": 0,
        "ko_meter": 0,
        "used_final": False
    }


def show_status(player, enemy):

    print("=" * 60)

    show_arena(player, enemy)

    print()

    print(
        f"{player['name']} HP: "
        f"{player['hp']} "
        f"{health_bar(player)}"
    )

    print(
        f"{enemy['name']} HP: "
        f"{enemy['hp']} "
        f"{health_bar(enemy)}"
    )

    print()

    print(
        f"Final Smash Meter: "
        f"{player['final_meter']}%"
    )

    if (
        player["final_meter"] >= 100
        and not player["used_final"]
    ):

        print("FINAL SMASH READY!")

    if player["name"] == "Cloud":

        print(
            f"Limit Gauge: "
            f"{player['limit']}%"
        )

    if player["name"] == "Little Mac":

        print(
            f"KO Meter: "
            f"{player['ko_meter']}%"
        )

        if player["ko_meter"] >= 100:

            print("KO PUNCH READY!")

    print("=" * 60)


def choose_move(player):

    fighter = player["name"]
    moves = CHARACTERS[fighter]["moves"]

    print()
    print("Choose a move")

    if (
        player["name"] == "Little Mac"
        and player["ko_meter"] >= 100
    ):

        print("1. KO Punch")

    else:

        print(
            f"1. {moves['neutral'][0]}"
        )

    print(
        f"2. {moves['side'][0]}"
    )

    print(
        f"3. {moves['up'][0]}"
    )

    print(
        f"4. {moves['down'][0]}"
    )

    if (
        player["final_meter"] >= 100
        and not player["used_final"]
    ):

        print(
            f"5. {moves['final'][0]}"
        )

    while True:

        choice = input("> ")

        if choice in ["1", "2", "3", "4"]:

            return MOVE_KEYS[choice]

        if (
            choice == "5"
            and player["final_meter"] >= 100
            and not player["used_final"]
        ):

            return "final"

        print("Invalid move.")


def calculate_damage(player, move):

    fighter = player["name"]

    move_name, damage = (
        CHARACTERS[fighter]["moves"][move]
    )

    critical = False

    if (
        fighter == "Ness"
        and move == "down"
    ):

        return move_name, 0, False

    damage += random.randint(-2, 2)

    if damage < 1:

        damage = 1

    if (
        fighter == "Luigi"
        and move == "up"
    ):

        if random.randint(1, 5) == 1:

            damage *= 2
            critical = True

    if fighter == "Cloud":

        if (
            move == "down"
            and player["limit"] >= 100
        ):

            damage += 10
            player["limit"] = 0

            print()
            print("LIMIT BREAK!")
            print()

    if fighter == "Little Mac":

        if (
            player["ko_meter"] >= 100
            and move == "neutral"
        ):

            move_name = "KO Punch"
            damage = 32

            player["ko_meter"] = 0

            print()
            print("KO PUNCH!!")
            print()

    return move_name, damage, critical


def enemy_choose_move(enemy, player):

    moves = [
        "neutral",
        "side",
        "up",
        "down"
    ]

    enemy_name = enemy["name"]

    enemy_moves = CHARACTERS[
        enemy_name
    ]["moves"]

    if (
        enemy["final_meter"] >= 100
        and not enemy["used_final"]
    ):

        if player["hp"] <= 45:

            return "final"

        if random.random() < 0.60:

            return "final"

    if (
        enemy_name == "Little Mac"
        and enemy["ko_meter"] >= 100
    ):

        if player["hp"] <= 50:

            return "neutral"

        if random.random() < 0.75:

            return "neutral"

    if (
        enemy_name == "Cloud"
        and enemy["limit"] >= 100
    ):

        if player["hp"] <= 60:

            return "down"

        if random.random() < 0.70:

            return "down"

    if enemy_name == "Ness":

        if enemy["hp"] <= 30:

            if random.random() < 0.65:

                return "down"

    if enemy_name == "Duck Hunt Duo":

        if enemy["hp"] <= 30:

            if random.random() < 0.65:

                return "up"

    if player["hp"] <= 30:

        strong_moves = []

        for move in moves:

            damage = enemy_moves[move][1]

            if damage >= 10:

                strong_moves.append(move)

        if strong_moves:

            if random.random() < 0.70:

                return random.choice(
                    strong_moves
                )

    if enemy_name == "Ness":

        if enemy["hp"] > 50:

            moves.remove("down")

    if enemy_name == "Duck Hunt Duo":

        if enemy["hp"] > 50:

            moves.remove("up")

    weighted_moves = []

    for move in moves:

        damage = enemy_moves[move][1]

        if damage >= 15:

            weighted_moves.extend(
                [move, move]
            )

        else:

            weighted_moves.append(move)

    return random.choice(
        weighted_moves
    )


def battle_round(player, enemy, round_number):

    show_status(player, enemy)

    print()
    print(f"ROUND {round_number}")
    print()

    player_move = choose_move(player)

    enemy_move = enemy_choose_move(
        enemy,
        player
    )

    round_start_hp = player["hp"]

    magnet_recovery = 0

    if (
        player["name"] == "Ness"
        and player_move == "down"
    ):

        magnet_recovery = min(
            10,
            75 - player["hp"]
        )

        player["hp"] += magnet_recovery

    player_move_name, player_damage, critical = (
        calculate_damage(
            player,
            player_move
        )
    )

    enemy_move_name, enemy_damage, enemy_critical = (
        calculate_damage(
            enemy,
            enemy_move
        )
    )

    print()

    if player_move == "final":

        print("FINAL SMASH")

        print(
            f"{player['name']} "
            f"used {player_move_name}!"
        )

        print(
            f"It dealt "
            f"{player_damage} damage!"
        )

    elif (
        player["name"] == "Ness"
        and player_move == "down"
    ):

        print("You used Magnet!")

        if magnet_recovery > 0:

            print(
                f"Ness recovered "
                f"{magnet_recovery} HP!"
            )

        else:

            print(
                "Ness is already at full HP!"
            )

    else:

        print(
            f"You used "
            f"{player_move_name}!"
        )

        if critical:

            print("CRITICAL HIT!")

    if (
        player["name"] == "Little Mac"
        and player_move == "down"
    ):

        print(
            "Little Mac waits for an attack..."
        )

        enemy_hits = (
            random.random() < 0.80
        )

        if enemy_hits:

            player_hp_before = player["hp"]

            print(
                "Enemy landed the attack!"
            )

            player["hp"] -= enemy_damage

            actual_damage = (
                player_hp_before
                - player["hp"]
            )

            print(
                "Slip Counter failed!"
            )

            print(
                f"You took "
                f"{actual_damage} damage!"
            )

        else:

            enemy_hp_before = enemy["hp"]

            print(
                "Enemy missed!"
            )

            counter = 22

            enemy["hp"] -= counter

            actual_counter_damage = (
                enemy_hp_before
                - enemy["hp"]
            )

            print(
                "Slip Counter activated!"
            )

            print(
                f"Enemy took "
                f"{actual_counter_damage} damage!"
            )

    else:

        enemy_hp_before = enemy["hp"]

        if player_move == "final":

            enemy["hp"] -= player_damage

            actual_damage = (
                enemy_hp_before
                - enemy["hp"]
            )

            print(
                f"Enemy took "
                f"{actual_damage} damage!"
            )

        elif (
            player["name"] == "Ness"
            and player_move == "down"
        ):

            pass

        elif random.random() < 0.80:

            enemy["hp"] -= player_damage

            actual_damage = (
                enemy_hp_before
                - enemy["hp"]
            )

            print(
                f"Enemy took "
                f"{actual_damage} damage!"
            )

        else:

            print("You missed!")

        if enemy["hp"] <= 0:

            enemy["hp"] = 0

            player["final_meter"] = min(
                player["final_meter"] + 20,
                100
            )

            if player["name"] == "Cloud":

                player["limit"] = min(
                    player["limit"] + 25,
                    100
                )

            if player["name"] == "Little Mac":

                player["ko_meter"] = min(
                    player["ko_meter"] + 20,
                    100
                )

            if player_move == "final":

                player["used_final"] = True
                player["final_meter"] = 0

            input(
                "\nPress ENTER to continue..."
            )

            return

        print()

        print(
            f"Enemy used "
            f"{enemy_move_name}"
        )

        if enemy_critical:

            print("Critical Hit!")

        if (
            enemy["name"] == "Ness"
            and enemy_move == "down"
        ):

            enemy_recovery = min(
                10,
                75 - enemy["hp"]
            )

            enemy["hp"] += enemy_recovery

            if enemy_recovery > 0:

                print(
                    f"Ness recovered "
                    f"{enemy_recovery} HP!"
                )

            else:

                print(
                    "Ness is already at full HP!"
                )

        elif enemy_move == "final":

            print()

            player_hp_before = player["hp"]

            if random.random() < 0.80:

                player["hp"] -= enemy_damage

                actual_damage = (
                    round_start_hp
                    - player["hp"]
                )

                print(
                    f"You took "
                    f"{actual_damage} damage!"
                )

            else:

                print("Enemy missed!")

        elif random.random() < 0.80:

            player_hp_before = player["hp"]

            player["hp"] -= enemy_damage

            if (
                player["name"] == "Ness"
                and player_move == "down"
            ):

                actual_damage = (
                    round_start_hp
                    - player["hp"]
                )

            else:

                actual_damage = (
                    player_hp_before
                    - player["hp"]
                )

            print(
                f"You took "
                f"{actual_damage} damage!"
            )

        else:

            print("Enemy missed!")

    player["final_meter"] = min(
        player["final_meter"] + 20,
        100
    )

    enemy["final_meter"] = min(
        enemy["final_meter"] + 20,
        100
    )

    if player["name"] == "Cloud":

        player["limit"] = min(
            player["limit"] + 25,
            100
        )

    if enemy["name"] == "Cloud":

        enemy["limit"] = min(
            enemy["limit"] + 25,
            100
        )

    if player["name"] == "Little Mac":

        player["ko_meter"] = min(
            player["ko_meter"] + 20,
            100
        )

    if enemy["name"] == "Little Mac":

        enemy["ko_meter"] = min(
            enemy["ko_meter"] + 20,
            100
        )

    if player_move == "final":

        player["used_final"] = True
        player["final_meter"] = 0

    if enemy_move == "final":

        enemy["used_final"] = True
        enemy["final_meter"] = 0

    player["hp"] = max(
        0,
        player["hp"]
    )

    enemy["hp"] = max(
        0,
        enemy["hp"]
    )

    if (
        player["name"] == "Ness"
        and player_move == "down"
        and player["hp"] > round_start_hp
    ):

        net_recovery = (
            player["hp"]
            - round_start_hp
        )

        if net_recovery > magnet_recovery:

            print(
                f"Ness gained "
                f"{net_recovery} HP overall!"
            )

    print()

    print(
        f"Final Smash Meter: "
        f"{player['final_meter']}%"
    )

    input(
        "\nPress ENTER to continue..."
    )


def choose_enemy(player_name):

    fighters = list(
        CHARACTERS.keys()
    )

    fighters.remove(
        player_name
    )

    enemy = random.choice(
        fighters
    )

    print()

    print(
        f"Your opponent is {enemy}!"
    )

    print()

    return enemy


def battle(player_name):

    enemy_name = choose_enemy(
        player_name
    )

    player = create_fighter(
        player_name
    )

    enemy = create_fighter(
        enemy_name
    )

    round_number = 1

    while (
        player["hp"] > 0
        and enemy["hp"] > 0
    ):

        battle_round(
            player,
            enemy,
            round_number
        )

        round_number += 1

        time.sleep(0.5)

    print()

    print(
        "=" * 60
    )

    if player["hp"] > 0:

        print("VICTORY!")

        print()

        print(
            f"{player['name']} "
            f"defeated "
            f"{enemy['name']}!"
        )

    else:

        print("DEFEAT!")

        print()

        print(
            f"{enemy['name']} "
            f"defeated "
            f"{player['name']}!"
        )

    print(
        "=" * 60
    )


def play_again():

    while True:

        choice = input(
            "\nPlay Again? (y/n): "
        ).lower()

        if choice in [
            "y",
            "yes"
        ]:

            return True

        if choice in [
            "n",
            "no"
        ]:

            return False

        print(
            "Please enter y or n."
        )


def main():

    title()

    while True:

        player = choose_character()

        print()

        print(
            f"You chose {player}!"
        )

        print()

        input(
            "Press ENTER to begin "
            "the battle..."
        )

        battle(
            player
        )

        if not play_again():

            break

    print()

    print(
        "=" * 60
    )

    print(
        "Thanks for playing!"
    )

    print(
        "Super Smash Bros. Ultimate "
        "- Python Edition"
    )

    print(
        "=" * 60
    )


if __name__ == "__main__":

    main()
