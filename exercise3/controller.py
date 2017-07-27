class Controller:

    def __init__(self, view, model):
        # self. is like this. from java/javascript
        self.model = model
        self.view = view

    def go(self):
        # Try-Catch block is used as when we cast to an int it will throw a
        # ValueError if the user entered something what isn't an int
        try:
            # We cast the user input to int because it will be string when it comes in.
            number = int(self.view.get("Please enter an integer >> "))
            self.view.say(self.model.print_word(number))
        except ValueError:
            self.view.say("That wasn't an integer!")