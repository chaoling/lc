'''
134. Gas Station
Medium
Topics
Companies
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104
'''
from collections import List
def canCompleteCircuitBrutalForce(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    assert n == len(cost)
    '''
    brute force:
    start from index i=0, if gas[i] < cost[i] then return false 
    for any other index, general formula is tank + gas[i] < cost[i] return false
    '''
    for i in range(n):
        tank = 0 #start with empty tank
        for j in range(n):
            index = (i+j) % n
            if tank + gas[index] < cost[index]:
                break #bail early inner loop, change starting index
            tank += gas[index]
            tank -= cost[index]
        else:
            return i
    else:
        return -1


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    n = len(gas)
    assert n == len(cost)
    '''
    optimization: Greedy Algorithm
    If the total amount of gas is greater than or equal to the total cost, a solution must exist (as the problem guarantees uniqueness when it does). We just need to find the starting index.

💡  Step-by-Step Greedy Strategy:
    Track total gas and total cost to verify feasibility.

    Iterate through stations once.

    Track a running gas tank.

    If the tank goes below 0, it means we can’t reach the next station from current start. So:

    Reset the start to the next station.

    Reset the current tank to 0.

    Return the final start index.
    '''
    total_gas, total_cost, tank, start_index = 0,0,0,0
    for i in range(n):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        #If tank is negative, cannot reach next gas station from current start index
        if tank < 0:
            start_index = i + 1
            tank = 0

    return start_index if total_gas >= total_cost else -1