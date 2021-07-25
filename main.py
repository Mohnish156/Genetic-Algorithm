import sys
from random import random, randint, randrange, uniform
import numpy.random as npr
from typing import List

pop_size = 10
crossover_rate = 1
mutation_rate = 0.2
alpha = 5
elite_percent = 0.2
generations = 10

all_items = list()

capacity = 269


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def main():
    create_data_struct()
    genetic_algorithm()

def genetic_algorithm():
    genome = generate_genome()
    best_chromosome = []
    for generation in range(generations):

        for chromosome in genome:
            if fitness_function(chromosome) > fitness_function(best_chromosome):
                best_chromosome = chromosome.copy()

        print("current generation: " + str(generation) + "\tbest: " + str(calculate_value(best_chromosome)))
        ye = calculate_value(best_chromosome)
        genome.sort(key=lambda chromo: fitness_function(chromo), reverse=True)
        new_genome = [] #need to implement elitism
        new_genome.append(genome[0])
        new_genome.append(genome[1])
        while len(new_genome) <= pop_size:
            p1 = roulette_wheel_selection(genome)
            p2 = roulette_wheel_selection(genome)
            children1, children2 = crossover(p1, p2)

            new_genome.append(mutation(children1, 1, mutation_rate))
            new_genome.append(mutation(children2, 1, mutation_rate))
        genome = new_genome

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
    pick = uniform(0, (max_val-sys.float_info.min))
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
    fitness = calculate_value(chromosome) - (alpha * max(0, (calculate_weight(chromosome) - capacity)))
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
