from model import Model
from view import View
from controller import Controller

# This is for dependency injection example: First make the View and Model...
view = View()
model = Model()

# Then inject them into the Controller
controller = Controller(view, model)

# And run the program
controller.go()
