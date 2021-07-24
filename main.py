from random import random, randint, randrange, uniform
import numpy.random as npr
from typing import List

pop_size = 50
crossover_rate = 1
mutation_rate = 0.2
alpha = 2
elite_percent = 0.2
generations = 100

all_items = list()

capacity = 269


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def main():
    create_data_struct()
    genetic_algorithm()


def genetic_algorithm():
    genome = generate_genome()
    best_chromosome = None
    i = 0
    ordered = genome.copy()
    while i < generations:

        for chromosome in range(len(ordered) - 1):
            if fitness_function(ordered[chromosome]) > fitness_function(ordered[chromosome + 1]):
                ordered[chromosome], ordered[chromosome + 1] = ordered[chromosome + 1], ordered[chromosome]
        best_chromosome = ordered[0]
        print(calculate_value(best_chromosome))
        new_genome = list()
        # implement elites
        new_genome.append(ordered[0].copy())
        new_genome.append(ordered[1].copy())

        while len(new_genome) <= pop_size:
            p1 = roulette_wheel_selection(new_genome)
            p2 = roulette_wheel_selection(new_genome)
            children = crossover(p1, p2)

            new_genome.append(mutation(children[0], 1, mutation_rate).copy())
            new_genome.append(mutation(children[1], 1, mutation_rate).copy())
        ordered = new_genome.copy()
        i += 1
    return print(calculate_value(best_chromosome))


def create_data_struct():
    lines = list()
    file = open("10_269", "r")
    for line in file:
        lines.append(line)

    del lines[0]
    for pair in lines:
        x = pair.split()
        I1 = Item(x[0], x[1])
        all_items.append(I1)


def roulette_wheel_selection(genome):
    max_val = sum(fitness_function(chromosome) for chromosome in genome)
    pick = uniform(0, max_val)
    current = 0
    for chromosome in genome:
        current += fitness_function(chromosome)
        if current > pick:
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
    fitness = calculate_value(chromosome) - (alpha * max(0, calculate_weight(chromosome) - capacity))
    return fitness


def mutation(chromosome, num: int = 1, probability: float = mutation_rate):
    for x in range(num):
        index = randrange(len(chromosome))
        chromosome[index] = chromosome[index] if random() > probability else abs(chromosome[index] - 1)
    return chromosome


def crossover(chromosome_1, chromosome_2):
    point = randint(1, len(chromosome_1))

    for i in range(point, len(chromosome_1)):
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
