from individual import Individual


class Population:
    def __init__(self, size, dimensions):
        self.size = size
        self.population = [
            Individual(dimensions=0)
            for _ in range(size)
        ]
