# import numpy as np


class Individual:
    def __init__(self, config, index):
        self.config = config

        self.variables = None
        self.swap_variables = None

        self.score = None
        self.swap_score = None

        self.index = index

        self.init()

    def init(self):
        self.random_init_variables()
        self.eval()

        self.swap_score = self.score

    def random_init_variables(self):
        self.variables = self.config.problem.initial_vector()
        self.swap_variables = self.variables.copy()

    def eval(self):
        if self.config.function_evaluations_available():
            self.score = self.config.problem.eval(self.variables)
            self.config.spend_function_evaluation()

        return self.score

    def eval_swap(self):
        if self.config.function_evaluations_available():
            self.swap_score = self.config.problem.eval(self.swap_variables)
            self.config.spend_function_evaluation()

        return self.score

    def step(self):
        self.before_update()
        self.apply_operator()
        self.before_eval()
        self.eval_swap()
        self.after_eval()
        self.after_update()

    def apply_operator(self):
        self.config.de.operators.rand1bin(
            self,
            self.config.population.get_random(),
            self.config.population.get_random(),
            self.config.population.get_random()
        )

    def swap(self):
        self.score = self.swap_score
        temp = self.variables
        self.variables = self.swap_variables
        self.swap_variables = temp

    def before_update(self, *args, **kargs):
        pass

    def before_eval(self, *args, **kargs):
        pass

    def after_eval(self, *args, **kargs):
        pass

    def after_update(self, *args, **kargs):
        pass
