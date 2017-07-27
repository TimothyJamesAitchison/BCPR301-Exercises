class Model:

    def print_word(self, number):
        return self.print_word_dictionary(number)

    # This is a bad solution
    def print_word_if(self, number):
        if number == 1:
            return "ONE"
        elif number == 2:
            return "TWO"
        elif number == 3:
            return "THREE"
        elif number == 4:
            return "FOUR"
        elif number == 5:
            return "FIVE"
        elif number == 6:
            return "SIX"
        elif number == 7:
            return "SEVEN"
        elif number == 8:
            return "EIGHT"
        elif number == 9:
            return "NINE"
        else:
            return "OTHER"

    # Python does not have switch-case

    # This is a better solution
    def print_word_dictionary(self, number):
       return {
           1: "ONE",
           2: "TWO",
           3: "THREE",
           4: "FOUR",
           5: "FIVE",
           6: "SIX",
           7: "SEVEN",
           8: "EIGHT",
           9: "NINE",
       }.get(number, "OTHER")