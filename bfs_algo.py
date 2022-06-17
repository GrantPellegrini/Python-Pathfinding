from queue import PriorityQueue
from astar import reconstruct_path

import pygame

def bfs_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            open_set.put(neighbor)
            
            
        

            open_set.remove(current)

