# import numpy as np


class Individual:
    def __init__(self, config, index):
        self.config = config

        self.variables = None

        self.score = None

        self.index = index

        self.init()

    def init(self):
        self.random_init_variables()
        self.eval()

    def random_init_variables(self):
        self.variables = self.config.problem.initial_vector()

    def eval(self):
        if self.config.function_evaluations_available():
            self.score = self.config.problem.eval(self.variables)
            self.config.spend_function_evaluation()

        return self.score

    def update(self):
        self.before_update()

        self.before_eval()

        self.eval()

        self.after_eval()

        self.config.population.update_best(self)

        self.after_update()

    def before_update(self, *args, **kargs):
        pass

    def before_eval(self, *args, **kargs):
        pass

    def after_eval(self, *args, **kargs):
        pass

    def after_update(self, *args, **kargs):
        pass
