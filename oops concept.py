#creating class
class Person:
    name = "Vikrant"
    age = 22
    occupation = "lawyer"

#a.name = "aryan"
#a.age = 22
#a.occupation="accountant"
    def info(self):
        print(f"{self.name} is a {self.occupation}")    
a = Person()
b = Person()
c = Person()
a.info()
#new object
b.name = "DahiyaBharadwaj"
b.occupation = "gangster"
b.age = 22
b.info()
#one more object
c.name = "Pushpender"
c.age = 24
c.occupation = "cafe owner"
c.info()