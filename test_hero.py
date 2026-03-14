class Hero:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.lives = 3

    def hi(self):
        print("Привет, я " + self.name)

hero1 = Hero("Вася")

hero1.hi()


