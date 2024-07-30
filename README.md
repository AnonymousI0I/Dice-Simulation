# Dice Rolling Simulator

This Python script simulates rolling a specified number of dice. The main functionalities include:

1. Rolling any number of dice at once.
2. Input validation to handle non-integer inputs and negative numbers.
3. Option to exit the program by entering 0.

## Features

- **Roll Any Number of Dice**: Roll a user-specified number of dice.
- **Input Validation**: Ensures only valid integer inputs.
- **Exit Option**: Allows the user to exit the program gracefully.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/dice-rolling-simulator.git
    cd dice-rolling-simulator
    ```

2. **Ensure Python 3.x is installed on your machine**.

## Usage

1. **Run the script**:

    ```bash
    python roll_dice.py
    ```

2. **Follow the on-screen prompts to roll the dice or exit the program**:

### Rolling Dice

- You will be prompted to enter the number of dice to roll.
- The program will display the results of each dice roll.

    Example:

    ```
    Enter the number of dice to roll (or 0 to quit): 3
    Rolling 3 dice: [4, 2, 5]
    Enter the number of dice to roll (or 0 to quit): 0
    Exiting the program. Goodbye!
    ```

## Code Overview

### Function Descriptions

#### `roll_dice(num_dice)`

Simulates rolling a specified number of dice and returns the results.

- **Parameters**:
  - `num_dice` (int): The number of dice to roll.
- **Returns**:
  - `list`: A list of integers representing the results of each dice roll.

#### `main()`

Handles user input and orchestrates the workflow of the program.

- Prompts the user to enter the number of dice to roll.
- Calls `roll_dice(num_dice)` to roll the dice.
- Displays the results.
- Allows the user to exit the program by entering 0.

### Example Workflow

When you run the program, you will see prompts like this:

Enter the number of dice to roll (or 0 to quit): 3
Rolling 3 dice: [4, 2, 5]
Enter the number of dice to roll (or 0 to quit): 0
Exiting the program. Goodbye!


## Contribution

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
