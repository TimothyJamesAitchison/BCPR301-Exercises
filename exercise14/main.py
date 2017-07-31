from view import View
from controller import Controller
from calculator import Calculator

controller = Controller(View, Calculator)
controller.go()
