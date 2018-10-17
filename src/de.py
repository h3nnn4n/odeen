from population import Population


class DE:
    def __init__(self, size, dimensions, obj_function):
        self.size = size
        self.dimensions = dimensions
        self.population = Population(
            size=size,
            dimensions=dimensions
        )
