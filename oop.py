class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello, my name is {self.name}")

class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp
        
        
JM = Player("JM", 1000)

class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team
        
        
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        print(super().__str__())
        return f"🐶 : {self.name}"
    def __getattribute__(self, name: str):
        print("thye want")
        
jia = Dog("jia")
print(jia)
print(dir(jia))