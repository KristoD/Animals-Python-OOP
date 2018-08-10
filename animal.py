class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 50

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "Name: " + str(self.name)
        print "Health: " + str(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am " + self.name + ", the Dragon"

goat = Animal("Henry")
print goat.walk().walk().walk().run().run().display_health()

doggo = Dog("MuCh w0W")
print doggo.walk().walk().walk().run().run().pet().display_health()

draggo = Dragon("Elvarg")
print draggo.walk().run().fly().display_health()

