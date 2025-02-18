# testing-auto-create-file
This Python script automatically creates a new directory for each day and generates a .txt file every 10 minutes with a timestamped filename, managing directories and files across day transitions.


## Python Script for Auto-Generating Date Directories and Files

This is a Python script that automatically creates a `.txt` file every 10 minutes in a directory named with the current date (YYYY-MM-DD). The filename includes the current timestamp (YYYY-MM-DD_HH-MM-SS). The script writes arbitrary test content into the file. If the directory for the current day does not exist, it will automatically create a new directory. At midnight (24:00), the script will automatically switch to a new day's directory.

## Features
- Creates a new file every 10 minutes with a filename containing the timestamp (year-month-day-hour-minute-second).
- Automatically manages date directories, creating a new directory for each day if it does not exist.
- Continuously runs until manually stopped.
- Automatically creates a new directory when the date changes at midnight.

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/kancheng/testing-auto-create-file.git
   cd testing-auto-create-file
   ```

2. Run the script:
   ```bash
   python m.py
   ```

## Code Structure
- `m.py`: Main script that checks for and creates directories and files.

## Contributing
Feel free to submit pull requests to improve this script or suggest new features.
