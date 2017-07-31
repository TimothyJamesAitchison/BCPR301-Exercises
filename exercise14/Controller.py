class Controller:
    def __init__(self, view, calc):
        self.view = view
        self.calc = calc

    def go(self):
        try:
            ceiling = int(self.view.get("How many Fibonacci numbers?"))
            fib_numbers = self.calc.fib_calc(ceiling)
            for number in fib_numbers:
                self.view.say(number)
        except ValueError:
            self.view.say("That wasn't an integer!")
