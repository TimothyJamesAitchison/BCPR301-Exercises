class Controller:
    def __init__(self, view, reverser):
        self.view = view
        self.reverser = reverser

    def go(self):
        the_string = self.view.get("Please enter the string to reverse: >>")
        self.view.say(self.reverser.reverse_string(the_string))