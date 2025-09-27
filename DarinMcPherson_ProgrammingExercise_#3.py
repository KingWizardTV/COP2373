# ------------------------------------------------------------
# Darin McPherson
# 09/27/2025
# Programming Exercise 3
# Monthly Expense Analyzer
#
# Description:
# Prompts the user for (expense type, amount) pairs. Uses
# functools.reduce to compute the total, highest, and lowest
# expenses. Clearly labels which expense is highest/lowest.
#
# Notes:
# - Input ends when the user leaves the type blank or types 'done'.
# - Amounts must be non-negative numbers.
# - All logic is organized into functions (no top-level execution).
# ------------------------------------------------------------

from functools import reduce
from typing import List, Tuple

# CONSTANTS (UPPERCASE)
CURRENCY_SYMBOL: str = "$"


def prompt_expenses() -> List[Tuple[str, float]]:
    """Collect (name, amount) expense entries from the user."""
    # Initialize the container for expense tuples
    expenses: List[Tuple[str, float]] = []

    # Explain how to finish input
    print("Enter your monthly expenses. Leave the type blank or type 'done' to finish.\n")

    # Loop until the user stops entering items
    while True:
        # Ask for the expense type
        name = input("Expense type (e.g., Rent, Groceries): ").strip()

        # End condition for data entry
        if name == "" or name.lower() == "done":
            break

        # Keep asking for a valid amount for this expense
        while True:
            # Get the raw amount as text (allow commas)
            raw = input(f"Amount for '{name}': ").strip().replace(",", "")
            try:
                # Convert to float
                amount = float(raw)

                # Validate non-negative
                if amount < 0:
                    print("Amount cannot be negative. Please enter a non-negative number.")
                    continue

                # Break once valid
                break
            except ValueError:
                print("Please enter a valid number (e.g., 1200 or 1200.50).")

        # Append a (name, amount) tuple
        expenses.append((name, amount))

        # Add a blank line for readability
        print()

    # Return all captured expenses
    return expenses


def analyze_expenses(expenses: List[Tuple[str, float]]) -> Tuple[float, Tuple[str, float], Tuple[str, float]]:
    """Use reduce to compute total, highest, and lowest expense."""
    # Calculate the total using reduce (accumulator starts at 0.0)
    total = reduce(lambda acc, item: acc + item[1], expenses, 0.0)

    # Calculate the highest expense (carry full tuple for labeling)
    highest = reduce(lambda acc, item: item if item[1] > acc[1] else acc, expenses)

    # Calculate the lowest expense (carry full tuple for labeling)
    lowest = reduce(lambda acc, item: item if item[1] < acc[1] else acc, expenses)

    # Return all three results
    return total, highest, lowest


def main() -> None:
    """Main entry point for the Monthly Expense Analyzer."""
    # Prompt the user to enter expenses
    expenses = prompt_expenses()

    # Handle the no-data case gracefully
    if not expenses:
        print("\nNo expenses entered. Nothing to analyze.")
        return

    # Analyze the expense list with reduce-based functions
    total, highest, lowest = analyze_expenses(expenses)

    # Print a formatted summary for the user
    print("\n=== Monthly Expense Summary ===")
    print(f"Total Expenses: {CURRENCY_SYMBOL}{total:,.2f}")
    print(f"Highest Expense: {highest[0]} — {CURRENCY_SYMBOL}{highest[1]:,.2f}")
    print(f"Lowest  Expense: {lowest[0]} — {CURRENCY_SYMBOL}{lowest[1]:,.2f}")


if __name__ == "__main__":
    # Run the main function only when executed directly
    main()
