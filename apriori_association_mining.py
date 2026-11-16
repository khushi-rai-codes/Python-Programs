from itertools import combinations


def generate_candidates(previous_frequent, size):
    candidates = set()

    previous = list(previous_frequent)

    for i in range(len(previous)):
        for j in range(i + 1, len(previous)):
            union = previous[i] | previous[j]

            if len(union) != size:
                continue

            # Every immediate subset must be frequent.
            if all(
                frozenset(subset) in previous_frequent
                for subset in combinations(union, size - 1)
            ):
                candidates.add(union)

    return candidates


def calculate_support(itemset, transactions):
    return sum(
        1 for transaction in transactions
        if itemset.issubset(transaction)
    )


def apriori(transactions, minimum_support):
    item_counts = {}

    for transaction in transactions:
        for item in transaction:
            itemset = frozenset([item])
            item_counts[itemset] = item_counts.get(itemset, 0) + 1

    frequent_itemsets = {}

    current = {
        itemset: count
        for itemset, count in item_counts.items()
        if count >= minimum_support
    }

    size = 1

    while current:
        frequent_itemsets.update(current)

        print(f"\nFrequent itemsets of size {size}:")

        for itemset, count in sorted(
            current.items(),
            key=lambda x: sorted(x[0])
        ):
            print(f"{sorted(itemset)} -> Support count: {count}")

        size += 1

        candidates = generate_candidates(
            set(current.keys()), size
        )

        current = {}

        for candidate in candidates:
            support = calculate_support(candidate, transactions)

            if support >= minimum_support:
                current[candidate] = support

    return frequent_itemsets


def generate_rules(frequent_itemsets, total_transactions,
                   minimum_confidence):
    print("\nAssociation Rules:")

    rules_found = 0

    for itemset, support_count in frequent_itemsets.items():
        if len(itemset) < 2:
            continue

        for size in range(1, len(itemset)):
            for antecedent_tuple in combinations(itemset, size):
                antecedent = frozenset(antecedent_tuple)
                consequent = itemset - antecedent

                antecedent_support = frequent_itemsets.get(
                    antecedent, 0
                )

                if antecedent_support == 0:
                    continue

                confidence = support_count / antecedent_support

                if confidence >= minimum_confidence:
                    support = support_count / total_transactions

                    print(
                        f"{sorted(antecedent)} => "
                        f"{sorted(consequent)}"
                    )

                    print(
                        f"  Support: {support:.3f}, "
                        f"Confidence: {confidence:.3f}"
                    )

                    rules_found += 1

    if rules_found == 0:
        print("No rules satisfy the confidence threshold.")


def main():
    print("APRIORI ASSOCIATION RULE MINING")

    try:
        n = int(input("Number of transactions: "))
        minimum_support = int(input("Minimum support count: "))
        minimum_confidence = float(
            input("Minimum confidence (0 to 1): ")
        )

        if n <= 0 or minimum_support <= 0:
            raise ValueError("Invalid transaction or support count.")

        if minimum_support > n:
            raise ValueError("Minimum support cannot exceed transactions.")

        if not 0 <= minimum_confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1.")

        transactions = []

        print("\nEnter each transaction as space-separated items:")

        for i in range(n):
            items = input(f"Transaction {i + 1}: ").split()

            if not items:
                raise ValueError("Transactions cannot be empty.")

            transactions.append(frozenset(items))

        frequent_itemsets = apriori(
            transactions, minimum_support
        )

        generate_rules(
            frequent_itemsets,
            n,
            minimum_confidence
        )

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
