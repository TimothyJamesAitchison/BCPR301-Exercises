from view import View
from model import Model
from controller import Controller

control = Controller(View(), Model())
control.go()
