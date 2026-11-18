import random
import math


class AntColony:
    def __init__(
        self,
        distances,
        ants=20,
        iterations=100,
        evaporation=0.5,
        alpha=1.0,
        beta=2.0,
        pheromone_constant=100
    ):
        self.distances = distances
        self.n = len(distances)

        if self.n < 2:
            raise ValueError("At least two cities are required.")

        if any(
            len(row) != self.n
            for row in distances
        ):
            raise ValueError("Distance matrix must be square.")

        if any(
            distances[i][j] < 0
            for i in range(self.n)
            for j in range(self.n)
        ):
            raise ValueError("Distances cannot be negative.")

        if any(
            distances[i][j] != distances[j][i]
            for i in range(self.n)
            for j in range(self.n)
        ):
            raise ValueError("This implementation requires symmetric distances.")

        if any(
            distances[i][j] == 0
            for i in range(self.n)
            for j in range(self.n)
            if i != j
        ):
            raise ValueError("Distinct cities must have positive distances.")

        if ants <= 0 or iterations <= 0:
            raise ValueError("Ants and iterations must be positive.")

        if not 0 < evaporation < 1:
            raise ValueError("Evaporation must be between 0 and 1.")

        if alpha < 0 or beta < 0 or pheromone_constant <= 0:
            raise ValueError("Invalid algorithm parameters.")

        self.ants = ants
        self.iterations = iterations
        self.evaporation = evaporation
        self.alpha = alpha
        self.beta = beta
        self.Q = pheromone_constant

        self.pheromone = [
            [1.0 for _ in range(self.n)]
            for _ in range(self.n)
        ]

    def calculate_distance(self, route):
        return sum(
            self.distances[route[i]][route[i + 1]]
            for i in range(len(route) - 1)
        ) + self.distances[route[-1]][route[0]]

    def select_next_city(self, current, unvisited):
        weights = []

        for city in unvisited:
            pheromone = self.pheromone[current][city]
            heuristic = 1 / self.distances[current][city]

            weight = (
                pheromone ** self.alpha
                * heuristic ** self.beta
            )

            weights.append(weight)

        total = sum(weights)

        if total == 0:
            return random.choice(unvisited)

        probabilities = [weight / total for weight in weights]

        return random.choices(
            list(unvisited),
            weights=probabilities,
            k=1
        )[0]

    def construct_route(self):
        start = random.randrange(self.n)

        route = [start]
        unvisited = set(range(self.n))
        unvisited.remove(start)

        while unvisited:
            next_city = self.select_next_city(
                route[-1], unvisited
            )

            route.append(next_city)
            unvisited.remove(next_city)

        return route

    def update_pheromones(self, routes):
        for i in range(self.n):
            for j in range(self.n):
                self.pheromone[i][j] *= (
                    1 - self.evaporation
                )

        for route, distance in routes:
            deposit = self.Q / distance

            for i in range(self.n):
                a = route[i]
                b = route[(i + 1) % self.n]

                self.pheromone[a][b] += deposit
                self.pheromone[b][a] += deposit

    def optimize(self):
        best_route = None
        best_distance = math.inf

        for iteration in range(self.iterations):
            routes = []

            for _ in range(self.ants):
                route = self.construct_route()
                distance = self.calculate_distance(route)

                routes.append((route, distance))

                if distance < best_distance:
                    best_distance = distance
                    best_route = route[:]

            self.update_pheromones(routes)

            if (iteration + 1) % 10 == 0:
                print(
                    f"Iteration {iteration + 1}: "
                    f"Best distance = {best_distance:.2f}"
                )

        return best_route, best_distance


def main():
    print("ANT COLONY OPTIMIZATION - TSP")

    try:
        n = int(input("Enter number of cities: "))

        if n < 2:
            raise ValueError("At least two cities are required.")

        distances = []

        print("\nEnter the distance matrix:")

        for i in range(n):
            row = list(map(int, input().split()))

            if len(row) != n:
                raise ValueError("Each row must contain n values.")

            distances.append(row)

        colony = AntColony(
            distances,
            ants=20,
            iterations=100,
            evaporation=0.5,
            alpha=1.0,
            beta=2.0
        )

        route, distance = colony.optimize()

        print("\nBEST ROUTE:")

        print(" -> ".join(map(str, route + [route[0]])))

        print(f"Total Distance: {distance:.2f}")

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
