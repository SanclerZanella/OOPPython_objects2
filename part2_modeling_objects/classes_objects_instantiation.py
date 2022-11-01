'''

Code that defines what an object will remember (its data or state) and the
things that it will be able to do (its functions or behavior).

Class:
    Code that defines what an object will remember (its data or state) and
    the things that it will be able to do (its functions or behavior).

Class syntax:

    class <ClassName>():
        def __init__(self, <optionalParam1>, <optionalParam2>, ...):
            # Constructor method
            # any initialization code here, like:

            self.optionalParam1 = optionalParam1
            self.optionalParam2 = optionalParam2

        def <methodName1>(self, <optionalMethodP1>, <optionalMethodP2>)
            # Body of the method

        # ... more methods

        def <methodNameN>(self, <optionalMethodP1>, <optionalMethodP2>)
            # Body of the method


Instantiation:
    The process of creating an object from a class.
    e.g.:

        <object> = <ClassName>(<optional arguments>)
        oLightSwitch = LightSwitch()

Method:
    A function defined inside a class. A method always has at least one
    parameter, which is usually named self.
    After creating an object from a class, to call a method of the object,
    you use the generic syntax:

        <object>.<methodName>(<any arguments>)
        oLightSwitch.show()


Instance variable:
    In a method, any variable whose name begins, by convention, with
    the prefix self. (for example, self.x). Instance variables have
    object scope.


'''


class MyClass:
    '''
    Example of method and instance variable
    '''
    def __init__(self):
        self.count = 0  # Create self.count and set it to 0

    def increment(self):
        self.count = self.count + 1  # Increment the variable


class LightSwitch:
    '''
        OOP light switch
    '''

    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # Turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # Turn the switch off
        self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)


# An instance of the class LightSwitch
# Instantiation is the process of creating an object from a class.
oLightSwitch = LightSwitch()  # create a LightSwitch object

# Calls to methods
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()
oLightSwitch.turnOff()
oLightSwitch.show()
oLightSwitch.turnOn()
oLightSwitch.show()

'''
One of the key features of OOP is that you can instantiate as many objects
as you want from a single class.
So, if you want two light switch objects, or three, or more, you can just
create additional objects from the LightSwitch class like so:
'''

oLightSwitch1 = LightSwitch()  # create a LightSwitch object
oLightSwitch2 = LightSwitch()  # create another LightSwitch object

'''
The important point here is that each object that you create from a
class maintains its own version of the data.
Any changes you make to the data of one object will not affect the data
of another object.
'''

oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()  # Turn switch 1 on
# Switch 2 should be off at start, but this makes it clearer
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()

# It might not surprise you that all built-in data types in Python are
# implemented as classes. Here is a simple example:

myString = 'abcde'
print(type(myString))  # Output: <class 'str'>

'''
We assign a string value to a variable. When we call the type() function
and print the results, we see that we have an instance of the str string class.
The str class gives us a number of methods we can call with strings, including
myString.upper(), myString.lower(), myString.strip(), and so on.
Any other pythpn data type work in the same way.
'''

myList = [10, 20, 30, 40]
print(type(myList))  # <class 'list'>

'''
To summarize the definition of an object:
    object - Data, plus code that acts on that data, over time

A class defines what an object will look like when you instantiate one.
An object is a set of instance variables and the code of the methods in the
class from which the object was instantiated. Any number of objects can
be instantiated from a class, and each has its own set of instance variables.
When you call a method of an object, the method runs and uses the set of
instance variables in that object.
'''
