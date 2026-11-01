import random


POPULATION_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.1
GENE_MIN = -10.0
GENE_MAX = 10.0


def fitness(x):
    """Maximize the negative squared distance from 3."""
    return -(x - 3) ** 2


def create_individual():
    return random.uniform(GENE_MIN, GENE_MAX)


def selection(population):
    candidates = random.sample(
        population,
        min(5, len(population))
    )

    return max(candidates, key=fitness)


def crossover(parent1, parent2):
    alpha = random.random()

    child = (
        alpha * parent1 +
        (1 - alpha) * parent2
    )

    return child


def mutate(individual):
    if random.random() < MUTATION_RATE:
        individual += random.gauss(0, 1)

    return max(
        GENE_MIN,
        min(GENE_MAX, individual)
    )


def genetic_algorithm():
    population = [
        create_individual()
        for _ in range(POPULATION_SIZE)
    ]

    for generation in range(GENERATIONS):
        population.sort(
            key=fitness,
            reverse=True
        )

        # Preserve the best individuals.
        next_population = population[:2]

        while len(next_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)
            child = mutate(child)

            next_population.append(child)

        population = next_population

        best = max(population, key=fitness)

        if generation % 10 == 0:
            print(
                f"Generation {generation:3d} | "
                f"Best solution: {best:.6f} | "
                f"Fitness: {fitness(best):.6f}"
            )

    best = max(population, key=fitness)

    return best


if __name__ == "__main__":
    random.seed(42)

    solution = genetic_algorithm()

    print("\nOptimization completed.")
    print(f"Best solution: {solution:.8f}")
    print(f"Best fitness: {fitness(solution):.8f}")
