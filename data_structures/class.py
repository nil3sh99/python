# This code shows class and objects in python

# Create a class called "Robot" -- featuring = name, color, weight
# Create two objects of this class -- o1, o2 which utilizes the features from the class

# A much better way to call the arguments and assume their default value is by using the constructors


# self keyword in python is like "this" in java, as it refers to the object which is using the class
class Robot: 
    # an additional "self" has to be added as the argument in every python function/method which are defined inside the class
    def introduce_self(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
    
    # constructor defined below
    # good practice is to name the arguments as same as the self.x    
    def __init__(self, givenName, givenColor, givenWeight):
        self.name = givenName
        self.color = givenColor
        self.weight = givenWeight

# create a new object with class Robot
# r1 = Robot()
# r1.name = "Nilesh"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Nileshv2"
# r2.color = "blue"
# r2.weight = 40

# r1.introduce_self()
# # when we write the code above, it basically goes to the introduce_self(self) function and then references "r1" as self, so 
# # self.name == r1.name

# r2.introduce_self()

#######################
# CONSTRUCTOR
#######################

r3 = Robot("tom", "blue", 30)
r3.introduce_self()

r4 = Robot("nilesh", "red", 40)
r4.introduce_self()




        
        