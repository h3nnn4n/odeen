from de import DE
from problem_data import ProblemData


if __name__ == "__main__":
    problem_data = ProblemData(pname='Rosenbrock', n_dimensions=20)
    de = DE(size=100, dimensions=100, obj_function=problem_data)
