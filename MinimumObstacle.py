"""
Math 482 SP2020 Final Project
Adwitiya Singh: 109772141
Elijah Razavi: 10956611
Irmuun Zamilan: 201105079
"""


from math import floor, pi, e
from typing import List, Any, Dict
from itertools import combinations
# Arrays to store all the puzzles
coloursOne: List[List[int]] = []
coloursTwo: List[List[int]] = []
coloursThree: List[List[int]] = []
coloursFour: List[List[int]] = []

# Arrays to store the solution
side1: List[int] = []
side2: List[int] = []
side3: List[int] = []

# Array  storing the occurrences of each colour
colour_values: Dict[int, List[List[int]]]


# Generating all the puzzles and storing them
for n in range(1, 300, 3):
    coloursOne.append([1 + (floor(n * pow(pi, 10))) % 100, 1 + (floor((n + 1) * pow(pi, 10))) % 100,
                       1 + (floor((n + 2) * pow(pi, 10))) % 100])
    coloursTwo.append([1 + (floor(n * pow(e, 10))) % 100, 1 + (floor((n + 1) * pow(e, 10))) % 100,
                       1 + (floor((n + 2) * pow(e, 10))) % 100])
    coloursThree.append([1 + ((n * 51) % 100), 1 + (((n + 1) * 51) % 100), 1 + (((n + 2) * 51) % 100)])
    coloursFour.append([1 + ((n * 24) % 100), 1 + (((n + 1) * 24) % 100), 1 + (((n + 2) * 24) % 100)])


def fix_sides(iteration: int):
    while len(side1) > iteration:
        side1.pop()
        side2.pop()
        side3.pop()


def solve(iteration: int, puzzle: List[List[int]]) -> bool:
    """
    Recursively rotates slices and looks for solutions and stores the, maybe partial, solution in the sides array.
    :param iteration: The number of the block that we're inserting
    :param puzzle: The puzzle that we're trying to solve
    :return True of a solution exists, false otherwise
    """
    if iteration == len(puzzle):
        return True
    if try_insert(iteration, 0, puzzle):
        if solve(iteration + 1, puzzle):
            return True
    if try_insert(iteration, 1, puzzle):
        if solve(iteration + 1, puzzle):
            return True
    if try_insert(iteration, 2, puzzle):
        if solve(iteration + 1, puzzle):
            return True
    return False


def try_insert(iteration: int, side: int, puzzle: List[List[int]]) -> bool:
    """
    Function to insert into the answers array and handle rotations
    :param iteration: The number of the block that we're inserting
    :param side: The side of the slice that we're assuming is "side 1"
    :param puzzle: The puzzle that we're trying to insert into
    :return True of inserting was successful without any conflicts, false otherwise
    """
    fix_sides(iteration)

    if puzzle[iteration][side % 3] in side1:
        return False
    if puzzle[iteration][(side + 1) % 3] in side2:
        return False
    if puzzle[iteration][(side + 2) % 3] in side3:
        return False

    if iteration >= len(side1):
        side1.insert(iteration, puzzle[iteration][side % 3])
        side2.insert(iteration, puzzle[iteration][(side + 1) % 3])
        side3.insert(iteration, puzzle[iteration][(side + 2) % 3])
    else:
        side1[iteration] = puzzle[iteration][side % 3]
        side2[iteration] = puzzle[iteration][(side + 1) % 3]
        side3[iteration] = puzzle[iteration][(side + 2) % 3]


    return True


def check_for_duplicates(list_of_elems: List[Any]):
    """
    Function to check for duplicates in a list.
    This can be used to check if a solution side has a repeating colour
   which can tell us if there is a conflict
   :param list_of_elems: The list in which we're trying to find duplicates
   :return True of duplicates exist in the list, false otherwise
   """
    if len(list_of_elems) == len(set(list_of_elems)):
        return False
    else:
        return True


def find_obstacles(puzzle) -> List[List[int]]:
    """Function to call the solve method on every subset of a given puzzle
       :param puzzle: The puzzle for which we're trying to find a minimum obstacle
       :return The subsets of a puzzle that don't have a solution
    """
    for subset in puzzle:
        global side1, side2, side3
        side1 = []
        side2 = []
        side3 = []
        solution = solve(0, subset)
        if not solution:
            return subset
    return []


def find_minimum_obstacle(puzzle: List[List[int]], upper_bound: int = None) -> List[List[int]]:
    """
    Finds minimum obstacle of a given size
    :param puzzle: The puzzle for which we're trying to find a minimum obstacle
    :param upper_bound: The max size of the minimum obstacle
    :return A list of all minimum obstacles
    """
    if upper_bound is None:
        upper_bound = len(puzzle) + 1
    minimum_obstacle_set: List[List[int]]

    for k in range(2, upper_bound):
        combinations_of_k = combinations(puzzle, k)
        minimum_obstacle_set = find_obstacles(combinations_of_k)
        if len(minimum_obstacle_set) == 0:
            continue
        else:
            return minimum_obstacle_set
    return []


# def find_four_group
def count_occurences(puzzle: List[List[int]]) -> bool:
    """
    Function to check if every colour occurs only three times in a puzzle, in which case,
    it might have a solution
    :param puzzle: The puzzle in which we want to count the occurrences of all colours
    :return True if all colours occur only three times, false otherwise
    """
    global colour_values
    colour_values = {}
    all_three: bool = True
    for value in puzzle:
        if value[0] not in colour_values:
            colour_values[value[0]] = []
        if value[1] not in colour_values:
            colour_values[value[1]] = []
        if value[2] not in colour_values:
            colour_values[value[2]] = []
        distinct_values = set(value)

        for dist_value in distinct_values:
            colour_values[dist_value].append(value)
        if len(colour_values[value[0]]) >3 or len(colour_values[value[1]]) >3 or len(colour_values[value[2]]) >3:
            all_three = False
    return all_three


def findsolution(puzzle: List[List[int]], which: int):
    """
    Driver function to find the solution/MO for a puzzle
    :param puzzle: The puzzle that we're trying to solve/Find an MO for
    :param which: Which puzzle are we on out of the four
    :return: None
    """
    global colour_values
    if count_occurences(puzzle):
        if solve(0, puzzle):
            print("\n\nPuzzle "+ str(which)+" is solvable and the solution, in the form "
                  "of three arrays representing the three sides of the solution tower, is")
            print(side1)
            print(side2)
            print(side3)
            return
    colour_values = {k: v for k, v in sorted(colour_values.items(), key=lambda item: len(item[1]), reverse=True)}
    obstacles: Dict[int, List[List[int]]] = {}
    for v in colour_values.values():
        minobs: List[List[int]] = find_minimum_obstacle(v)
        if len(minobs) == 0:
            continue
        if len(minobs) not in obstacles:
            obstacles[len(minobs)] = []
        obstacles[len(minobs)].append(minobs)
    obstacles = {k: v for k, v in sorted(obstacles.items(), key=lambda item: item[0])}
    smaller_obstacles = find_minimum_obstacle(puzzle, list(obstacles)[0])
    minimum_obstacles = obstacles.values()
    if len(smaller_obstacles) > 0:
        minimum_obstacles = smaller_obstacles
    print("\n\nThe smallest minimal obstacle for puzzle " + str(which) + " is of size " + str(list(obstacles)[0]))
    print("Here are all of them:")
    print(str(minimum_obstacles).replace("(", "\n").replace(")", "")[14:-2])


if __name__ == '__main__':
    findsolution(coloursOne, 1)
    findsolution(coloursTwo, 2)
    findsolution(coloursThree, 3)
    findsolution(coloursFour, 4)
    #An example to see if the algo solves puzzles that require a lot of backtracking
    findsolution([[1, 2, 3], [4, 5, 6], [5, 3, 3], [2, 1, 2], [ 5, 1, 6], [ 4, 6, 4]], 5)
    findsolution([[1, 6, 1], [2, 2, 6], [6, 2, 1]], 6)
    #Testing a puzzle that requires flipping to solve
    findsolution([[1, 2, 3], [3, 1, 2], [3, 2, 1]], 7)



