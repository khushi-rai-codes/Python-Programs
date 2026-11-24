import random
import math


def average_path_length(n):
    if n <= 1:
        return 0.0

    if n == 2:
        return 1.0

    # Harmonic-number approximation.
    harmonic = (
        math.log(n - 1)
        + 0.5772156649
        + 1 / (2 * (n - 1))
        - 1 / (12 * (n - 1) ** 2)
    )

    return 2 * harmonic - 2 * (n - 1) / n


class Node:
    def __init__(self, feature=None, split=None):
        self.feature = feature
        self.split = split
        self.left = None
        self.right = None
        self.size = 0


class IsolationTree:

    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.root = None

    def build(self, data, depth=0):
        node = Node()
        node.size = len(data)

        if len(data) <= 1 or depth >= self.max_depth:
            return node

        features = list(range(len(data[0])))

        valid_features = [
            f for f in features
            if min(row[f] for row in data)
            < max(row[f] for row in data)
        ]

        if not valid_features:
            return node

        feature = random.choice(valid_features)

        minimum = min(row[feature] for row in data)
        maximum = max(row[feature] for row in data)

        split = random.uniform(minimum, maximum)

        left_data = [
            row for row in data
            if row[feature] < split
        ]

        right_data = [
            row for row in data
            if row[feature] >= split
        ]

        if not left_data or not right_data:
            return node

        node.feature = feature
        node.split = split

        node.left = self.build(left_data, depth + 1)
        node.right = self.build(right_data, depth + 1)

        return node

    def fit(self, data):
        self.root = self.build(data)

    def path_length(self, sample):
        node = self.root
        depth = 0

        while node.left is not None and node.right is not None:
            if sample[node.feature] < node.split:
                node = node.left
            else:
                node = node.right

            depth += 1

        return depth + average_path_length(node.size)


class IsolationForest:

    def __init__(self, trees=100, sample_size=64):
        if trees <= 0 or sample_size <= 1:
            raise ValueError("Invalid forest configuration.")

        self.trees = trees
        self.sample_size = sample_size
        self.forest = []
        self.normalizer = 0

    def fit(self, data):
        if not data:
            raise ValueError("Dataset cannot be empty.")

        dimensions = len(data[0])

        if dimensions == 0 or any(
            len(row) != dimensions for row in data
        ):
            raise ValueError("Invalid dataset dimensions.")

        sample_size = min(
            self.sample_size, len(data)
        )

        max_depth = math.ceil(
            math.log2(sample_size)
        )

        self.normalizer = average_path_length(
            sample_size
        )

        if self.normalizer == 0:
            self.normalizer = 1

        self.forest = []

        for _ in range(self.trees):
            sample = random.sample(data, sample_size)

            tree = IsolationTree(max_depth)
            tree.fit(sample)

            self.forest.append(tree)

        return self

    def anomaly_score(self, sample):
        average_length = sum(
            tree.path_length(sample)
            for tree in self.forest
        ) / len(self.forest)

        return 2 ** (
            -average_length / self.normalizer
        )

    def predict(self, sample, threshold=0.65):
        return (
            "ANOMALY"
            if self.anomaly_score(sample) >= threshold
            else "NORMAL"
        )


if __name__ == "__main__":

    random.seed(42)

    data = [
        [random.gauss(10, 1), random.gauss(10, 1)]
        for _ in range(150)
    ]

    data += [
        [random.gauss(30, 1), random.gauss(30, 1)]
        for _ in range(5)
    ]

    model = IsolationForest(
        trees=100,
        sample_size=64
    )

    model.fit(data)

    test_points = [
        [10, 10],
        [11, 9],
        [30, 30],
        [35, 35]
    ]

    print("ISOLATION FOREST RESULTS")
    print("------------------------")

    for point in test_points:
        score = model.anomaly_score(point)

        prediction = model.predict(point)

        print(
            f"Point: {point} | "
            f"Score: {score:.4f} | "
            f"Prediction: {prediction}"
        )
