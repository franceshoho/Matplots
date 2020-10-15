from random import choice

class RandomWalk:
    """A class to generate points of random walks"""

    def __init__(self, num_points=5000):
        # set default num_points=5000
        self.num_points = num_points
        # initializes 2 lists for x, y values (starting at 0,0)
        self.x_values = [0]
        self.y_values = [0]

    def generate_walks(self):
        """Generates all points in random walks"""
        dir = [1, -1]  # forward or backward
        length = [0, 1, 2, 3, 4]
        while len(self.x_values) < self.num_points:
            x_dir = choice(dir)  # choice takes sequence/list/tuple
            x_step = choice(length)
            x_length = x_dir * x_step

            y_dir = choice(dir)  # choice takes sequence/list/tuple
            y_step = choice(length)
            y_length = y_dir * y_step

            if not (x_length == 0 and y_length == 0):
                # use last stored x, y values to calculate
                x = self.x_values[-1] + x_length
                y = self.y_values[-1] + y_length
                self.x_values.append(x)
                self.y_values.append(y)

    def print_graph(self):
        for i in range(len(self.x_values)):
            print(f'({self.x_values[i]}, {self.y_values[i]})')

