from algorithms.hillclimbing import hillclimbing
from algorithms.hillclimbingModified import hillclimbingModified
from excelExport import excelExport

from knapsack import knapsack
import numpy as np
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':
    maxRepetitions = 31
    maxIterations = 1000
    directory = 'C:\\Users\\\DanielT\\Documents\\9no' \
                '\\Metaheuristica\\mochila-binaria\\problems\\'
    myProblem = knapsack(directory + 'Knapsack1.txt')
    myProblem2 = knapsack(directory + 'Knapsack2.txt')
    myProblem3 = knapsack(directory + 'f2.txt')
    myProblem4 = knapsack(directory + 'f7.txt')
    myProblem5 = knapsack(directory + 'knapsack4.txt')

    myProblems = [myProblem, myProblem2, myProblem3, myProblem4, myProblem5]
    best = np.zeros(maxRepetitions, dtype=float)
    avgX = np.arange(0, maxIterations)
    myHC = hillclimbing(maxIterations)
    myHCM = hillclimbingModified(maxIterations)
    myAlgorithms = [myHC, myHCM]
    myLeg = []
    myData = []
    for problem in myProblems:
        for algorithm in myAlgorithms:
            avgY = np.arange(0, maxIterations)
            times = time.time()
            for i in range(maxRepetitions):
                np.random.seed(i)
                [x, y] = algorithm.evolve(problem)
                best[i] = algorithm.best.fitness
                avgY = avgY + y
            fin = time.time()
            times = fin - times
            avgY = avgY / maxRepetitions
            plt.plot(avgX, avgY)
            myLeg.append(str(algorithm))
            myData.append([problem.name, best.mean(), best.std(), best.max(), best.min(), times])
        # plotting
        plt.title("Convergence curve " + problem.name)
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.legend(myLeg)
        plt.show()
    myExport = excelExport(myData)
    myExport.evaluate()