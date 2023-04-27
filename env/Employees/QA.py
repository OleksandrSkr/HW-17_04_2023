from Employee import Employee
import random
QAs = []

class QA (Employee):
    def __init__(self, name, age, unemployed):
        super().__init__(name, age)
        self._unemployed = unemployed
#        unemployed = False
    def saveQA (self, name, age, unemployed):
        QAs.append(QA)

#    def Firing (self):
#        n = len(QAs)
#        i = random.randint(1, n)
#        QAs[i].unemployed = True

QA.saveQA("Bob", "21", False)
print(QAs)
        

#Bob = QA("Bob", "21", unemployed : False)