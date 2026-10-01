def optimal_storage(demand, capacity, holding_cost, shortage_cost):
   
    n = len(demand)
    
    dp = [[float("inf")] * (capacity + 1) for _ in range(n + 1)]

    
    for s in range(capacity + 1):
        dp[n][s] = 0

    decision = [[0] * (capacity + 1) for _ in range(n)]

    
    for i in range(n - 1, -1, -1):
        for storage in range(capacity + 1):

            for next_storage in range(capacity + 1):

                available = storage + next_storage
                shortage = max(0, demand[i] - available)

                cost = (
                    holding_cost * next_storage
                    + shortage_cost * shortage
                    + dp[i + 1][next_storage]
                )

                if cost < dp[i][storage]:
                    dp[i][storage] = cost
                    decision[i][storage] = next_storage

    
    storage = 0
    optimal_plan = []

    for i in range(n):
        next_storage = decision[i][storage]

        available = storage + next_storage
        shortage = max(0, demand[i] - available)

        optimal_plan.append({
            "stage": i + 1,
            "starting_storage": storage,
            "demand": demand[i],
            "ending_storage": next_storage,
            "shortage": shortage
        })

        storage = next_storage

    return dp[0][0], optimal_plan



demand = [5, 8, 6, 7]
capacity = 10
holding_cost = 2
shortage_cost = 10

cost, plan = optimal_storage(
    demand,
    capacity,
    holding_cost,
    shortage_cost
)

print("Minimum total cost:", cost)

for stage in plan:
    print(stage)
