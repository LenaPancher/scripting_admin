
def user_input():
    while True:
        input_year = input("Enter a leap year: ")
        year = int(input_year) if input_year.isdigit() else None
        if year is None:
            print("The value you entered is not a number")
            continue
        if is_leap(year):
            print(input_year + " is a leap year")
        else:
            print(input_year + " is not a leap year")


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


if __name__ == '__main__':
    user_input()
