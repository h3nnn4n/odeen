from de import DE
from problem_data import ProblemData
from config import Config


if __name__ == "__main__":

    config = Config()
    config.size = 100
    config.dimensions = 20
    config.set_function_evaluations_budget(5000)
    problem_data = ProblemData(pname='Rosenbrock', n_dimensions=config.dimensions)
    config.problem = problem_data

    de = DE(config=config)
    de.run()
