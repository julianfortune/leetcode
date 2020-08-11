# Leetcode
Solutions to leetcode challenges

## 746. Min Cost Climbing Stairs `Easy`

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

#### Example 1:
```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```

#### Example 2:
```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```

#### Note:

1. Cost will have a length in the range [2, 1000].
1. Every cost[i] will be an integer in the range [0, 999].

### Solution

``` python3
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    cheapestPathTo = {} # Dictionary mapping `stair index` to cost to get there

    # Uses cached values
    def costToStep(index):
      if index < 0:
        return 0
      else:
        return cheapestPathTo[index]

    # Work from the beginning of the stairs to the top
    for index, currentCost in enumerate(cost):
      oneStepCost = costToStep(index - 1)
      twoStepCost = costToStep(index - 2)

      cheapestPathTo[index] = min(oneStepCost, twoStepCost) + currentCost

    lastStair = cheapestPathTo[len(cost) - 1]
    secondToLastStair = cheapestPathTo[len(cost) - 2]

    return min(lastStair, secondToLastStair)
```
