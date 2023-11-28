# Python Crash Course By Eric Matthes
# Chapter 15 Ex 15-4
# Modified Random Walks.py

"""
Modified Random Walks: In the RandomWalk class, x_step and y_step are
generated from the same set of conditions. The direction is chosen randomly
from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. Modify the
values in these lists to see what happens to the overall shape of your walks. Try
a longer list of choices for the distance, such as 0 through 8, or remove the −1
from the x or y direction list
"""

from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])  # Modified direction list
            x_distance = choice([0, 1, 2, 3, 4, 5])  # Modified distance list
            x_step = x_direction * x_distance
            
            y_direction = choice([1])  # Removed -1 from the direction list
            y_distance = choice([0, 1, 2, 3, 4, 5, 6])  # Modified distance list
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)