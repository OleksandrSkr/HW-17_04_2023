from Employees.QA import QA

class Developer (QA):
    def __init__(self, name, age, unemployed : False ):
        super().__init__(name, age, unemployed: False)

    def Firing (self):
        unemployed = True
    
    