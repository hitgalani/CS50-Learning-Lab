# CS50 AI Lecture 0: Search

Video: Search - Lecture 0 - CS50's Introduction to Artificial Intelligence
with Python (CS50, about 1h 49m). Check timestamps in the video yourself.

## 1. What is search?
Search means finding a series of actions that takes an agent from a start
to a goal, like solving a maze or a puzzle.

## 2. Parts of a search problem
- **Agent:** the thing that looks at its surroundings and acts.
- **State:** one situation the agent can be in.
- **Initial state:** where we start.
- **Actions:** the moves possible in a state.
- **Transition model:** which state we reach after an action.
- **Goal test:** a check to see if we reached the goal.
- **Path cost:** the price of a path, such as distance or time.
- **Solution:** a path from start to goal. **Optimal** means the lowest cost.

## 3. How a search runs
1. Put the start in the **frontier** (nodes waiting to be explored).
2. Take one node out. If it is the goal, stop.
3. Otherwise add its neighbours to the frontier.
4. Repeat until the frontier is empty.

Keep an **explored set** so you never visit a state twice. Without it the
search can loop forever.

## 4. Uninformed search (no guess about the goal)
| Search | Frontier type | Idea | Good / bad |
|---|---|---|---|
| Depth first (DFS) | stack (last in, first out) | go deep, backtrack at dead end | uses little memory, may not find the shortest path |
| Breadth first (BFS) | queue (first in, first out) | explore all neighbours level by level | finds the shortest path (when each step costs the same), uses more memory |

## 5. Informed search (uses a heuristic)
A **heuristic** is a rule-of-thumb guess of how close a state is to the goal.
- **Greedy best first:** picks the node that looks closest. Fast, but it can
  be fooled and give a longer route.
- **A\* search:** picks the node with the smallest `cost so far + guess`.
  It gives the best path if the guess never overestimates the real distance.

## 6. Adversarial search (games with an opponent)
- **Minimax:** one player (MAX) wants the highest score, the other (MIN)
  wants the lowest. Each assumes the other plays perfectly.
- **Alpha-beta pruning:** skips branches that cannot change the final answer.
  Same result as minimax, with less work.
- **Depth-limited minimax:** stop at a set depth and use an **evaluation
  function** to estimate the score. Needed when the game is too big to search fully.

## 7. Mistakes to avoid
- Forgetting the explored set, which causes infinite loops.
- Using a heuristic that overestimates, so A* may not be optimal.
- Thinking DFS always gives the shortest path. It does not.
- Forgetting that minimax assumes the opponent plays well.

## 8. Review questions
1. Why do we need an explored set?
2. What is the difference between DFS and BFS in terms of the frontier?
3. What two things does A* add together?
4. What does alpha-beta pruning save?
5. Why do big games need depth-limited minimax?

**Answers (check after trying):**
1. To avoid visiting the same state again and looping forever.
2. DFS uses a stack, BFS uses a queue.
3. Cost so far and the heuristic guess.
4. Time, by skipping branches that cannot change the result.
5. The full game tree is too large, so you stop early and estimate.

## 9. Hints for the problem set (hints only)
- **Degrees:** think of people as states and shared movies as the actions.
  Which search guarantees the fewest steps?
- **Tic-Tac-Toe:** write small helper functions first (whose turn, possible
  moves, who won, is the game over). When you make a move on a trial board,
  work on a copy so the real board is not changed.
- Test each small function alone before combining them.

## 10. Try yourself
- In `00.py`, change `guess["C"]` to `1` and run greedy again. Does it
  still find the best path?
- Add a new city to the graph and run all four searches.
- Draw the minimax tree on paper and find the answer before running it.