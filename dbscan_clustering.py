import math
from collections import deque


UNVISITED = -2
NOISE = -1


def euclidean_distance(point_a, point_b):
    return math.sqrt(
        sum(
            (a - b) ** 2
            for a, b in zip(point_a, point_b)
        )
    )


def region_query(data, index, epsilon):
    neighbors = []

    for i, point in enumerate(data):
        if euclidean_distance(data[index], point) <= epsilon:
            neighbors.append(i)

    return neighbors


def expand_cluster(data, labels, index, neighbors,
                   cluster_id, epsilon, min_points):

    labels[index] = cluster_id
    queue = deque(neighbors)
    queued = set(neighbors)

    while queue:
        current = queue.popleft()

        if labels[current] == NOISE:
            labels[current] = cluster_id

        if labels[current] != UNVISITED:
            continue

        labels[current] = cluster_id

        current_neighbors = region_query(
            data, current, epsilon
        )

        if len(current_neighbors) >= min_points:
            for neighbor in current_neighbors:
                if neighbor not in queued:
                    queue.append(neighbor)
                    queued.add(neighbor)


def dbscan(data, epsilon, min_points):
    if epsilon <= 0 or min_points <= 0:
        raise ValueError("Parameters must be positive.")

    if not data:
        return []

    dimensions = len(data[0])

    if dimensions == 0:
        raise ValueError("Points cannot have zero dimensions.")

    for point in data:
        if len(point) != dimensions:
            raise ValueError("All points must have equal dimensions.")

        if not all(math.isfinite(x) for x in point):
            raise ValueError("Coordinates must be finite.")

    labels = [UNVISITED] * len(data)
    cluster_id = 0

    for i in range(len(data)):
        if labels[i] != UNVISITED:
            continue

        neighbors = region_query(data, i, epsilon)

        if len(neighbors) < min_points:
            labels[i] = NOISE
            continue

        expand_cluster(
            data,
            labels,
            i,
            neighbors,
            cluster_id,
            epsilon,
            min_points
        )

        cluster_id += 1

    return labels


def main():
    points = [
        [1.0, 1.0],
        [1.2, 1.1],
        [0.8, 0.9],
        [1.1, 0.8],
        [5.0, 5.0],
        [5.2, 5.1],
        [4.8, 4.9],
        [5.1, 4.8],
        [10.0, 10.0]
    ]

    epsilon = 0.6
    min_points = 3

    labels = dbscan(points, epsilon, min_points)

    print("DBSCAN Clustering Results")
    print("-------------------------")

    for point, cluster in zip(points, labels):
        if cluster == NOISE:
            print(f"{point} -> Noise")
        else:
            print(f"{point} -> Cluster {cluster}")

    print("\nTotal clusters:", len(set(labels) - {NOISE}))


if __name__ == "__main__":
    main()
