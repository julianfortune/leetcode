# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    # Dictionary mapping `stair index` to the cheapest total cost to get there
    cheapestPathTo = {} 

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
    
    # Looking down from the top, pick between the last two stairs
    lastStair = cheapestPathTo[len(cost) - 1]
    secondToLastStair = cheapestPathTo[len(cost) - 2]

    return min(lastStair, secondToLastStair)
