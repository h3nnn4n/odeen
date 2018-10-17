from de import DE
from problem_data import ProblemData
from config import Config


def test(self):
    print('%6.2f %6.2f' % (
            self.score,
            self.config.population.best_score
        )
    )


if __name__ == "__main__":

    config = Config()
    config.size = 100
    config.dimensions = 20
    config.set_function_evaluations_budget(5000)
    problem_data = ProblemData(pname='Rosenbrock', n_dimensions=config.dimensions)
    config.problem = problem_data

    de = DE(config=config)
    de.set_before_eval_callback(test)
    de.run()

    print(de.population.best_score)
