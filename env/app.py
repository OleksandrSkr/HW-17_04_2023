
from Employees.QA import QA
from Employees.Developer import Developer
import random

rand_int = random.randint(1, 2)
print(rand_int)
if rand_int == 1:
    Developer.Firing(False)
elif rand_int == 2:
    QA.Firing(False)
    
