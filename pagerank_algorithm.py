def pagerank(graph, damping=0.85, tolerance=1e-10,
             max_iterations=1000):

    nodes = list(graph.keys())
    n = len(nodes)

    if n == 0:
        return {}

    if not 0 <= damping < 1:
        raise ValueError("Damping must be between 0 and 1.")

    node_set = set(nodes)

    for node, links in graph.items():
        if not set(links).issubset(node_set):
            raise ValueError(
                f"Unknown destination found in node {node}"
            )

    rank = {node: 1 / n for node in nodes}

    for iteration in range(max_iterations):
        new_rank = {
            node: (1 - damping) / n
            for node in nodes
        }

        dangling_sum = sum(
            rank[node]
            for node in nodes
            if len(graph[node]) == 0
        )

        dangling_contribution = (
            damping * dangling_sum / n
        )

        for node in nodes:
            new_rank[node] += dangling_contribution

        for source in nodes:
            links = graph[source]

            if not links:
                continue

            contribution = (
                damping * rank[source] / len(links)
            )

            for destination in links:
                new_rank[destination] += contribution

        difference = sum(
            abs(new_rank[node] - rank[node])
            for node in nodes
        )

        rank = new_rank

        if difference < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break
    else:
        print("Maximum iterations reached.")

    return rank


def main():
    print("PAGERANK ALGORITHM")
    print("------------------")

    try:
        n = int(input("Enter number of pages: "))

        if n <= 0:
            raise ValueError("Number of pages must be positive.")

        graph = {}

        print("\nUse page names such as A, B, C.")

        for i in range(n):
            page = input(f"Page {i + 1} name: ").strip()

            if not page or page in graph:
                raise ValueError("Page names must be unique.")

            links = input(
                f"Pages linked from {page} (space-separated): "
            ).split()

            graph[page] = links

        damping = float(
            input("\nEnter damping factor (default 0.85): ")
        )

        ranks = pagerank(graph, damping)

        print("\nPAGE RANK RESULTS")
        print("-----------------")

        sorted_ranks = sorted(
            ranks.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for position, (page, score) in enumerate(
            sorted_ranks, start=1
        ):
            print(
                f"{position}. {page}: {score:.8f}"
            )

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
