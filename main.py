import math
from random import random, randint, randrange, uniform
import numpy as np
import matplotlib.pyplot as plt

pop_size = 20
crossover_rate = 1
mutation_rate = 0.3
alpha = 4
elite_percent = 0.05
generations = 100

all_items = list()

capacity = 0
avg = []


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


def main():
    create_data_struct()
    Sum = 0
    values = []



    for x in range(5):
        values.append(genetic_algorithm())
    Sum = sum(values)
    print("Mean: ", Sum / 5)
    print("Standard Deviation, ", np.std(values))

    print(len(avg))

    gens = []
    for x in range(generations):
        gens.append(x)
    plt.plot(gens, avg[0])
    plt.xlabel("Generations")
    plt.ylabel("Average fitness of the 5 best solutions in the population")
    plt.savefig("10_269_converge.png")


def genetic_algorithm():
    current_avg = []
    genome = generate_genome()
    best_chromosome = []
    for generation in range(generations):

        for chromosome in genome:
            if fitness_function(chromosome) > fitness_function(best_chromosome):
                best_chromosome = chromosome.copy()

        # print("current generation: " + str(generation) + "\tbest: " + str(calculate_value(best_chromosome)))

        genome.sort(key=lambda chromo: fitness_function(chromo), reverse=True)

        new_genome = []
        top_chromosomes = math.ceil(elite_percent * len(genome))

        for top in range(top_chromosomes):
            new_genome.append(genome[top])
        while len(new_genome) <= pop_size:
            p1 = list(roulette_wheel_selection(genome))
            p2 = list(roulette_wheel_selection(genome))

            children1, children2 = crossover(p1, p2)

            new_genome.append(mutation(children1, 1, mutation_rate))
            new_genome.append(mutation(children2, 1, mutation_rate))

        best_5 = []
        for x in range(5):
            best_5.append(calculate_value(genome[x]))

        mean = sum(best_5) / 5
        current_avg.append(mean)
        genome = new_genome

    avg.append(current_avg)
    return calculate_value(best_chromosome)


def create_data_struct():
    lines = list()
    file = open("10_269", "r")
    for line in file:
        lines.append(line)

    first_line = lines[0].split()
    global capacity
    capacity = int(first_line[1])

    del lines[0]
    del lines[0]
    for pair in lines:
        x = pair.split()
        I1 = Item(x[0], x[1])
        all_items.append(I1)


def roulette_wheel_selection(genome):
    max_val = sum(fitness_function(chromosome) for chromosome in genome)
    chosen = uniform(0, max_val)
    current = 0
    for chromosome in genome:
        current += fitness_function(chromosome)
        if current > chosen:
            return chromosome


def calculate_weight(chromosome):
    weight = 0
    index = 0
    for bit in chromosome:
        if bit == 1:
            weight += int(all_items[index].weight)
        index += 1
    return weight


def calculate_value(chromosome):
    value = 0
    index = 0
    for bit in chromosome:
        if bit == 1:
            value += int(all_items[index].value)
        index += 1
    return value


def fitness_function(chromosome):
    fitness = calculate_value(chromosome) - (alpha * max(0, (calculate_weight(chromosome) - capacity)))
    return fitness


def mutation(chromosome, num: int = 1, probability: float = mutation_rate):
    for x in range(num):
        index = randrange(len(chromosome))
        chromosome[index] = chromosome[index] if random() > probability else abs(chromosome[index] - 1)
    return chromosome


def crossover(chromosome_1, chromosome_2):
    length = len(chromosome_1)
    point = randint(1, length)

    for i in range(point, length):
        chromosome_1[i] = chromosome_2[i]
        chromosome_2[i] = chromosome_1[i]
    return chromosome_1, chromosome_2


def generate_genome():
    genome = list()
    for i in range(pop_size):
        chromosome = list()
        for x in range(len(all_items)):
            chromosome.append(randint(0, 1))
        genome.append(chromosome.copy())

    return genome


if __name__ == '__main__':
    main()
