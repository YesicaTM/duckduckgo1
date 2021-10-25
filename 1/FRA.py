# asks the user for a birth year and month,
# displays the age (with additional months) for obtaining full SSA benefits
# displays the year and month for obtaining full SSA benefits
# separate user interaction from calculation
import sys


def main():
    # ask for birth month and year, if "" for birth year, exit. if not, continue.
    # print retirement age and month, then calculate user specific retirement year and month and print
    birth_y = input("Enter the year of birth or to exit: ")

    if birth_y == "":
        sys.exit()
    else:
        birth_y = int(birth_y)
        birth_m = int(input("Enter the month of birth: "))

    # find age and month of retirement from birth year
    retire_age, retire_m = retirement_age(birth_y)

    # calculate specific year and month of user retirement
    user_retire_y, user_retire_m_num = calc(birth_y, retire_age, birth_m, retire_m)

    print("Your full retirement age is", retire_age, "and", retire_m, "months")
    print("This will be in", month_switch(user_retire_m_num), "of", user_retire_y)


def calc(birth_y, retire_age, birth_m, retire_m):
    # find specific user retirement year and month

    # add birth year to retirement age
    user_retire_y = birth_y + retire_age
    # add birth month to retirement month, if months go over 12 add a year
    user_retire_m_num = birth_m + retire_m
    if user_retire_m_num > 12:
        user_retire_y += 1
        # remainder of 12 equals user month retirement
        user_retire_m_num = user_retire_m_num % 12

    return user_retire_y, user_retire_m_num


def month_switch(month_num):
    # for converting month number to string
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        }
    return months[month_num]


def retirement_age(year):
    # FINISH SETTING ALL RETIRE AGES AND MONTHS
    if 1937 >= year >= 1900:
        retire_age = 65
        retire_month = 0
    elif year == 1938:
        retire_age = 65
        retire_month = 2
    elif year == 1939:
        retire_age = 65
        retire_month = 4
    elif year == 1940:
        retire_age = 65
        retire_month = 6
    elif year == 1941:
        retire_age = 65
        retire_month = 8
    elif year == 1942:
        retire_age = 65
        retire_month = 10
    elif 1954 >= year >= 1943:
        retire_age = 66
        retire_month = 0
    elif year == 1955:
        retire_age = 66
        retire_month = 2
    elif year == 1956:
        retire_age = 66
        retire_month = 4
    elif year == 1957:
        retire_age = 66
        retire_month = 6
    elif year == 1958:
        retire_age = 66
        retire_month = 8
    elif year == 1959:
        retire_age = 66
        retire_month = 10
    elif 2021 >= year >= 1960:
        retire_age = 67
        retire_month = 0
    else:
        print("invalid birth year")
        sys.exit()

    return retire_age, retire_month


if __name__ == '__main__':
    main()
