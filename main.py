import random
from typing import Tuple, List, Callable

pop_size = 50
crossover_rate = 1
mutation_rate = 0.2
Genome = List[int]


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


def select_pair(population, fitness_func):
    return random.choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )


def mutation(genome: Genome, num: int = 1, probability: float = mutation_rate) -> Genome:
    for i in range(num):
        index = random.randrange(len(genome))
        genome[index] = genome[index] \
            if random() > probability \
            else abs(genome[index] - 1)
    return genome


def crossover(genome1, genome2):
    point = random.randint(1, genome1.size)

    for i in range(point, len(genome1)):
        genome1[i] = genome2[i]
        genome2[i] = genome1[i]
    return genome1, genome2


def generate_genome():
    genome = list()
    for i in range(pop_size):
        genome.append(random.randint(0, 1))

    return genome


if __name__ == '__main__':
    main()
