from controller import Controller
from model import Model
from view import View

model = Model()
view = View()
controller = Controller(view, model)
controller.go()
