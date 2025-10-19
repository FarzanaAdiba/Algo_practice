#given the cost and cost[i] is the cost of ith step, return the minimum cost to reach the top of the floor
 
"""
Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Subproblem:
Here the minimum cost will be counted. for step, n=3 the min cost will be counted from index=0,1,2.
So for step n, the min cost= cost[n]+min(cost to reach n-1 step, cost to reach n-2 step)
 
"""
def min_cost_memo(n, cost, memo):
    if n in memo:
        return memo[n]
    if n==0:
        return cost[0]
    if n==1:
        return cost[1]
    
    result = cost[n]+min(min_cost_memo(n-1, cost, memo), min_cost_memo(n-2, cost, memo))
    memo[n] = result
    return result
def min_cost_calc(cost):
    n = len(cost)
    memo = {}
    return min(min_cost_memo(n-1, cost, memo), min_cost_memo(n-2, cost, memo))

if __name__ == "__main__":
    cost=[10, 15, 20]
    print(min_cost_calc(cost))
    
