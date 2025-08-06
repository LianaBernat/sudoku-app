# Sudoku Game (Python CLI)

## 📌 Description
How about a fun little game where you don't risk your money? 😲😂
This is Sudoku game developed in **Python** to be played directly at the **terminal**.
I developed this game to learn more about Numpy and Pandas and project structure.

## 📜 Rules
1. Each row must contain the numbers 1-9 exactly once.
2. Each column must contain the numbers 1-9 exactly once.
3. Each of the nine 3x3 sub-grids (also called "boxes") must contain the numbers 1-9 exactly
once.

The puzzle begins with some numbers already filled in, and your goal is to fill in the remaining
empty squares while following these three rules.
At the beginnig, you can choose the difficulty level:
        - 1: Easy (only 10% empty cells)
        - 2: Medium (20% empty cells)
        - 3: Hard (40% empty cells)

## 🛠 Technologies
- Python
- Pandas
- NumPy

## 🎮 Features
✔ Board display at the terminal
✔ Board initial display with hidden positions
✔ Moves Validation (line, column and 3x3 block)
✔ Clear messages for hits,erros and invalid positions
✔ Option to quit the game at any time (`q`)
✔ Randomization of the initial board to play the game.
✔ 3 Difficulty levels

## ▶ How to play
1. Clone this repository:
   ```bash
   git clone git@github.com:LianaBernat/sudoku-app.git
   cd sudoku-app
   python -m app.game
