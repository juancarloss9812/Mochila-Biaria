from solution import solution
from knapsack import knapsack
import numpy as np


class hillclimbingModified:
    def __init__(self, problem: knapsack, maxIter: int):
        self.best = solution(problem)
        self.problem = problem
        self.maxIterations = maxIter

    def evolve(self):
        x = np.arange(0, self.maxIterations)
        y = np.zeros(self.maxIterations, float)
        self.best.randomInitializationOptima()
        for iteration in range(self.maxIterations):
            copyOfBest = solution(self.best.problem)
            copyOfBest.from_solution(self.best)
            copyOfBest.tweakNew()
            if copyOfBest.fitness > self.best.fitness:
                self.best.from_solution(copyOfBest)
            y[iteration] = self.best.fitness
        return [x, y]
