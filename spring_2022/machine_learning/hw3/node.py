from msilib import datasizemask
from turtle import left


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        print(str(self.data))
        try:
            print(str(len(self.left)))
        except:
            print(None)
        try:
            print(str(len(self.right)))
        except:
            print(None)
