#!/usr/bin/env python3

def print_pattern(n: int) -> None:
    """Prints a nxn box outline pattern"""
    for col in range(n):
        for row in range(n):
            if col == 0 or col == n - 1 or row == 0 or row == n - 1:
                print(' * ', end='')
            else:
                print('   ', end='')
        print()
        
