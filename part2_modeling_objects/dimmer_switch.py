'''

Dimmer switch class

Instance Variables:
    The switch state (on or off);
    Brightness level (0 to 10);

Methods:
    def TurnOn(self);
    def TurnOff(self);
    def raiseLevel(self);
    def lowerLevel(self);
    def show(self) (for debugging);

'''


class DimmerSwitch:
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    # Extra method for debugging
    def show(self):
        print(f"Switch is on? {self.switchIsOn}")
        print(f"Brightness is: {self.brightness}")


# Main code
oDimmer1 = DimmerSwitch()
oDimmer2 = DimmerSwitch()

print(type(oDimmer1))

oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

oDimmer1.showState()
oDimmer2.showState()
