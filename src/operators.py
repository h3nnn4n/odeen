from random import random


class Operators:
    def __init__(self, config):
        self.config = config

    def rand1bin(self, target, r1, r2, r3):
        for i in range(self.config.dimensions):
            if random() < self.config.de.get_cr():
                target.swap_variables[i] = (
                    r1.variables[i] + self.config.de.get_f() * (
                        r2.variables[i] -
                        r3.variables[i]
                    )
                )
