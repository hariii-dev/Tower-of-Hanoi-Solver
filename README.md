# Tower of Hanoi Solver

A clean and efficient Python implementation of the classic mathematical puzzle **Tower of Hanoi**, solved using the recursive approach.

## Problem Description
The puzzle consists of three rods and `n` disks of different diameters. The objective is to move the entire stack to the last rod, obeying the following rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
3. No larger disk may be placed on top of a smaller disk.

The optimal solution requires exactly $2^n - 1$ moves.

## Features
- Tracks and outputs the exact visual state of all three rods (`A`, `B`, `C`) at every single step.
- Implements strict type hinting and clean docstrings.
- Adheres to $O(2^n)$ optimal time complexity.
