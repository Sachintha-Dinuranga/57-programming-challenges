class Madlibs():
    """Three different madlib methods"""
    def __init__(self, noun, verb, adjective, verb2):
        self.noun = noun
        self.verb = verb
        self.adjective = adjective
        self.verb2 = verb2

    def first_method(self):
        madlib = f"Learning to {self.verb} is very {self.adjective}. {self.noun} can be difficult, so you need to {self.verb2} hard."
        print(madlib)
    
    def second_method(self):
        madlib2 = ("Learning to " + self.verb)
        print(madlib2)

    def third_method(self):
        madlib3 = "Learning to {} is very {}. {} can be difficult, so you need to {} hard.".format(self.verb,self.adjective,self.noun,self.verb2)
        print(madlib3)
