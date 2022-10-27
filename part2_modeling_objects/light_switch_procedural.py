'''

To model a real-world object in code, we need to decide what data will
represent that object's attributes and what operations it can perform. These
two concepts are often referred to as an object's state and behavior,
respectively: the state is the data that the object remembers, and the
behaviors are the actions that the object can do.

State and Behavior: Light Switch Example
A software model of a standard two-position light switch written in procedural
Python. This is a trivial example, but it will demonstrate state and behavior

'''

from glob import glob


def turnOn():
    global switchIsOn

    # Turn the light on
    switchIsOn = True


def turnOff():
    global switchIsOn

    # Turn the light off
    switchIsOn = False


switchIsOn = False

print(switchIsOn)
turnOn
print(switchIsOn)
turnOff
print(switchIsOn)
turnOn
print(switchIsOn)

'''

The switch can only be in one of two positions: on or off. To model
the state, we only need a single Boolean variable. We name this variable
switchIsOn and we say that True means on and False indicates off. When
the switch comes from the factory, it is in the off position, so we initially
set switchIsOn to False.
Next, we look at the behavior. This switch can only perform two actions:
“turn on” and “turn off.” We therefore build two functions, turnOn() 1 and
turnOff(), which set the value of the single Boolean variable to True and
False, respectively.
because we've used a global variable to represent the state
(in this case, the variable switchIsOn), this code will only work for a single
light switch, but one of the main goals of writing functions is to make
reusable code.

'''
