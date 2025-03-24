import matplotlib.pyplot as plt
from itertools import permutations


class PathOptimizer:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def optimize(self):
        if len(self.points) < 2:
            return []
        best_path = None
        min_dist = float('inf')
        for path in permutations(self.points):
            dist = sum(self.distance(path[i], path[i + 1]) for i in range(len(path) - 1))
            dist += self.distance(path[-1], path[0])  # Return to start
            if dist < min_dist:
                min_dist = dist
                best_path = path
        return list(best_path) + [best_path[0]]

    def plot(self, path):
        x, y = zip(*path)
        plt.plot(x, y, 'bo-')
        plt.title(f"Optimized Path (Distance: {self.total_distance(path):.2f})")
        plt.show()

    def total_distance(self, path):
        return sum(self.distance(path[i], path[i + 1]) for i in range(len(path) - 1))


def main():
    po = PathOptimizer()
    # Sample points
    po.add_point(0, 0)
    po.add_point(1, 3)
    po.add_point(4, 1)
    po.add_point(2, 5)

    path = po.optimize()
    print("Optimized Path:", path)
    po.plot(path)


if __name__ == "__main__":
    main()