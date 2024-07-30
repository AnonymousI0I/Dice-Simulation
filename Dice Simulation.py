import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def main():
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (or 0 to quit): "))
            if num_dice == 0:
                print("Exiting the program. Goodbye!")
                break
            elif num_dice < 0:
                print("Please enter a positive integer or 0 to quit.")
            else:
                results = roll_dice(num_dice)
                print(f"Rolling {num_dice} dice: {results}")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
