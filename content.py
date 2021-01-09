""" class Animal:
    def __init__ (self,name,type):
        self.name = name
        self.type = type
    
    def kingdom(self):
        print("We all belong to Animal Kingdom")

class Fish(Animal):
    def swim(self):
        print(f"{self.name} can swim")
        print(f'we are {self.type}')
        super().kingdom()

A = Fish('Nemo','aquatic')

A.swim() """

""" 
class Account:
    def __init__(self,bank,name,type):
        self.bank = bank
        self.name = name 
        self.type = type 

a = Account("XYZ_BANK","ABC_owner", 'type_A')

print(f"info of object(a) is:  {a.bank,a.name,a.type}")  """

""" class Account:
    def __init__(self,bank,name,type):
        self.bank = bank
        self._name = name 
        self.__type = type
        self.__balance = 1000

a = Account("XYZ_BANK","ABC_owner", 'type_A')

print(f"info of object(a) is:  {a.bank,a._name,a.__balance}")
 """

""" class Speed:
    def __init__(self,distance,time):
        self.ditance = distance
        self.time = time

    def speef_formula(self):
        speed = self.ditance // self.time
        return speed

    @classmethod
    def acceleration(cls,speed):
        return cls(x,y)

car1 = Speed.acceleration(2)
print(car1.acceleration()) """
    
# Python program to demonstrate 
# use of class method and static method. 
from datetime import date 

class Person: 
	def __init__(self, name, age): 
		self.name = name 
		self.age = age 
	
	# a class method to create a Person object by birth year. 
	@classmethod
	def fromBirthYear(cls, name, year): 
		return cls(name, date.today().year - year) 
	
	# a static method to check if a Person is adult or not. 
	@staticmethod
	def isAdult(age): 
		return age > 18

person1 = Person('XYZ', 21) 
person2 = Person.fromBirthYear('XYZ', 1990) 

print (person1.age) 
print (person2.age) 

# print the result 
print (Person.isAdult(22)) 


