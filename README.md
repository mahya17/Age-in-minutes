# Age in Minutes ⏳

A Python program that calculates a person's age in minutes and writes the result in English words.

## About the Project

The program asks the user to enter their birth date in `YYYY-MM-DD` format and calculates how many minutes have passed from that date until today.

For simplicity, both the birth time and the current time are considered to be midnight.

The calculated number of minutes is then converted into English words instead of being displayed as a number.

## How It Works

The program takes a birth date as input:

```text
Birthdate: 2020-01-01
```

It calculates the difference between the birth date and the current date using Python's `datetime` module.

The result is then converted from days to minutes and written out in English words.

For example, one year corresponds to:

```text
Five hundred twenty-five thousand, six hundred minutes
```

The program also handles incorrectly formatted dates without displaying an exception.

## Testing

The project includes a separate `test_seasons.py` file for testing the functions used by the program.

Tests can be run with:

```bash
pytest test_seasons.py
```

The tests check different cases to make sure the program correctly calculates and formats the number of minutes.

## What I Practiced

* Working with the `datetime` module
* Using `date`
* Calculating the difference between dates
* Working with `timedelta`
* Converting days into minutes
* Handling date input
* Using `sys.exit()`
* Writing numbers in English words
* Creating functions
* Writing automated tests with `pytest`
* Testing functions separately from `main()`

## Technologies

* Python
* datetime
* inflect
* pytest

## Installation

Install the required packages with:

```bash
pip install inflect
```

## Course

This project was completed as part of **CS50's Introduction to Programming with Python** by Harvard University.
