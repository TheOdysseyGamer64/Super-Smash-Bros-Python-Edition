# Super Smash Bros. Python Edition

<img width="819" height="228" alt="Super Smash Bros. Python Edition banner" src="https://github.com/user-attachments/assets/58b3c0e1-82a5-40f3-a936-f2b69e77bf77" />

**Super Smash Bros. Python Edition** is a fan-made, text-based fighting game inspired by the Super Smash Bros. series. Choose a fighter, face a CPU opponent, and use their moves and special mechanics to win the battle.

<img width="550" height="600" alt="Gameplay preview" src="https://github.com/user-attachments/assets/a470d2cf-cafa-4523-b679-ff1f772c8ae7" />

## Download

The latest published release is **v1.4.0**. The v1.5.0 work is still being prepared, so the download below links to the latest published release.

[Download Super Smash Bros. Python Edition v1.4.0](https://github.com/TheOdysseyGamer64/Super-Smash-Bros-Python-Edition/archive/refs/tags/1.4.0.zip)

You can also browse the project's [Releases](https://github.com/TheOdysseyGamer64/Super-Smash-Bros-Python-Edition/releases) page.

## Features

- Playable fighters with different stats and moves
- Turn-based battles against CPU opponents
- Fighter-specific attacks and mechanics
- Final Smash meter and powerful Final Smash attacks
- HP and damage system
- Attack or block during a turn
- ASCII battle arena, fighter sprites, and health bars
- Coloured terminal output when Colorama is installed

## Fighter-specific mechanics

The current development code includes resource mechanics for several fighters:

| Fighter | Mechanic |
| --- | --- |
| Mario | Fire Charge can empower Fireball |
| Luigi | Misfire Charge can power up Green Missile |
| Sora | Magic Points can boost special moves |
| Mii Swordfighter | Technique Charges can empower special moves |
| Duck Hunt Duo | Ammo Supply powers up selected attacks; running out reduces their damage |
| Ness | PSI Energy can boost selected attacks; Magnet can recover HP |
| Kirby | Copy Charge can empower attacks |
| Kazuya | Rage builds based on missing HP; Rage Drive spends Rage |
| R.O.B. | Fuel can boost selected attacks |
| Cloud | Limit Gauge and Limit Break |
| Little Mac | KO Meter and KO Punch |
| Terry | GO! moves become available at low HP |

Resource values, costs, and effects are part of the game's balancing and may change as v1.5.0 development continues.

### Final Smash

Build the Final Smash Meter during battle. Once it reaches **100%**, a Final Smash becomes available, provided it has not already been used.

### Cloud: Limit Gauge

Cloud builds the Limit Gauge and can use Limit Break when the gauge is full.

### Little Mac: KO Meter

Little Mac builds his KO Meter. At **100%**, his neutral attack can become KO Punch.

### Terry: GO!

Terry's GO! moves become available when his HP reaches **35 or below**.

## Requirements

- Python 3.10 or newer is recommended.
- A terminal or Python editor, such as IDLE or VS Code.
- The main `smash.py` program uses the accompanying `characters.json` file. Keep both files in the same folder.
- [Colorama](https://pypi.org/project/colorama/) is optional and enables coloured terminal output. The game can fall back to uncoloured output if Colorama is not installed.

To install Colorama, run:

```bash
python -m pip install colorama
```

## How to play

1. Download and extract the project, or clone the repository.
2. Open a terminal in the project folder.
3. Run the main program:

   ```bash
   python smash.py
   ```

   Or run the standalone version:

   ```bash
   python smash.v.1.5.0.py
   ```

4. Follow the prompts to choose a fighter and make your moves.

You can also open a Python file in IDLE and press **F5**, or use the Run control in your editor.

## Development and tests

The repository includes automated tests. To run them locally, install pytest and run:

```bash
python -m pip install pytest
python -m pytest -q
```

The project also uses Ruff for Python lint checks. Passing automated checks helps catch problems, but does not replace trying the game in a terminal.

## Screenshots

### Starting the game

<img width="550" height="600" alt="Gameplay at startup" src="https://github.com/user-attachments/assets/a470d2cf-cafa-4523-b679-ff1f772c8ae7" />

### Fighters without special mechanics

<img width="500" height="400" alt="Fighter selection preview" src="https://github.com/user-attachments/assets/cc1cc7b0-8190-4972-a55e-538e6111003a" />

### Fighters with special mechanics

<img width="600" height="450" alt="Resource meter preview" src="https://github.com/user-attachments/assets/6e522e0b-bdac-459f-92d1-eeab22be7d01" />

### Fully charged mechanics

<img width="600" height="700" alt="Fully charged mechanic preview" src="https://github.com/user-attachments/assets/a9409d90-faea-49ed-b9cb-6b1a3b3094a9" />

Screenshots show earlier gameplay and may not reflect every change in the current development version.

## Disclaimer

This is a **fan-made, non-commercial project** inspired by Super Smash Bros. Super Smash Bros. and its characters are the property of their respective copyright and trademark holders. This project is not affiliated with, endorsed by, or sponsored by Nintendo or any other rights holder.

There may still be bugs. The project is a learning experience, and fixes and improvements will continue as development progresses.

---

Thanks for playing **Super Smash Bros. Python Edition**!

**Diesel**
