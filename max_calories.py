from tabulate import tabulate


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items: dict, budget: int) -> int:
    # create items list with calories/cost ratio included
    item_ratios = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        item_ratios.append({
            "name": name,
            "cost": data["cost"],
            "calories": data["calories"],
            "ratio": ratio
        })
    item_ratios.sort(key=lambda x: x['ratio'], reverse=True)

    total_cost = 0
    total_calories = 0
    selected_items = []

    # select dishes as long as the budget allows
    for item in item_ratios:
        if total_cost + item["cost"] <= budget:
            total_cost += item["cost"]
            total_calories += item["calories"]
            selected_items.append(item["name"])

    print(item_ratios)

    return selected_items, total_cost, total_calories


def dynamic_programming(items: dict, budget: int):
    """
    Find a optimal food set for maximizing calories within limited budget
    """
    item_list = list(items.items())
    n = len(item_list)

    # initialize table (n+1 row, budget+1 column)
    K = [[0] * (budget + 1) for _ in range(n + 1)]

    # fill out DP table
    for i in range(1, n + 1):
        item_name, item_data = item_list[i-1]
        cost = item_data["cost"]
        calories = item_data["calories"]

        for w in range(budget + 1):
            if cost > w:
                # if product cost is higher than the left budget, do not take it
                K[i][w] = K[i-1][w]
            else:
                # take product and its calories within available budget
                K[i][w] = max(K[i-1][w], calories + K[i-1][w - cost])

    total_calories = K[n][budget]
    total_cost = 0
    selected_items = []

    w = budget
    for i in range(n, 0, -1):
        # if value in current cell is different from value in prev row,
        # it means we took product i
        if K[i][w] != K[i-1][w]:
            item_name, item_data = item_list[i-1]
            selected_items.append(item_name)
            total_cost += item_data["cost"]
            w -= item_data["cost"]

    return selected_items, total_cost, total_calories


if __name__ == "__main__":

    budget = 105

    # Greedy Algorithm
    items_g, cost_g, cal_g, = greedy_algorithm(items, budget)

    # Dynamic Programming
    items_dp, cost_dp, cal_dp = dynamic_programming(items, budget)

    # Prepare the data for the table
    table_data = [
        ["Greedy Algorithm", cal_g, cost_g, ", ".join(items_g)],
        ["Dynamic Programming", cal_dp, cost_dp, ", ".join(items_dp)]
    ]

    headers = ["Algorithm", "Total Calories", "Total Cost", "Selected Dishes"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
