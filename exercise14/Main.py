from View import View
from Controller import Controller
from Calculator import Calculator

controller = Controller(View, Calculator)
controller.go()
