from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        # keep taling steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # decide which directio and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere
            if(x_step == 0 and y_step == 0):
                continue

            # calculate new position
            # self.x_values[-1] = negative referencing -1 is the last value
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)