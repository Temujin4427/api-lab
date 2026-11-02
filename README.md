# api-lab

## Input Domain Model for POST /api/ratings

| Characteristic    | Blocks                | Values in the tests | Test function                |
| ----------------- | --------------------- | ------------------- | ---------------------------- |
| C1 Value of stars | below 1               | 0                   | `test_stars_out_of_range[0]` |
|                   | 1 to 5 (base)         | 3                   | `test_base_choice_is_saved`  |
|                   | above 5               | 6                   | `test_stars_out_of_range[6]` |
| C2 Type of stars  | whole number (base)   | 3                   | `test_base_choice_is_saved`  |
|                   | decimal               | 3.5                 | `test_stars_decimal`         |
|                   | text                  | "3"                 | `test_stars_text`            |
|                   | missing               | no field            | `test_stars_missing`         |
| C3 Pizza          | exists (base)         | a new pizza         | `test_base_choice_is_saved`  |
|                   | does not exist        | 999999999           | `test_pizza_does_not_exist`  |
| C4 Token          | the user's own (base) | from auth           | `test_base_choice_is_saved`  |
|                   | none                  | no header           | `test_token_missing`         |
|                   | wrong length          | token short         | `test_token_short`           |

## How to run

Windows (PowerShell):

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v --html=report.html --self-contained-html
```

macOS / Linux: use `source .venv/bin/activate` instead of `.venv\Scripts\activate`.
