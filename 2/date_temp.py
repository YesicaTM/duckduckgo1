import sys


class DateTemp:
    # constructor with date and time and dic to store them
    def __init__(self, date, temp):
        self.date = date
        self.temp = temp

    def __str__(self):
        return "Date: " + str(self.date) + " Temperature: " + str(self.temp) + "F"


# end of class

# Start of main containing user interaction
# present menu
# implement DateTemp class
# loop to allow user various entries
# list to maintain user info in order submitted
# ability to sort by date and time


def main():
    list1 = []
    while True:
        print("[1] Enter a date and temperature")
        print("[2] Display all date and temperature information in the order entered")
        print("[3] Display all date and temperature information by date")
        print("[4] Display all date and temperature information by temperature")
        print("[5] Exit")
        user = int(input("Enter your menu option: "))

        # read choice and execute it
        if user == 1:
            date = int(input("Enter date in yyyymmdd format: "))
            temp = int(input("Enter corresponding temperature in Fahrenheit: "))
            obj = DateTemp(date, temp)
            list1.append(obj)
        elif user == 2:
            for x in range(len(list1)):
                print(list1[x])
        elif user == 3:
            list2 = sorted(list1, key=lambda l: l.date)
            for x in range(len(list2)):
                print(list2[x])
        elif user == 4:
            list3 = sorted(list1, key=lambda l: l.temp)
            for x in range(len(list3)):
                print(list3[x])
        elif user == 5:
            sys.exit()
        else:
            print('Invalid, try again.')


if __name__ == '__main__':
    main()
