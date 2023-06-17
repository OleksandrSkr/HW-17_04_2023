from Employees.Employee import Employee

class Developer (Employee):
    def __init__(self, name, age, unemployed, skills, experience):
        super().__init__(name, age, unemployed)
        self._skills = skills
        self._experience = experience

    def Firing (self, unemployed):
        self._unemployed = unemployed
        print("Dev", Developer.__dict__)
        

Developer = Developer("Bob", 25, True, "Python", "5 years")
      
#print("Dev", Developer.__dict__)


#from Employees.QA import QA

#class Developer (QA):
#    def __init__(self, name, age, unemployed, skills, experience):
#        super().__init__(name, age, unemployed, skills)
#        self._experience = experience

#    def Firing (self, unemployed):
#        self._unemployed = unemployed
#        print("Dev", Developer.__dict__)
        

#Developer = Developer("Bob", 25, True, "Python", "5 years")
      
#print("Dev", Developer.__dict__)

#Developer.Firing(False)


