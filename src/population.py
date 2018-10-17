import random

from individual import Individual


class Population:
    def __init__(self, config=None):
        self.config = config

        self.population = [
            Individual(config=config, index=i)
            for i in range(self.config.size)
        ]

        self.best_score = float('inf')
        self.best_index = None

    def update(self):
        for individual in self.population:
            individual.update()

    def update_best(self, individual):
        if individual.score < self.best_score:
            self.best_score = individual.score
            self.best_index = individual.index

    def get_best(self):
        return (
            self.population[self.best_index],
            self.best_index
        )

    def get_random(self):
        position = random.randint(0, len(self.population))
        return (
            self.population[position],
            position
        )
