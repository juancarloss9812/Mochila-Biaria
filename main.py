from algorithms.hillclimbing import hillclimbing
from algorithms.hillclimbingModified import hillclimbingModified

from knapsack import knapsack
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    maxRepetitions = 31
    maxIterations = 1000
    directory = 'C:\\Users\\\HP\\Desktop\\mochila-binaria'\
                '\\problems\\'
    myProblem = knapsack(directory + 'knapsack4.txt')
    print('Optimal Known = ', myProblem.OptimalKnown)

    best = np.zeros(maxRepetitions, dtype=float)
    best2 = np.zeros(maxRepetitions, dtype=float)

    avgX = np.arange(0, maxIterations)
    avgY = np.zeros(maxIterations, float)
    avgY1 = np.zeros(maxIterations, float)

    for i in range(maxRepetitions):
        np.random.seed(i)
        myHC = hillclimbing(myProblem, maxIterations)
        myHC1 = hillclimbingModified(myProblem, maxIterations)
        [x, y] = myHC.evolve()
        [x, y1] = myHC1.evolve()
        best[i] = myHC.best.fitness
        best2[i] = myHC1.best.fitness

        avgY = avgY + y
        avgY1 = avgY1 + y1

        # plotting
        '''
        plt.title("Convergence curve")
        plt.xlabel("Iteration")
        plt.ylabel("Fitness")
        plt.plot(x, y, color="red")
        plt.show()
        '''

    print('AVG = ', best.mean(), ' +/- ', best.std(), ' MAX = ', best.max(), ' MIN =  ', best.min())

    print('AVG1 = ', best2.mean(), ' +/- ', best2.std(), ' MAX = ', best2.max(), ' MIN =  ', best2.min())

    # plotting
    avgY = avgY / maxRepetitions
    avgY1 = avgY1 / maxRepetitions

    plt.title("Average convergence curve")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.plot(avgX, avgY, 'o', color="red")
    plt.plot(avgX, avgY1, 'o', color="blue")
    plt.show()

    fig1, ax1 = plt.subplots()
    ax1.set_title('Box Plot for best solutions')
    ax1.boxplot(best)
    plt.show()
