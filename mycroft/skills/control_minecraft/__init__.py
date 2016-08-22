import time
#from pykeyboard import PyKeyboard
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill

__author__ = 'bsays'

class ControlMinecraftSkill(MycroftSkill):
    
    def __init__(self):
        super(ControlMinecraftSkill, self).__init__(name="ControlMinecraftSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        move_minecraft_intent = IntentBuilder("MoveMinecraftIntent").require("MoveKeyword").build()
        self.register_intent(move_minecraft_intent, self.handle_move_minecraft_intent)

    def handle_move_minecraft_intent(self, message):
        self.speak_dialog("move.feedback")
        #k = PyKeyboard()        
        #k.tap_key('R')

    def stop(self):
        pass

def create_skill():
    return ControlMinecraftSkill()
