from collections import defaultdict, deque


def resolve_dependencies(dependencies):
    """
    Each pair (dependency, task) means that dependency
    must be completed before task.
    """

    graph = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()

    for dependency, task in dependencies:
        graph[dependency].append(task)

        nodes.add(dependency)
        nodes.add(task)

        indegree[task] += 1
        indegree[dependency] += 0

    queue = deque(
        sorted(node for node in nodes if indegree[node] == 0)
    )

    order = []

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in sorted(graph[current]):
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != len(nodes):
        return None

    return order


def main():
    dependencies = [
        ("Python", "Flask"),
        ("Python", "Django"),
        ("Flask", "WebApp"),
        ("Django", "WebApp"),
        ("Database", "WebApp"),
        ("WebApp", "Deployment"),
    ]

    result = resolve_dependencies(dependencies)

    if result is None:
        print("Circular dependency detected!")
    else:
        print("Valid dependency resolution order:")

        for position, task in enumerate(result, start=1):
            print(f"{position}. {task}")

    print("\nTesting circular dependencies...")

    cyclic_dependencies = [
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
    ]

    cyclic_result = resolve_dependencies(cyclic_dependencies)

    if cyclic_result is None:
        print("Circular dependency detected successfully.")
    else:
        print("Resolution order:", cyclic_result)


if __name__ == "__main__":
    main()
