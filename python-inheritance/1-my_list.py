#!/usr/bin/python3
"""We will create a class"""


class MyList(list):
    """class from list"""
    def print_sorted(self):
        """Print the list elements in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
