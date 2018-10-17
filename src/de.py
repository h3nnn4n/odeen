from population import Population
from operators import Operators
import types


class DE:
    def __init__(self, config=None):
        self.config = config
        self.config.de = self

        self.size = self.config.size
        self.dimensions = self.config.dimensions

        self.population = Population(
            config=config
        )

        self.operators = Operators(config=config)

        self.config.population = self.population

    def run(self):
        self.optimize_start()

        while self.step():
            pass

        self.optimize_end()

    def step(self):
        self.generation_start()

        if not self.config.function_evaluations_available():
            return False

        self.population.step()

        self.generation_start()

        return True

    def get_f(self):
        return self.config.f

    def get_cr(self):
        return self.config.cr

    def optimize_start(self, *args, **kargs):
        pass

    def generation_start(self, *args, **kargs):
        pass

    def generation_end(self, *args, **kargs):
        pass

    def optimize_end(self, *args, **kargs):
        pass

    def set_before_eval_callback(self, callback):
        self.population.set_before_eval_callback(callback)

    def set_after_eval_callback(self, callback):
        self.population.set_after_eval_callback(callback)

    def set_before_update_callback(self, callback):
        self.population.set_before_update_callback(callback)

    def set_after_update_callback(self, callback):
        self.population.set_after_update_callback(callback)

    def set_optimize_start(self, callback):
        self.optimize_start = types.MethodType(callback, self)

    def set_optimize_end(self, callback):
        self.optimize_end = types.MethodType(callback, self)

    def set_generation_start(self, callback):
        self.generation_start = types.MethodType(callback, self)

    def set_generation_end(self, callback):
        self.generation_end = types.MethodType(callback, self)
