import hashlib


def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


class MerkleTree:
    def __init__(self, data_blocks):
        if not data_blocks:
            raise ValueError("At least one data block is required.")

        self.data_blocks = list(data_blocks)
        self.levels = []

        self._build_tree()

    def _build_tree(self):
        current = [
            hash_data(block)
            for block in self.data_blocks
        ]

        self.levels.append(current)

        while len(current) > 1:
            next_level = []

            for i in range(0, len(current), 2):
                left = current[i]

                # Duplicate the final hash when the level has
                # an odd number of elements.
                right = (
                    current[i + 1]
                    if i + 1 < len(current)
                    else left
                )

                next_level.append(
                    hash_data(left + right)
                )

            current = next_level
            self.levels.append(current)

    @property
    def root_hash(self):
        return self.levels[-1][0]

    def get_proof(self, index):
        if not 0 <= index < len(self.data_blocks):
            raise IndexError("Invalid data block index.")

        proof = []
        position = index

        for level in self.levels[:-1]:
            sibling = position ^ 1

            if sibling < len(level):
                proof.append(
                    (level[sibling], sibling < position)
                )
            else:
                proof.append((level[position], False))

            position //= 2

        return proof

    @staticmethod
    def verify(data, proof, expected_root):
        current = hash_data(data)

        for sibling_hash, sibling_is_left in proof:
            if sibling_is_left:
                current = hash_data(
                    sibling_hash + current
                )
            else:
                current = hash_data(
                    current + sibling_hash
                )

        return current == expected_root

    def display(self):
        for level_number, level in enumerate(self.levels):
            print(f"\nLevel {level_number}:")

            for value in level:
                print(value)


def main():
    blocks = [
        "Transaction A",
        "Transaction B",
        "Transaction C",
        "Transaction D",
        "Transaction E"
    ]

    tree = MerkleTree(blocks)

    print("MERKLE TREE")
    tree.display()

    print("\nMerkle Root:")
    print(tree.root_hash)

    index = 2
    proof = tree.get_proof(index)

    print(f"\nVerifying: {blocks[index]}")

    valid = MerkleTree.verify(
        blocks[index],
        proof,
        tree.root_hash
    )

    print("Verification:", "VALID" if valid else "INVALID")

    print("\nTesting modified data:")

    valid = MerkleTree.verify(
        "Modified Transaction",
        proof,
        tree.root_hash
    )

    print("Verification:", "VALID" if valid else "INVALID")


if __name__ == "__main__":
    main()
