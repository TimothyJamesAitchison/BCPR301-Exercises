class Model:

    def harmonic_sum_forwards(self, ceiling):
        result = 0.0
        for denominator in range(1, ceiling+1):
            result += 1/denominator
        return result

    def harmonic_sum_backwards(self, ceiling):
        result = 0.0
        for denominator in range(ceiling, 0, -1):
            result += 1/denominator
        return result
