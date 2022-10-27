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
