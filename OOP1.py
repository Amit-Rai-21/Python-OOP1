'''OOP in Python'''
'''
To map with real world scenarions,we started using objects in code
This is called object oriented programming.


Class is bluprint for creating objects.
 
#creating class
class Student:
     name="RAM "

     #creating object(instance)
     s1=student()
     print(s1.name)







'''
# class Student:
#     name="RAm"
# s1=Student()
# print(s1.name)
#-----------------------------------------
# class Car:
#     color="blue"
#     brand="mercidies"

# car1=Car()
# print(car1.color)
# print(car1.brand)


''' _ _init_ _Function
Constructor
All classes have a function called _init_(), which is always executed whent the class is being initiated

#creating class
  class student:
    def _ _init_ _(self,fullname):
         self.name=fullname



#creating object
s1=student("karan")
print(S1.name)

note:The self parameter is a reference to the current instance of the class and is used to access the variables
     that belongs to the class




DEfault constructor:
def __init__(self) -> None:
        pass






'''
#Example of parameterized constructor
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding a new data")
        
s1=Student("Amit",88)
print(s1.name,s1.marks)
s2=Student("Ram",99)
print(s2.name,s2.marks)  '''


#CLASS AND INSTANCE ATTRIBUTES
''' 
Instance attributes-->Changable or which can be different for example in above program sutuden name and marks are the example os instance atribute
for instance attributes we use self._____ like self.marks,self.name etc..

Class attribute---->having same atribute or data,(common),we don't create object for same data repeatdetly ,instead of doing that we store single time in memory

class Student:
    college_name="xyz"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding a new data")
        
s1=Student("Amit",88)
print(s1.name,s1.marks)
s2=Student("Ram",99)
print(s2.name,s2.marks)
print(Student.College_name) pr s2.Collegename




METHODS
 Methods are functions that belong to objects.
 #creating class
 class Student:
     def_ _init_ _(self,fullname):
        self.name=fullname
     def hello(self):
        print("hello",self.name)



#creating object
s1=Student("Ram")
s1.hello()

class Student:
  def __init__(self,name):
    self.name=name

  def display(self):
    print("Hello student",self.name)

s1=Student("Amit")
s1.display() 



'''
# PRACTICE QUESTION
#! Crate student class that takes name and marks of 3 subjects as arguments 
# in constructor .Then create a methon to print the average

'''class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def Avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        Avg=sum/3
        print("Average is",Avg)
s1=student("Amit",[78,88,44]) 
print(s1.name,s1.marks)
s1.Avg()     '''  

'''
STATIC METHOD

methods that does not use the self parameter (work at class level)

   class student:
       @staticmethod   #decorator
       def college()
           print("ABC College")

           

  " Decorator allow us to wrap another function in order to extend
  the behviour of the wrapped function without permanently modifiying it."


  IMPORTANT

   #Abstraction
   Hiding the implementation details of a class and only showing the essential features to the user


   #Encapsulation
   Wrapping data and functions into a single unit (object)

'''

 #1Create account class with 2 attributes -balance and account.no
 # Create methods for debit,credit and printing the balance

''''class Account:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno

    def disp(self):
        sum=10000
        n=(input("Do you want to take or give money"))
        if n=="take":
            print(self.balance,"is debited from acc.no",self.accountno)
            sum+=self.balance
        else:
            print(self.balance,"is creditd from acc.no",self.accountno)
            sum-=self.balance
             
        print("Your current balance is",sum)

s1=Account(5000,98274974398) 
s1.disp() '''

 
'''class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance+=amount
        print(amount ,"was debited") 
        print("Total balance=",self.get_balance())

    def credit(self,amount):
        self.balance-=amount
        print(amount,"was credited")
        print("Total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
 
acc1=Account(1000,12345)
print(acc1.debit(1000))
print(acc1.credit(500))       '''


