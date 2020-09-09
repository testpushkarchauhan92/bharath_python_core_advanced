class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hello")

def callTalk(obj):
    obj.talk();

# Polymorphism Based on Type of Argument Passed i.e. Duck or Human
d=Duck()
callTalk(d)

h=Human()
callTalk(h)
