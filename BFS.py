# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 17:29:37 2022
@author: Eriny
"""

from Queue import Queue
import helpers as he


def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}

    while not queue.isEmpty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return he.get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = he.offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if he.is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = he.read_maze("mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = bfs(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = he.read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    assert result is None

    # Test 4
    maze = [['0', '0', '*', '0'],
            ['0', '0', '0', '0'],
            ['0', '*', '0', '*'],
            ['0', '0', '0', '0']]
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = bfs(maze, start_pos, goal_pos)
    print(result)