from Employees.Employee import Employee

class QA (Employee):
    def __init__(self, name, age, unemployed, skills):
        super().__init__(name, age, unemployed)
        self._skills = skills
            
    def Firing (self, unemployed):
        self._unemployed = unemployed
        print("QA", QA.__dict__)
        

QA = QA("Nik", 42, True, "automatizer")
#QA = ("Nik", 42, True, "automatizer")     

#print("QA", QA.__dict__)
#print("QA", QA)
#QA.Firing(False)
