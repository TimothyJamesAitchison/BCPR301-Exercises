class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def go(self):
        try:
            ceiling = int(self.view.get("Please enter the integer to sum to: >> "))
            total_sum = str(self.model.get_sum(ceiling))
            average = str(self.model.get_average(ceiling))
            self.view.say("The sum was " + total_sum)
            self.view.say("The average was " + average)
        except ValueError:
            self.view.say("That wasn't an integer!")
