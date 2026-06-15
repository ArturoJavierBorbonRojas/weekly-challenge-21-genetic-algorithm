# Weekly challenge 21: Bio-inspired Optimization (Genetic Algorithm)

## Description
Welcome to Week 21! After heavily focusing on mathematical algorithms and data structures, I decided to venture into the fascinating world of **Bio-inspired Metaheuristics**. I built a **Genetic Algorithm** from scratch to solve a string-matching optimization problem.

Instead of writing strict rules for the computer to follow, a Genetic Algorithm creates an environment that simulates Darwinian natural selection. The algorithm generates random solutions, evaluates their "fitness", and allows them to evolve over time until it finds the optimal answer.

## How it works
The algorithm relies on four core biological principles:
1. **Initialization:** A population of random strings (DNA) is generated.
2. **Fitness Function:** Each string is evaluated based on how closely it resembles the target goal (`MAESTRIA UANL`).
3. **Selection & Crossover:** The "fittest" individuals are selected to reproduce. Their strings are sliced and combined to create a new generation of offspring.
4. **Mutation:** To maintain genetic diversity and prevent the algorithm from getting stuck in a local minimum, there is a small probability (5%) that a character will randomly change.

This loop repeats until an individual evolves into the exact target string.

##  Complexity Analysis
* **Time Complexity:** $O(G \times P \times L)$ where $G$ is the number of generations required to converge, $P$ is the population size, and $L$ is the length of the target string. 
* **Space Complexity:** $O(P \times L)$ to store the population array in memory at any given generation.

## 🛠Dependencies
* Python 3.14.3 (Standard Libraries: `random`, `string`)
