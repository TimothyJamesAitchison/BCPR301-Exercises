class Controller:

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def go(self):
        harmonic_forwards = self.model.harmonic_sum_forwards(50000)
        harmonic_backwards = self.model.harmonic_sum_backwards(50000)
        harmonic_difference = harmonic_backwards - harmonic_forwards
        self.view.say("Forwards got a result " + str(harmonic_forwards))
        self.view.say("Backwards got a result " + str(harmonic_backwards))
        self.view.say("The difference was " + str(harmonic_difference))
