import subprocess
students = []
features = []

def anyKeyContinue():
    input("Press Any key to continue!")
    subprocess.call("cls", shell=True)
    menu()


def listAll():
    for student in students:
        print(student)

def add():
    name = input("Enter Student Name (use , to add multiple names):")
    cnt = 0
    if "," in name:
        names = name.split(",")
        for nm in names:
            cnt += 1
            students.append(nm)
    else:
        cnt += 1
        students.append(name)
    print(str(cnt)+" Students Added!")

def remove():
    listAll()
    name = input("Enter Name To Remove (use , to add multiple names):")
    cnt = 0
    if "," in name:
        names = name.split(",")
        for nm in names:
            if nm in names:
                cnt += 1
                students.remove(nm)
        print(str(cnt) + " Students Removed!")
    else:
        if name in students:
            students.remove(name)
            print(name+" Removed!")
        else:
            print("Student Not Found!")

def edit():
    listAll()
    name = input("Enter Name To Edit:")
    cnt = -1
    for student in students:
        cnt += 1
        if name == student:
            students[cnt] = input("Enter New Name For '"+student+"':")
            print("Saved '"+student+"' as '"+students[cnt]+"'!")
    if cnt < 0:
        print("No Student Found with given name!")


def search():
    name = input("Enter Name To Search:")
    for student in students:
        if name in student:
            print(student)


def menu():
    subprocess.call("cls", shell=True)
    print("Welcome To Students Management System")
    print("Press 1 to List All Students")
    print("Press 2 to add Student")
    print("Press 3 to Remove Student")
    print("Press 4 to Edit Student")
    print("Press 5 to Search Student")
    menuInp = input("Enter Your Choice:")
    validRanges = ["1","2","3","4","5"]
    if menuInp in validRanges:
        if menuInp == "1":
            listAll()
        elif menuInp == "2":
            add()
        elif menuInp == "3":
            remove()
        elif menuInp == "4":
            edit()
        elif menuInp == "5":
            search()
        anyKeyContinue()
    else:
        print("Invalid Input!")
        anyKeyContinue()


menu()