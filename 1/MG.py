# asks the user for his score in each of the items contributing to the final grade
# calculates the user’s final grade using the grading weights from Course Resources
# displays the user’s final grade.

def main():
    # ask how many grades for labs(34), midterm(33) and final(33)
    # return final grade

    lab_list = []
    num_labs = int(input("Enter the number of graded labs: "))
    for x in range(num_labs):
        print("Enter grade for Lab", x + 1)
        grade = int(input())
        lab_list.append(grade)
    midterm = int(input("Enter midterm exam grade: "))
    final = int(input("Enter final exam grade: "))

    print("Your final grade is: ", total_grade(lab_list, midterm, final))


def calc_ave(list1):
    # calculate average for labs
    total = 0
    for x in range(len(list1)):
        total += list1[x]
    ave = total/len(list1)

    return ave


def calc_lab(lab_list):
    # calculate points for lab
    lab_grade = calc_ave(lab_list)
    lab_points = (lab_grade * 34) / 100

    return lab_points


def calc_test(test):
    # calculate points for midterm and final
    test_points = (test * 33) / 100

    return test_points


def total_grade(labs, midterm, final):
    # calculate total grade
    mygrade = calc_lab(labs) + calc_test(midterm) + calc_test(final)
    mygrade = round(mygrade, 2)
    return mygrade


if __name__ == '__main__':
    main()
