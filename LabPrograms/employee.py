class Emp:
    def __init__(self):
        self.name = ""
        self.empID = ""
        self.dept = ""
        self.salary = 0

    def empGetDetails(self):
        self.name = input("Enter name:")
        self.empID = input("Enter empID:")
        self.dept = input("Enter department:")
        self.salary = int(input("entry salary:"))

    def empShow(self):
        print("Employee Details")
        print("Name : ", self.name)
        print("ID : ", self.empID)
        print("Dept : ", self.dept)
        print("Salary : ", self.salary)

    def updateSalary(self):
        newSalary = int(input("Enter new salary.."))
        self.salary = newSalary


e1 = Emp()
e1.empGetDetails()
e1.empShow()
e1.updateSalary()