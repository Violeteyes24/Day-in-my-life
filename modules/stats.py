"""
Module for managing player and game stats.
"""

class GameStats:
    def __init__(self):
        self.energy = 0
        self.focus = 0
        self.distraction = 0
        self.happiness = 0
        self.sadness = 0

    def update_stats(self, energy=0, focus=0, distraction=0, happiness=0, sadness=0):
        self.energy += energy
        self.focus += focus
        self.distraction += distraction
        self.happiness += happiness
        self.sadness += sadness

    def display_stats(self):
        print(f'Energy: {self.energy}')
        print(f'Focus: {self.focus}')
        print(f'Distraction: {self.distraction}')
        print(f'Happiness: {self.happiness}')
        print(f'Sadness: {self.sadness}')
        print()
