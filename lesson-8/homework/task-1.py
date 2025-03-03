class Animal():
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def walking(self):
        return f"{self.type} is walking"
    def sleeping(self):
        return f"{self.type} is sleeping"
    def eating(self):
        return f"{self.type} is eating"

class Activity(Animal):
    def __init__ (self, type, name):
        self.name = name
        super().__init__(type)
    def play(self):
        return f"{self.type} {self.name} is playing"
    def cleaning(self):
        return f"{self.type} {self.name} is cleaning by own"
class Zoo(Animal):
    def __init__ (self, type, name, is_sent):
        super().__init__(type, name)
        self.is_sent = is_sent
    def sent_to_zoo(self):
        if self.is_sent:
            return f"{self.type} {self.name} is sent to zoo"
        else:
            return f"{self.type} {self.name} is not sent to zoo"
class Condition(Animal):
    def __init__ (self, type, name, is_injured, is_sick):
        super().__init__(type, name)
        self.is_injured = is_injured
        self.is_sick = is_sick
    def injured(self):
        if self.is_injured:
            return f"{self.type} {self.name} is injured"
        else:
            return f"Everything is good with {self.type} {self.name}"
    def sick(self):
        if self.is_sick:
            return f"{self.type} {self.name} is sick"
        else: 
            return f"Everything is good with {self.type} {self.name}"

animal = Condition("Cat","Momiq", False, True)
print(animal.injured())