# Expense Tracker

A small terminal-based expense tracker built with Python. It stores entries in a local JSON file, so the records remain available the next time you run it.

## Features

- Add, view, search, and delete expenses
- Validate names, categories, and positive amounts
- Show total and average spending
- Summarize spending by category
- Handle missing or invalid JSON data with a useful message
- Save data using a temporary file before replacing the saved file

## Requirements

- Python 3.10 or newer
- No third-party packages are required

## Run it

```bash
python main.py
```

Choose an option from the menu and follow the prompts. The program stores data in `expenses.json` next to `main.py`.

## Data note

The included `expenses.json` contains example records. Replace them with an empty JSON list (`[]`) if you want to start fresh. Do not commit real personal spending records to a public repository.

## Project structure

```text
expense-tracker-python/
├── main.py
├── expenses.json
├── .gitignore
└── readme.md
```
