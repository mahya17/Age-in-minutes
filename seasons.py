from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Date of Birth: ")
    try:
        year, month, day = birthdate.split("-")
        birth = date(int(year), int(month), int(day))
    except Exception:
        sys.exit(1)

    today = date.today()
    delta = today - birth
    minutes = delta.days * 24 * 60

    words = p.number_to_words(minutes, andword="")
    words = words.capitalize()

    print(f"{words} minutes")


if __name__ == "__main__":
    main()
