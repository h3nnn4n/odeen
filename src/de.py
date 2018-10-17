from population import Population


class DE:
    def __init__(self, config=None):
        self.config = config
        self.config.de = self

        self.size = self.config.size
        self.dimensions = self.config.dimensions

        self.population = Population(
            config=config
        )

        self.config.population = self.population

    def run(self):
        if not self.config.function_evaluations_available():
            return False

        self.population.update()

        return True
