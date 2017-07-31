from controller import Controller
from view import View
from reverser import Reverser

controller = Controller(View, Reverser)
controller.go()