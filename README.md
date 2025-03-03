# Console Calculator

A simple console-based calculator written in Python. The calculator supports basic arithmetic operations and allows for continuous calculations based on previous results.

## Features
- Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Keeps track of the last result and allows further operations on it.
- Handles invalid input and provides user-friendly prompts.
- Detects and prevents division by zero.
- Allows the user to exit by entering `q`.

## Usage
1. Run the script:
   ```sh
   python calc.py
   ```
2. Enter an equation in the format:
   ```
   number operator number
   ```
   Example:
   ```
   5 + 5
   ```
   Output:
   ```
   Result = 10.0
   ```
3. To continue calculations using the last result, enter another equation:
   ```
   + 5
   ```
   Output:
   ```
   Result = 15.0
   ```
4. To exit, type `q`.

## Example Session
```
Input the equation: 5 + 5
Result = 10.0
Input the equation: * 2
Result = 20.0
Input the equation: - 4
Result = 16.0
Input the equation: q
BYE!
```

## Error Handling
- If an invalid format is entered, the program prompts the user to input the equation correctly.
- Division by zero is caught and reported as an error.

## Installation
Make sure you have Python installed, then clone the repository:
```sh
git clone https://github.com/m0urn1ngl1d/console_calc.git
cd console_calc
python calc.py
```
---

Happy calculating! 😊

