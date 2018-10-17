import random
import types

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

    def step(self):
        self.population_generation_start()

        for individual in self.population:
            self.before_individual_eval()
            individual.step()
            self.after_individual_eval()

        self.selection()

        self.population_generation_end()

    def update_best(self, individual):
        if individual.score < self.best_score:
            self.best_score = individual.score
            self.best_index = individual.index

    def get_best(self):
        return self.population[self.best_index]

    def get_random(self):
        position = random.randint(0, len(self.population) - 1)
        return self.population[position]

    def selection(self):
        for individual in self.population:
            if individual.swap_score < individual.score:
                individual.swap()
                self.update_best(individual)

    def population_generation_start(self, *args, **kargs):
        pass

    def before_individual_eval(self, *args, **kargs):
        pass

    def after_individual_eval(self, *args, **kargs):
        pass

    def population_generation_end(self, *args, **kargs):
        pass

    def set_before_eval_callback(self, callback):
        for individual in self.population:
            individual.before_eval = types.MethodType(callback, individual)

    def set_after_eval_callback(self, callback):
        for individual in self.population:
            individual.after_eval = types.MethodType(callback, individual)

    def set_before_update_callback(self, callback):
        for individual in self.population:
            individual.before = types.MethodType(callback, individual)

    def set_after_update_callback(self, callback):
        for individual in self.population:
            individual.after_update = types.MethodType(callback, individual)
