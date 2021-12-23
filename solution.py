import numpy as np
from knapsack import knapsack


class solution:
    def __init__(self, p: knapsack):
        self.problem = p
        self.cells = np.zeros(self.problem.size, int)
        self.fitness = 0.0
        self.weight = 0.0

    def from_solution(self, origin):
        self.problem = origin.problem
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.weight = origin.weight

    def randomInitialization(self):
        positions = np.random.choice(self.problem.size, self.problem.size, replace=False)
        weight = 0
        for p in positions:
            if weight + self.problem.weights[p] < self.problem.capacity:
                self.cells[p] = 1
                weight = weight + self.problem.weights[p]
        self.fitness, self.weight = self.problem.evaluate(self.cells)

    def randomInitializationOptima(self):

        denside = (self.problem.profits/self.problem.weights)
        densideAux = np.copy(denside)
        densideAux[::-1].sort()
        positions = self.__getpositions(densideAux,denside)
        ##se ordenan de mayor a menor
        weight = 0
        for p in self.problem.profits:
            #saca el aleatorio
            if densideAux.size >= 3:
                position = np.random.choice(3, 1, replace=False)
                index = positions[position[0]]
                if weight + self.problem.weights[index] < self.problem.capacity:
                    self.cells[index] = 1
                    weight = weight + self.problem.weights[index]
                densideAux = np.delete(densideAux, position)
                positions = np.delete(positions, position)

        self.fitness, self.weight = self.problem.evaluate(self.cells)

    def __getpositions(self,desidadAux,desities):
        positions = []
        index = np.where(desities == desidadAux[0])[0]
        count = index.size
        count = count - 1
        for d in desidadAux:
            if count== 0 :
                index = np.where(desities == d)[0]
                count = index.size
                count = count - 1
                if(count == 0):
                    positions.append(index[0])
                else:
                    count = count + 1
                    positions.append(index[(count - 1)])
                    count = count - 1
            else:
                positions.append(index[(count-1)])
                count=count-1

        return positions



    def tweak(self):
        selectedPositions = np.where(self.cells == 1)[0]
        unselectedPositions = np.where(self.cells == 0)[0]
        x = np.random.randint(len(selectedPositions), size=1)
        elementToRemove = selectedPositions[x[0]]
        self.cells[elementToRemove] = 0
        self.weight = self.weight - self.problem.weights[elementToRemove]
        self.fitness = self.fitness - self.problem.profits[elementToRemove]

        empty = self.problem.capacity - self.weight


        while empty > 0 and len(unselectedPositions) > 0:
            fitUnselected = np.array([unselectedPositions, self.problem.weights[unselectedPositions]])
            fitUnselected = fitUnselected[:, np.where(fitUnselected[1, :] < empty)][0]
            unselectedPositions = np.copy(fitUnselected[0])

            if len(fitUnselected[0]) == 0:
                break
            #evaluar por el precio entre los mas altos.
            elementToAdd = int(fitUnselected[0][np.random.randint(len(fitUnselected[0]))])
            self.cells[elementToAdd] = 1
            self.weight = self.weight + self.problem.weights[elementToAdd]
            self.fitness = self.fitness + self.problem.profits[elementToAdd]
            unselectedPositions = np.array(unselectedPositions[np.where(unselectedPositions != elementToAdd)],
                                           dtype=int)
            empty = self.problem.capacity - self.weight

    def tweakNew(self):

        denside = (self.problem.profits / self.problem.weights)
        densideAux = np.copy(denside)
        densideAux[::-1].sort()
        positions = self.__getpositions(densideAux, denside)

        selectedPositions = np.where(self.cells == 1)[0]

        x = np.random.randint(len(selectedPositions), size=1)
        elementToRemove = selectedPositions[x[0]]
        self.cells[elementToRemove] = 0
        self.weight = self.weight - self.problem.weights[elementToRemove]
        self.fitness = self.fitness - self.problem.profits[elementToRemove]
        full=0
        limit = np.where(positions == elementToRemove)[0]
        positions=self.__deleteElements(selectedPositions,positions,limit)

        while full < positions.size:
            index = positions[full]
            if self.weight + self.problem.weights[index] < self.problem.capacity:
                self.cells[index] = 1
                self.weight = self.weight + self.problem.weights[index]
                self.fitness = self.fitness + self.problem.profits[index]
            full=full+1

    def __deleteElements(self,selectedPositions,positions,limit):

        for d in positions:
            index = np.where(positions == d)[0]
            if index[0] > limit:
                positions = np.delete(positions, index)

        for i in selectedPositions:
            index = np.where(positions == i)[0]
            positions = np.delete(positions, index)

        return positions

    def show(self):
        print(self.cells)
        print(self.fitness)
