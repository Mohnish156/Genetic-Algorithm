from random import random, randint, randrange, uniform
import numpy.random as npr

pop_size = 5
crossover_rate = 1
mutation_rate = 0.2
alpha = 2
elite = 0.05
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
    return 0


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
        current += chromosome.fitness
        if current > pick:
            return chromosome


def calculate_weight(chromosome):
    weight = 0
    for bit in chromosome:
        if bit == 1:
            weight += int(all_items[bit].weight)
    return weight


def calculate_value(chromosome):
    weight = 0
    for bit in chromosome:
        if bit == 1:
            weight += int(all_items[bit].value)
    return weight


def fitness_function(chromosome):
    fitness = calculate_value(chromosome) - (alpha * max(0, calculate_weight(chromosome) - capacity))
    return fitness


def mutation(chromosome, num: int = 1, probability: float = mutation_rate):
    for x in range(num):
        index = random.randrange(len(chromosome))
        chromosome[index] = chromosome[index] if random() > probability else abs(chromosome[index] - 1)
    return chromosome


def crossover(chromosome_1, chromosome_2):
    point = random.randint(1, chromosome_1.size)

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
