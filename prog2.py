import numpy as np
from numpy import random
import copy
import matplotlib.pyplot as plt

population_size = 1000
mutation_pct = 0.9
average_fitness = []
generation = []

#normalized fitnesws to select parents for next generation
def fitness(population, num_iterations):
    temp_fitness_list = []
    for chromosomes in population:
        #calculate fitness
        fitness_value = 0
        for i in range(len(chromosomes) - 1):
            for j in range(i + 1, len(chromosomes)):
                if chromosomes[i] == chromosomes[j]:
                    fitness_value += 1
        for i in range(len(chromosomes) - 1):
            for j in range(i + 1, len(chromosomes)):
                if abs(chromosomes[j] - chromosomes[i]) == abs(j - i):
                    fitness_value += 1
        fitness_value = 28 - fitness_value
        if fitness_value == 28:
            print("Generation: ",generation[len(generation)-1])
            print(chromosomes)
            return 28
        temp_fitness_list.append(fitness_value)
    if num_iterations % 100 == 0:
        print("Generation: ",generation[len(generation)-1])
        print(chromosomes)
    return temp_fitness_list

#helper percentage function
def percentage(fitness_list, fitness_percentage):
    total = 0
    for i in fitness_list:
        total += i
    for j in range(0, len(fitness_list)):
        fitness_percentage.append(fitness_list[j] / total)
    average_fitness.append(total / population_size)

#perform mutation at random, if it occurs force a random change on the chromosome
def mutation(chromosomes):
    pct = np.random.rand(8)
    for i in range(len(pct)):
        if pct[i] > mutation_pct:
            chromosomes[i] = random.randint(0, 8)
    return chromosomes
