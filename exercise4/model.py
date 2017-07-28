class Model:

    def get_average(self, ceiling):
        return self.get_sum(ceiling) / ceiling

    def get_sum(self, ceiling):
        total_sum = 0
        for number in range(1, ceiling+1):
            total_sum += number
        return total_sum
