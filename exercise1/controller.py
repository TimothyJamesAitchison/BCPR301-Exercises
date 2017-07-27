class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def go(self):
        result = int(self.view.get("Please enter your mark "))
        self.view.say(self.model.check_mark(result))