from Employee import Employee

class QA (Employee):
    def __init__(self, name, age, unemployed : False ):
        super().__init__(name, age)
        self._unemployed = unemployed
    