import random


def choose_initial_solution():
    print("Choose random initial solution or take input from user?")
    print("1. Random")
    print("2. User Input")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        return random.uniform(-10, 10)  # Random initial solution between -10 and 10
    elif choice == 2:
        return float(input("Enter initial solution: "))
    else:
        print("Invalid choice, try again!")
        return choose_initial_solution()


def evaluate_objective_function(solution):
    return solution**2  # Maximizing a quadratic function


def generate_neighbors(solution):
    return [solution + random.uniform(-1, 1) for _ in range(5)]


def select_best_neighbor(neighbors):
    return max(neighbors, key=evaluate_objective_function)


# Termination Criteria
max_iterations = 100  # Total number of iterations
no_improvement_threshold = 10  # Number of iterations with no improvement
objective_threshold = -90  # Stop if the objective function value reaches this threshold

initial_solution = choose_initial_solution()
current_solution = initial_solution
current_value = evaluate_objective_function(current_solution)

no_improvement_count = 0

for _ in range(max_iterations):
    neighbors = generate_neighbors(current_solution)

    best_neighbor = select_best_neighbor(neighbors)
    best_value = evaluate_objective_function(best_neighbor)

    # Check if the best neighbor improves the current solution
    if best_value > current_value:
        current_solution = best_neighbor
        current_value = best_value
        no_improvement_count = 0
    else:
        no_improvement_count += 1

    # Termination checks
    if no_improvement_count >= no_improvement_threshold:
        print(
            "Terminating due to no improvement for",
            no_improvement_threshold,
            "iterations.",
        )
        break

    if current_value >= objective_threshold:
        print("Terminating due to reaching the objective threshold.")
        break

print("Initial Solution:", initial_solution)
print("Best Solution:", current_solution)
print("Objective Value:", current_value)
