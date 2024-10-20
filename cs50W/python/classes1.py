# Defines a class Bed
class Bed():
    # this is a function called init that creates a bed by storing beds inside of the property called a and a property called f. Such that later I can create a bed that calls the init function implicitly
    def __init__(self, bed1, bed2):
        self.a = bed1
        self.f = bed2

# creates a bed
b = Bed("decker", "cot")

# Accesses the data inside the point
print(b.a)
print(b.f)