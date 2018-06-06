from compute import *
import os
import sys

path = os.path.dirname(os.path.realpath(__file__))
# making a file object
class_info = open(os.path.join(path, 'class.txt'))
a1_info = open(os.path.join(path, 'a1.txt'))
a2_info = open(os.path.join(path, 'a2.txt'))
project_info = open(os.path.join(path, 'project.txt'))
test1_info = open(os.path.join(path, 'test1.txt'))
test2_info = open(os.path.join(path, 'test2.txt'))


class_list = class_info.read().splitlines()
a1_list = a1_info.read().splitlines()
a2_list = a2_info.read().splitlines()
project_list = project_info.read().splitlines()
test1_list = test1_info.read().splitlines()
test2_list = test2_info.read().splitlines()

# assigning maximum values of individual component
Student.maxa1 = int(a1_list[0])
Student.maxa2 = int(a2_list[0])
Student.maxproject = int(project_list[0])
Student.maxt1 = int(test1_list[0])
Student.maxt2 = int(test2_list[0])

for line in class_list:
    a, b, c = line.split('|')
    s = Student(a, b, c)
    studentList.append(s)
    '''print(s.id)
        print(s.firstname)
        print(s.lastname)
        print(studentList[x].id)
    x += 1'''

# assigning numbers to all the students
for line in a1_list[1:]:
    a, b = line.split('|')
    b = int(b)
    for s in studentList:
        if s.id == a:
            s.a1marks = b

for line in a2_list[1:]:
    a, b = line.split('|')
    b = int(b)
    for s in studentList:
        if s.id == a:
            s.a2marks = b

for line in project_list[1:]:
    a, b = line.split('|')
    b = int(b)
    for s in studentList:
        if s.id == a:
            s.projectmarks = b

for line in test1_list[1:]:
    a, b = line.split('|')
    b = int(b)
    for s in studentList:
        if s.id == a:
            s.t1marks = b

for line in test2_list[1:]:
    a, b = line.split('|')
    b = int(b)
    for s in studentList:
        if s.id == a:
            s.t2marks = b

for s in studentList:
    s.numerictotal = s.calculateNumericTotal()
    s.assignLetterGrade()

x = 0

while x is not 1:
    print("1> Display individual component")
    print("2> Display component average")
    print("3> Display standard report")
    print("4> Sort by alternate column")
    print("5> Change pass/fail point")
    print("6> Exit")
    user_input = input("Please select one of the above options: ")

    if user_input == "1":
        seprateComponent()

    elif user_input == "2":
        averageComponent()

    elif user_input == "3":
        Student.threshold = 50
        studentList = sortID()
        printStandard()

    elif user_input == "4":
        inputfour()

    elif user_input == "5":
        passfail = input("Please enter the Pass/Fail number: ")
        passfail = int(passfail)
        Student.threshold = passfail
        printStandard()


    elif user_input == "6":
        x = 1
        print("Good Bye")

    else:
        print("Wrong Entry!!")
        x = 9

    print()