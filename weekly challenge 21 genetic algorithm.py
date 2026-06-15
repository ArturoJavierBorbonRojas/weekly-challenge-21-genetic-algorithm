import random
import string

# Week 21: Genetic Algorithm 
# Author: Ing. Arturo Javier Borbon Rojas

# 1. Hyperparameters
TARGET = "WEEKLY CHALLENGE 21"
POPULATION_SIZE = 150
MUTATION_RATE = 0.05  # 5% chance of a gene mutating
# Our "DNA" pool: uppercase letters and a space
GENES = string.ascii_uppercase + " "

# 2. Helper Functions (The Laws of Nature)
def create_individual():
    """Generates a random string of the same length as the target."""
    return "".join(random.choice(GENES) for _ in range(len(TARGET)))

def calculate_fitness(individual):
    """Fitness = +1 for every character that matches the target exactly."""
    fitness = 0
    for i in range(len(TARGET)):
        if individual[i] == TARGET[i]:
            fitness += 1
    return fitness

def crossover(parent1, parent2):
    """Combines the DNA of two parents by splitting them at a random point."""
    split_point = random.randint(0, len(TARGET) - 1)
    child = parent1[:split_point] + parent2[split_point:]
    return child

def mutate(individual):
    """Randomly alters characters in the DNA based on the mutation rate."""
    mutated = list(individual)
    for i in range(len(mutated)):
        if random.random() < MUTATION_RATE:
            mutated[i] = random.choice(GENES)
    return "".join(mutated)

# 3. Main Evolutionary Loop
print(f"🧬 Starting Genetic Algorithm | Target: '{TARGET}'")
print("-" * 50)

# Create "Generation 0"
population = [create_individual() for _ in range(POPULATION_SIZE)]
generation = 1
best_fitness = 0

# Evolve until we reach a perfect match
while best_fitness < len(TARGET):
    # Evaluate fitness for the entire population
    population = sorted(population, key=calculate_fitness, reverse=True)
    best_individual = population[0]
    best_fitness = calculate_fitness(best_individual)

    # Print progress to watch the evolution live
    if generation % 5 == 0 or best_fitness == len(TARGET) or generation == 1:
        print(f"Generation {generation:04d} | Best DNA: [{best_individual}] | Fitness: {best_fitness}/{len(TARGET)}")

    if best_fitness == len(TARGET):
        break

    # Selection: Keep the top 50% "fittest" individuals (Elitism)
    next_generation = population[:POPULATION_SIZE // 2]

    # Crossover & Mutation: Repopulate the remaining 50%
    while len(next_generation) < POPULATION_SIZE:
        # Randomly select two parents from our elite group
        parent1 = random.choice(population[:POPULATION_SIZE // 2])
        parent2 = random.choice(population[:POPULATION_SIZE // 2])
        
        # Create a child and apply random mutation
        child = crossover(parent1, parent2)
        child = mutate(child)
        
        next_generation.append(child)

    # Replace old generation with the new one
    population = next_generation
    generation += 1

print("-" * 50)
print(f"✅ Evolution Complete in {generation} generations!")
print(f"🏆 Final Optimal Result: '{best_individual}'")