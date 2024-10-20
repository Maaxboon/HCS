# Define a new class Point
class Point():
    def __init__(self, input1, input2): # self represents the object in question
        # self.x = x # could also be self.x = input1
        # self.y = y # could also be self.y = input2

# What goes after self should also appear after the equal sign

        self.x = input1 # could also be self.x = input1
        self.y = input2 # could also be self.y = input2

# creates a point
p = Point(2, 8)
print(p.x)
print(p.y)
