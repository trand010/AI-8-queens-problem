from prog2 import *

def main():
    #genetic algorithm
    num_iterations = 1
    population = []
    for i in range(population_size):
        population.append(np.random.choice(range(8), 8))

    while 1:
        fitness_list = []
        fitness_percentage = []
        new_population = []
        
        if num_iterations == 2000:
            print("reach maximum iterations!")
            break

        fitness_list = fitness(population, num_iterations)
        if fitness_list == 28:
            break

        percentage_list = percentage(fitness_list, fitness_percentage)
        selected_chromosomes = np.random.choice(range(population_size), population_size, replace=True, p=percentage_list)
        for chromosomesIndex in selected_chromosomes:
            new_population.append(population[chromosomesIndex])

        #crossover after highest fitness chromosomes are selected
        for i in range(0, population_size, 2):
            cross_value_one = random.randint(0, 3)
            cross_value_two = random.randint(4, 7)
            for j in range(cross_value_one, cross_value_two):
                temp1 = copy.deepcopy(new_population[i][j])
                temp2 = copy.deepcopy(new_population[i + 1][j])
                new_population[i][j] = temp2
                new_population[i + 1][j] = temp1

        for i in range(population_size):
            new_population[i] = copy.deepcopy(mutation(new_population[i]))

        population = new_population
        num_iterations += 1
        generation.append(num_iterations)

    #plot graphs
    linear_model = np.polyfit(generation, average_fitness, 12)
    linear_model_fn = np.poly1d(linear_model)
    x_s = np.arange(0, len(generation))
    plt.plot(x_s, linear_model_fn(x_s), color="red")
    plt.show()

if __name__ == "__main__":
    main()