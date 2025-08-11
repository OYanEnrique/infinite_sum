# infinite_sum
A Python script for basic statistical analysis on user-provided numbers. It interactively collects numbers and calculates their average, maximum, and minimum values.

# Simple Statistics Calculator (Average, Max, Min)

This command-line script allows a user to enter a series of numbers and then calculates basic statistics for the set. The program uses a `while` loop that continues as long as the user wishes to add more numbers (by responding 'Y').

Once the user decides to stop (by responding 'N'), it computes and displays the average, the highest value (maximum), and the lowest value (minimum) from all the numbers provided.

## Features

-   Interactively accepts a sequence of numbers from the user.
-   Loop continuation is controlled by a simple `Y/N` prompt.
-   Calculates the average of the entered numbers.
-   Tracks and identifies the maximum (greatest) value.
-   Tracks and identifies the minimum (lowest) value.
-   Displays a formatted summary of all results.

## How to Run

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed.
2.  Save the code as a Python file (e.g., `infinite_sum.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is located.
5.  Execute the script using:
    ```bash
    python infinite_sum.py
    ```

## Usage Example

The user can enter several numbers, confirming with 'Y' (or 'y') to continue. To stop and see the results, the user enters 'N' (or 'n').

```
Enter a number:
10
Want to continue, Y or N? y
Enter a number:
25
Want to continue, Y or N? Y
Enter a number:
5
Want to continue, Y or N? n
The average is 13.33
The greater number was 25
The lower number was 5
```
