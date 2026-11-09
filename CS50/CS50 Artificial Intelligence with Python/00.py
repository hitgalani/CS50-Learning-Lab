# practice for cs50 ai lecture 0 - search

# a small map of cities, each city lists its neighbours
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E", "G"],
    "G": ["F"],
}


# depth first search: take the newest path (stack)
def dfs(start, goal):
    frontier = [[start]]      # frontier is a list of paths
    explored = set()          # states we already visited
    while frontier:
        path = frontier.pop()         # last in, first out
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            if n not in explored:
                frontier.append(path + [n])
    return None


# breadth first search: take the oldest path (queue)
def bfs(start, goal):
    frontier = [[start]]
    explored = set()
    while frontier:
        path = frontier.pop(0)        # first in, first out
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in graph[state]:
            if n not in explored:
                frontier.append(path + [n])
    return None


# roads with distances, used for greedy and A*
roads = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "F": 3},
    "E": {"C": 10, "F": 2},
    "F": {"D": 3, "E": 2, "G": 6},
    "G": {"F": 6},
}

# heuristic: a guess of how far each city is from G
guess = {"A": 15, "B": 12, "C": 14, "D": 8, "E": 7, "F": 5, "G": 0}


# greedy best first: always pick the city that looks closest to goal
def greedy(start, goal, h):
    frontier = [(h[start], [start])]
    explored = set()
    while frontier:
        frontier.sort()               # smallest guess first
        _, path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path
        if state in explored:
            continue
        explored.add(state)
        for n in roads[state]:
            if n not in explored:
                frontier.append((h[n], path + [n]))
    return None


# A* search: cost so far + guess to goal
def a_star(start, goal, h):
    frontier = [(h[start], 0, [start])]
    best_cost = {}
    while frontier:
        frontier.sort()
        _, cost, path = frontier.pop(0)
        state = path[-1]
        if state == goal:
            return path, cost
        if state in best_cost and best_cost[state] <= cost:
            continue                  # we already reached it cheaper
        best_cost[state] = cost
        for n, c in roads[state].items():
            new_cost = cost + c
            frontier.append((new_cost + h[n], new_cost, path + [n]))
    return None, None


# minimax on a small tree made of lists
# numbers are final scores, lists are choices
# root is MAX, next level is MIN, and so on
tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]


def minimax(node, is_max):
    if isinstance(node, int):         # a leaf, just return the score
        return node
    scores = [minimax(child, not is_max) for child in node]
    return max(scores) if is_max else min(scores)


# alpha beta pruning: same answer but skips useless branches
visited = 0


def alphabeta(node, is_max, alpha, beta):
    global visited
    if isinstance(node, int):
        visited += 1
        return node
    if is_max:
        best = float("-inf")
        for child in node:
            best = max(best, alphabeta(child, False, alpha, beta))
            alpha = max(alpha, best)
            if alpha >= beta:         # MIN above will never allow this
                break
        return best
    else:
        best = float("inf")
        for child in node:
            best = min(best, alphabeta(child, True, alpha, beta))
            beta = min(beta, best)
            if alpha >= beta:         # MAX above will never allow this
                break
        return best


# depth limited minimax: stop early and guess the score
def flatten(node):
    if isinstance(node, int):
        return [node]
    nums = []
    for child in node:
        nums += flatten(child)
    return nums


def depth_limited(node, is_max, depth):
    if isinstance(node, int):
        return node
    if depth == 0:
        nums = flatten(node)
        return sum(nums) / len(nums)  # simple evaluation: the average
    scores = [depth_limited(c, not is_max, depth - 1) for c in node]
    return max(scores) if is_max else min(scores)


def main():
    print("DFS:", dfs("A", "G"))
    print("BFS:", bfs("A", "G"))
    print("Greedy:", greedy("A", "G", guess))
    path, cost = a_star("A", "G", guess)
    print("A*:", path, "cost", cost)

    print("Minimax:", minimax(tree, True))
    print("Alpha-beta:", alphabeta(tree, True, float("-inf"), float("inf")))
    print("Leaves checked by alpha-beta:", visited, "out of 9")

    deep = [[[3, 5], [6, 9]], [[1, 2], [0, -1]]]
    print("Full minimax:", minimax(deep, True))
    print("Depth 1 guess:", depth_limited(deep, True, 1))


main()