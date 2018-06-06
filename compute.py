class Student:

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    a1marks = 0
    a2marks = 0
    projectmarks = 0
    t1marks = 0
    t2marks = 0
    grade = "F"
    defaultPassFail = 50

    threshold = 50
    numerictotal = 0
    maxa1 = 0
    maxa2 = 0
    maxproject = 0
    maxt1 = 0
    maxt2 = 0

    def calculateNumericTotal(self):
        return round((self.a1marks/self.maxa1)*7.5 + (self.a2marks/self.maxa2)*7.5 \
               + (self.projectmarks/self.maxproject)*25 + (self.t1marks/self.maxt1)*30 \
               + (self.t2marks/self.maxt2)*30, 2)

    def assignLetterGrade(self):
        passingNumberRange = 101 - self.threshold
        range = passingNumberRange/7

        if self.numerictotal < self.threshold:
            self.grade = "F"
        elif self.numerictotal >= self.threshold and self.numerictotal < (self.threshold + range):
            self.grade = "C"
        elif self.numerictotal >= (self.threshold + range) and self.numerictotal < (self.threshold + 2*range):
            self.grade = "B-"
        elif self.numerictotal >= (self.threshold + 2*range) and self.numerictotal < (self.threshold + 3*range):
            self.grade = "B"
        elif self.numerictotal >= (self.threshold + 3*range) and self.numerictotal < (self.threshold + 4*range):
            self.grade = "B+"
        elif self.numerictotal >= (self.threshold + 4*range) and self.numerictotal < (self.threshold + 5*range):
            self.grade = "A-"
        elif self.numerictotal >= (self.threshold + 5*range) and self.numerictotal < (self.threshold + 6*range):
            self.grade = "A"
        elif self.numerictotal >= (self.threshold + 6*range) and self.numerictotal < 101:
            self.grade = "A+"


studentList = []




validentries = ["a1","A1", "a2", "A2", "PR", "pr", "Pr", "pR", "t1", "T1", "t2", "T2"]

def printStandard():
    print()
    print("ID     " + "LN     " + "FN     "
          + "A1     " + "A2     " + "PR     " + "T1     " + "T2     "
          + "GR     " + "FL     ")
    studentList = sortID()
    for s in studentList:
        s.numerictotal = s.calculateNumericTotal()
        s.assignLetterGrade()
        print(s.id, end="")
        print("  ", end="")

        print(s.lastname, end="")
        if len(s.lastname) != 6:
            x = 7 - len(s.lastname)
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        print(s.firstname, end="")
        if len(s.firstname) != 6:
            x = 7 - len(s.firstname)
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        if(s.a1marks == 0):
            print(" ", end="")
            if len(str(s.a1marks)) != 6:
                x = 7 - len(str(s.a1marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.a1marks, end="")
            if len(str(s.a1marks)) != 6:
                x = 7 - len(str(s.a1marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.a2marks == 0):
            print(" ", end="")
            if len(str(s.a2marks)) != 6:
                x = 7 - len(str(s.a2marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.a2marks, end="")
            if len(str(s.a2marks)) != 6:
                x = 7 - len(str(s.a2marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.projectmarks == 0):
            print(" ", end="")
            if len(str(s.projectmarks)) != 6:
                x = 7 - len(str(s.projectmarks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.projectmarks, end="")
            if len(str(s.projectmarks)) != 6:
                x = 7 - len(str(s.projectmarks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.t1marks == 0):
            print(" ", end="")
            if len(str(s.t1marks)) != 6:
                x = 7 - len(str(s.t1marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.t1marks, end="")
            if len(str(s.t1marks)) != 6:
                x = 7 - len(str(s.t1marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.t2marks == 0):
            print(" ", end="")
            if len(str(s.t2marks)) != 6:
                x = 7 - len(str(s.t2marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.t2marks, end="")
            if len(str(s.t2marks)) != 6:
                x = 7 - len(str(s.t2marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        print(s.numerictotal, end="")
        if len(str(s.numerictotal)) != 6:
            x = 7 - len(str(s.numerictotal))
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        print(s.grade, end="")

        print()


def seprateComponent():
    component = input("Please indicate the component marks you wish to see: ")

    while not component in validentries:
        print("Wrong entry!!")
        component = input("Please indicate the component marks you wish to see: ")
    print()
    if component == "a1" or component == "A1":
        print("A1 grades " + "(" + str(Student.maxa1) + ")")
        for s in studentList:
            print(s.id, " ", end="")
            print(s.lastname + ",", end=" ")
            print(s.firstname, end=" ")
            if len(s.firstname + s.lastname + " " + ",") != 15:
                x = 15 - len(s.firstname + s.lastname + " " + ",")
                while x != 1:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")

            if s.a1marks == 0:
               print(" ")
            else:
                print(s.a1marks)

    elif component == "a2" or component == "A2":
        print("A2 grades " + "(" + str(Student.maxa2) + ")")
        for s in studentList:
            print(s.id, " ", end="")
            print(s.lastname + ",", end=" ")
            print(s.firstname, end=" ")
            if len(s.firstname + s.lastname + " " + ",") != 15:
                x = 15 - len(s.firstname + s.lastname + " " + ",")
                while x != 1:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")

            if s.a2marks == 0:
               print(" ")
            else:
               print(s.a2marks)

    elif component == "PR" or component == "pr" or component == "Pr" or component == "pR":
        print("Project grades " + "(" + str(Student.maxproject) + ")")
        for s in studentList:
            print(s.id, " ", end="")
            print(s.lastname + ",", end=" ")
            print(s.firstname, end=" ")
            if len(s.firstname + s.lastname + " " + ",") != 15:
                x = 15 - len(s.firstname + s.lastname + " " + ",")
                while x != 1:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")

            if s.projectmarks == 0:
                print(" ")
            else:
                print(s.projectmarks)

    elif component == "t1" or component == "T1":
        print("T1 grades " + "(" + str(Student.maxt1) + ")")
        for s in studentList:
            print(s.id, " ", end="")
            print(s.lastname + ",", end=" ")
            print(s.firstname, end=" ")
            if len(s.firstname + s.lastname + " " + ",") != 15:
                x = 15 - len(s.firstname + s.lastname + " " + ",")
                while x != 1:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")

            if s.t1marks == 0:
                print(" ")
            else:
                print(s.t1marks)

    elif component == "t2" or component == "T2":
        print("T2 grades " + "(" + str(Student.maxt2) + ")")
        for s in studentList:
            print(s.id, " ", end="")
            print(s.lastname + ",", end=" ")
            print(s.firstname, end=" ")
            if len(s.firstname + s.lastname + " " + ",") != 15:
                x = 15 - len(s.firstname + s.lastname + " " + ",")
                while x != 1:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")


            if s.t2marks == 0:
                print(" ")
            else:
                print(s.t2marks)


def averageComponent():
    component = input("Please indicate the component,you wish to see: ")

    while not component in validentries:
        print("Wrong Entry!!")
        component = input("Please indicate the component,you wish to see: ")
    print()
    if component == "a1" or component == "A1":
        x = 0
        for s in studentList:
            x = x + s.a1marks
        print("A1 Average: " + str(round(x / len(studentList), 2)) + "/" + str(s.maxa1))
    elif component == "a2" or component == "A2":
        x = 0
        for s in studentList:
            x = x + s.a2marks
        print("A2 Average: " + str(round(x / len(studentList), 2)) + "/" + str(s.maxa2))
    elif component == "PR" or component == "pr" or component == "Pr" or component == "pR":
        x = 0
        for s in studentList:
            x = x + s.projectmarks
        print("Project Average: " + str(round(x / len(studentList), 2)) + "/" + str(s.maxproject))
    elif component == "t1" or component == "T1":
        x = 0
        for s in studentList:
            x = x + s.t1marks
        print("T1 Average: " + str(round(x / len(studentList), 2)) + "/" + str(s.maxt1))
    elif component == "t2" or component == "T2":
        x = 0
        for s in studentList:
            x = x + s.t2marks
        print("T2 Average: " + str(round(x / len(studentList), 2)) + "/" + str(s.maxt2))


def sortID():
    return sorted(studentList, key=lambda s: s.id)

def sortLN():
    return sorted(studentList, key=lambda s: s.lastname)

def sortGR():
    return sorted(studentList, key=lambda s: s.numerictotal, reverse=True)


def printLastName():
    print()
    print("ID     " + "LN     " + "FN     "
          + "A1     " + "A2     " + "PR     " + "T1     " + "T2     "
          + "GR     " + "FL     ")
    lastNameList = sortLN()
    for s in lastNameList:
        s.numerictotal = s.calculateNumericTotal()
        s.assignLetterGrade()
        print(s.id, end="")
        print("  ", end="")

        print(s.lastname, end="")
        if len(s.lastname) != 6:
            x = 7 - len(s.lastname)
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        print(s.firstname, end="")
        if len(s.firstname) != 6:
            x = 7 - len(s.firstname)
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        if (s.a1marks == 0):
            print(" ", end="")
            if len(str(s.a1marks)) != 6:
                x = 7 - len(str(s.a1marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.a1marks, end="")
            if len(str(s.a1marks)) != 6:
                x = 7 - len(str(s.a1marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.a2marks == 0):
            print(" ", end="")
            if len(str(s.a2marks)) != 6:
                x = 7 - len(str(s.a2marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.a2marks, end="")
            if len(str(s.a2marks)) != 6:
                x = 7 - len(str(s.a2marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.projectmarks == 0):
            print(" ", end="")
            if len(str(s.projectmarks)) != 6:
                x = 7 - len(str(s.projectmarks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.projectmarks, end="")
            if len(str(s.projectmarks)) != 6:
                x = 7 - len(str(s.projectmarks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.t1marks == 0):
            print(" ", end="")
            if len(str(s.t1marks)) != 6:
                x = 7 - len(str(s.t1marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.t1marks, end="")
            if len(str(s.t1marks)) != 6:
                x = 7 - len(str(s.t1marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.t2marks == 0):
            print(" ", end="")
            if len(str(s.t2marks)) != 6:
                x = 7 - len(str(s.t2marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.t2marks, end="")
            if len(str(s.t2marks)) != 6:
                x = 7 - len(str(s.t2marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        print(s.numerictotal, end="")
        if len(str(s.numerictotal)) != 6:
            x = 7 - len(str(s.numerictotal))
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        print(s.grade, end="")

        print()


def printByGrade():
    print()
    print("ID     " + "LN     " + "FN     "
          + "A1     " + "A2     " + "PR     " + "T1     " + "T2     "
          + "GR     " + "FL     ")

    studentList = sortGR()

    for s in studentList:
        print(s.id, end="")
        print("  ", end="")

        print(s.lastname, end="")
        if len(s.lastname) != 6:
            x = 7 - len(s.lastname)
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        print(s.firstname, end="")
        if len(s.firstname) != 6:
            x = 7 - len(s.firstname)
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        if (s.a1marks == 0):
            print(" ", end="")
            if len(str(s.a1marks)) != 6:
                x = 7 - len(str(s.a1marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.a1marks, end="")
            if len(str(s.a1marks)) != 6:
                x = 7 - len(str(s.a1marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.a2marks == 0):
            print(" ", end="")
            if len(str(s.a2marks)) != 6:
                x = 7 - len(str(s.a2marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.a2marks, end="")
            if len(str(s.a2marks)) != 6:
                x = 7 - len(str(s.a2marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.projectmarks == 0):
            print(" ", end="")
            if len(str(s.projectmarks)) != 6:
                x = 7 - len(str(s.projectmarks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.projectmarks, end="")
            if len(str(s.projectmarks)) != 6:
                x = 7 - len(str(s.projectmarks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.t1marks == 0):
            print(" ", end="")
            if len(str(s.t1marks)) != 6:
                x = 7 - len(str(s.t1marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.t1marks, end="")
            if len(str(s.t1marks)) != 6:
                x = 7 - len(str(s.t1marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        if (s.t2marks == 0):
            print(" ", end="")
            if len(str(s.t2marks)) != 6:
                x = 7 - len(str(s.t2marks))
                while x != 0:
                    print(" ", end="")
                    x -= 1
            else:
                print(" ", end="")
        else:
            print(s.t2marks, end="")
            if len(str(s.t2marks)) != 6:
                x = 7 - len(str(s.t2marks))
            while x != 0:
                print(" ", end="")
                x -= 1

        print(s.numerictotal, end="")
        if len(str(s.numerictotal)) != 6:
            x = 7 - len(str(s.numerictotal))
            while x != 0:
                print(" ", end="")
                x -= 1
        else:
            print(" ", end="")

        print(s.grade, end="")

        print()

def inputfour():
    component = input("How do you want the list to sorted, LT or GR: ")
    Sortingentries = ["LT", "GR", "lt", "gr", "Lt", "lT", "Gr", "gR"]
    while not component in Sortingentries:
        print("Wrong entry!!")
        component = input("LT or GR: ")

    component = component.lower()
    if component == "lt":
        printLastName()
    elif component == "gr":
        printByGrade()