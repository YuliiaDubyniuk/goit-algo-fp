import numpy as np
from tabulate import tabulate


def simulate_dice_rolls(num_simulations: int) -> dict:
    """
    Simulate 2 dices throw for given of simulations.
    Calculate and return probabilities for each unique sum of points.
    """
    dice1 = np.random.randint(1, 7, size=num_simulations)
    dice2 = np.random.randint(1, 7, size=num_simulations)

    total_sums = dice1 + dice2

    # get count of each unique sum
    unique_sums, counts = np.unique(total_sums, return_counts=True)

    emp_probabilities = {}

    sum_counts = dict(zip(unique_sums, counts))

    for total_sum in range(2, 13):
        # get the number of occurrences or 0 if the sum did not occur
        count = sum_counts.get(total_sum, 0)

        # calculate probability for each sum
        probability = count / num_simulations
        emp_probabilities[total_sum] = probability

    return emp_probabilities


def get_analytical_probabilities():
    """
    Calculate and return dictionary with analytical sum probabilities.
    """
    ways_to_get_sum = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }
    total_outcomes = 36

    analytical_probabilities = {
        s: count / total_outcomes for s, count in ways_to_get_sum.items()
    }
    return analytical_probabilities


def create_comparison_table(empirical_probs, analytical_probs, num_simulations):
    """
    Generates and displays a comparative table of results.
    """
    table_data = []

    for total_sum in range(2, 13):
        p_analytical = analytical_probs.get(total_sum, 0)
        p_empirical = empirical_probs.get(total_sum, 0)
        difference = abs(p_empirical - p_analytical)

        table_data.append([
            total_sum,
            f"{p_analytical:.4f} ({p_analytical * 100:.2f}%)",
            f"{p_empirical:.4f} ({p_empirical * 100:.2f}%)",
            f"{difference:.5f}"
        ])

    headers = [
        "Sum of Points",
        "Theoretical P (Analytics)",
        f"Empirical P (Monte Carlo, N={num_simulations})",
        "Deviation (|Diff|)"
    ]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
    num_simulations = 100_000

    analytical_probabilities = get_analytical_probabilities()
    empirical_probabilities = simulate_dice_rolls(num_simulations)

    # display comparison table
    create_comparison_table(empirical_probabilities,
                            analytical_probabilities, num_simulations)
