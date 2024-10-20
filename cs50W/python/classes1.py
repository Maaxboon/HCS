# Defines a class Bed
class Bed():
    def __init__(self, bed1, bed2):
        self.a = bed1
        self.f = bed2

# creates a bed
b = Bed("decker", "cot")
print(b.a)
print(b.f)