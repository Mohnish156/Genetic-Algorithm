import random
from typing import Tuple

pop_size = 50
crossover_rate = 1
mutation_rate = 0.2


def main():
    genetic_algorithm()


def genetic_algorithm():
    genome = generate_genome()
    best_sol = None
    stopping_criteria = 1
    while stopping_criteria < 100:
        new_pop = list
        full = False
        # while not full:


def fitness_function(genome, items, weight_limit):
    value = 0
    weight = 0

    for i in range(items.size):
        if genome[i] == 1:
            weight += items[i].weight
            value += items[i].value

            if weight > weight_limit:
                return 0
    return value

# def select_pair(population, fitness_func):


def crossover(genome1, genome2):

    point = random.randint(1,genome1.size)
    p1, p2 = list(genome1), list(genome2)  # convert str to list
    for i in range(point, len(p1)):
        p1[i] = p2[i]
        p2[i] = p1[i]
    return p1, p2


def generate_genome():
    genome = list()
    for i in range(pop_size):
        genome.append(random.randint(0, 1))

    return genome


if __name__ == '__main__':
    main()
