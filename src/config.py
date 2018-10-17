class Config:
    def __init__(self):
        self.de = None
        self.population = None
        self.problem = None
        self.size = 0
        self.dimensions = 0
        self.f = 0.5
        self.cr = 0.9
        self.function_evaluations_budget = 0
        self.evaluations_budget_left = self.function_evaluations_budget

    def function_evaluations_available(self, n=1):
        return self.evaluations_budget_left >= n

    def spend_function_evaluation(self, n=1):
        self.evaluations_budget_left -= n

    def set_function_evaluations_budget(self, n):
        self.function_evaluations_budget = n
        self.evaluations_budget_left = self.function_evaluations_budget
