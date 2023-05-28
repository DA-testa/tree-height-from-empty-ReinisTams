# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    heights = [0] * n

    def calculate_height(node):
        if heights[node] != 0:
            return heights[node]

        parent = parents[node]
        if parent == -1:
            heights[node] = 1
        else:
            heights[node] = calculate_height(parent) + 1

        return heights[node]

    max_height = 0
    for node in range(n):
        height = calculate_height(node)
        max_height = max(max_height, height)

    return max_height


# Read input
n = int(input())
parents = list(map(int, input().split()))

print(compute_height(n, parents))
