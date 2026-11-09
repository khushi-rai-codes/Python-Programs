import math
from collections import Counter


def entropy(labels):
    total = len(labels)
    counts = Counter(labels)

    result = 0.0

    for count in counts.values():
        probability = count / total
        result -= probability * math.log2(probability)

    return result


def information_gain(dataset, feature_index):
    labels = [row[-1] for row in dataset]
    initial_entropy = entropy(labels)

    groups = {}

    for row in dataset:
        value = row[feature_index]
        groups.setdefault(value, []).append(row)

    weighted_entropy = 0.0

    for group in groups.values():
        weight = len(group) / len(dataset)
        group_labels = [row[-1] for row in group]

        weighted_entropy += weight * entropy(group_labels)

    return initial_entropy - weighted_entropy


def build_tree(dataset, features):
    labels = [row[-1] for row in dataset]

    # All examples have the same class.
    if len(set(labels)) == 1:
        return labels[0]

    # No features remain.
    if not features:
        return Counter(labels).most_common(1)[0][0]

    best_feature = max(
        features,
        key=lambda index: information_gain(dataset, index)
    )

    tree = {
        "feature": best_feature,
        "branches": {},
        "default": Counter(labels).most_common(1)[0][0]
    }

    remaining_features = [
        index for index in features
        if index != best_feature
    ]

    for value in set(row[best_feature] for row in dataset):
        subset = [
            row for row in dataset
            if row[best_feature] == value
        ]

        tree["branches"][value] = build_tree(
            subset,
            remaining_features
        )

    return tree


def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree

    feature = tree["feature"]
    value = sample[feature]

    branch = tree["branches"].get(value)

    if branch is None:
        return tree["default"]

    return predict(branch, sample)


def main():
    features = [
        "Outlook",
        "Temperature",
        "Humidity",
        "Wind"
    ]

    dataset = [
        ["Sunny", "Hot", "High", "Weak", "No"],
        ["Sunny", "Hot", "High", "Strong", "No"],
        ["Overcast", "Hot", "High", "Weak", "Yes"],
        ["Rain", "Mild", "High", "Weak", "Yes"],
        ["Rain", "Cool", "Normal", "Weak", "Yes"],
        ["Rain", "Cool", "Normal", "Strong", "No"],
        ["Overcast", "Cool", "Normal", "Strong", "Yes"],
        ["Sunny", "Mild", "High", "Weak", "No"],
        ["Sunny", "Cool", "Normal", "Weak", "Yes"],
        ["Rain", "Mild", "Normal", "Weak", "Yes"],
        ["Sunny", "Mild", "Normal", "Strong", "Yes"],
        ["Overcast", "Mild", "High", "Strong", "Yes"],
        ["Overcast", "Hot", "Normal", "Weak", "Yes"],
        ["Rain", "Mild", "High", "Strong", "No"]
    ]

    tree = build_tree(
        dataset,
        list(range(len(features)))
    )

    print("ID3 Decision Tree Classifier")
    print("----------------------------")

    sample = ["Sunny", "Cool", "High", "Strong"]

    prediction = predict(tree, sample)

    print("\nTest sample:")

    for name, value in zip(features, sample):
        print(f"{name}: {value}")

    print("\nPrediction:", prediction)


if __name__ == "__main__":
    main()
