import math


class GaussianMixtureModel:

    def __init__(self, k=2, iterations=100):
        self.k = k
        self.iterations = iterations
        self.means = []
        self.variances = []
        self.weights = []

    def gaussian(self, x, mean, variance):
        variance = max(variance, 1e-6)

        coefficient = 1 / math.sqrt(
            2 * math.pi * variance
        )

        exponent = math.exp(
            -((x - mean) ** 2) / (2 * variance)
        )

        return coefficient * exponent

    def fit(self, data):
        n = len(data)

        if n < self.k:
            raise ValueError("Not enough data points.")

        if self.k < 1:
            raise ValueError("Number of clusters must be positive.")

        self.means = [
            data[int(i * n / self.k)]
            for i in range(self.k)
        ]

        overall_mean = sum(data) / n

        overall_variance = (
            sum((x - overall_mean) ** 2 for x in data) / n
        )

        self.variances = [
            max(overall_variance, 1e-6)
            for _ in range(self.k)
        ]

        self.weights = [1 / self.k] * self.k

        for _ in range(self.iterations):

            responsibilities = []

            # E-step
            for x in data:
                probabilities = [
                    self.weights[j] *
                    self.gaussian(
                        x,
                        self.means[j],
                        self.variances[j]
                    )
                    for j in range(self.k)
                ]

                total = sum(probabilities)

                if total == 0:
                    raise ArithmeticError(
                        "Numerical underflow during EM."
                    )

                responsibilities.append([
                    p / total for p in probabilities
                ])

            # M-step
            for j in range(self.k):

                cluster_weight = sum(
                    responsibilities[i][j]
                    for i in range(n)
                )

                if cluster_weight < 1e-10:
                    continue

                new_mean = sum(
                    responsibilities[i][j] * data[i]
                    for i in range(n)
                ) / cluster_weight

                new_variance = sum(
                    responsibilities[i][j] *
                    (data[i] - new_mean) ** 2
                    for i in range(n)
                ) / cluster_weight

                self.means[j] = new_mean
                self.variances[j] = max(
                    new_variance, 1e-6
                )

                self.weights[j] = cluster_weight / n

        return self

    def predict(self, x):
        probabilities = [
            self.weights[j] *
            self.gaussian(
                x,
                self.means[j],
                self.variances[j]
            )
            for j in range(self.k)
        ]

        return probabilities.index(max(probabilities))


data = [
    2, 3, 4, 5, 6,
    20, 21, 22, 23, 24,
    3, 4, 5, 21, 22
]

model = GaussianMixtureModel(k=2, iterations=100)
model.fit(data)

print("Gaussian Mixture Model Results")
print("--------------------------------")

for i in range(model.k):
    print(f"Cluster {i}:")
    print("Mean:", round(model.means[i], 3))
    print("Variance:", round(model.variances[i], 3))
    print("Weight:", round(model.weights[i], 3))

print("\nPredictions:")

for value in [3, 5, 21, 23]:
    print(f"{value} -> Cluster {model.predict(value)}")
