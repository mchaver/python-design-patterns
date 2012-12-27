'''
An object is used to represent and encapsulate all the information needed to call a
method at a later time. 

Client instantiates the command object and provides the information to call the method later
Invoker decides when the method should be called
Receiver is an instance of the class that contains the method's code
'''
#http://en.wikipedia.org/wiki/Command_pattern#Python

class Switch(object):
    """INVOKER"""
    def __init__(self, flip_up_cmd, flip_down_cmd):
        self.flip_up = flip_up_cmd
        self.flip_down = flip_down_cmd
        
class Light(object):
    """RECEIVER"""
    def turn_on(self):
        print "The light is on"
    def turn_off(self):
        print "The light is off"

class LightSwitch(object):
    """CLIENT"""
    def __init__(self):
        lamp = Light()
        self._switch = Switch(lamp.turn_on, lamp.turn_off)
    
    def switch(self, cmd):
        if cmd == "ON":
            self._switch.flip_up()
        elif cmd == "OFF":
            self._switch.flip_down()
        else:
            print 'Only accepts "ON" or "OFF"'

light_switch = LightSwitch()
light_switch.switch("ON")
light_switch.switch("OFF")
light_switch.switch("*****")