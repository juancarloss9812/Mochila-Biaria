import numpy as np


class knapsack:
    def __init__(self, filename):
        file1 = open(filename, 'r')
        lines = file1.readlines()

        firstline = lines[0].split(' ')
        self.size = int(firstline[0])
        self.capacity = float(firstline[1].strip())
        self.profits = np.zeros(self.size, dtype=float)
        self.weights = np.zeros(self.size, dtype=float)

        positionLine = 1
        for i in range(0, self.size):
            line = lines[positionLine].split(' ')
            self.profits[positionLine - 1] = float(line[0])
            self.weights[positionLine - 1] = float(line[1])
            positionLine = positionLine + 1
        self.OptimalKnown = float(lines[positionLine])

    def evaluate(self, cells):
        weight = (cells * self.weights).sum()
        fitness = -1
        if weight <= self.capacity:
            fitness = (cells * self.profits).sum()
        return fitness, weight
