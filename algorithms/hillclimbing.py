from solution import solution
from knapsack import knapsack
import numpy as np


class hillclimbing:
    def __init__(self, problem: knapsack, maxIter: int):
        self.best = solution(problem)
        self.problem = problem
        self.maxIterations = maxIter

    def evolve(self):
        x = np.arange(0, self.maxIterations)
        y = np.zeros(self.maxIterations, float)
        self.best.randomInitialization()
        for iteration in range(self.maxIterations):
            copyOfBest = solution(self.best.problem)
            copyOfBest.from_solution(self.best)
            copyOfBest.tweak()
            if copyOfBest.fitness > self.best.fitness:
                self.best.from_solution(copyOfBest)
            y[iteration] = self.best.fitness
        return [x, y]
