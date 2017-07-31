class Calculator:
    @staticmethod
    def fib_calc(ceiling):
        assert ceiling >= 0
        fib_numbers = [1, 1]
        first_pivot = 0
        second_pivot = 1
        while len(fib_numbers) < ceiling:
            fib_numbers.append(fib_numbers[first_pivot] + fib_numbers[second_pivot])
            first_pivot += 1
            second_pivot += 1
        if ceiling == 0:
            return []
        elif ceiling == 1:
            return {1}
        else:
            return fib_numbers
