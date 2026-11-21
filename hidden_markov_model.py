class HiddenMarkovModel:
    def __init__(self, states, observations, start, transition, emission):
        self.states = states
        self.observations = observations
        self.start = start
        self.transition = transition
        self.emission = emission

    def forward(self, sequence):
        dp = {}

        for state in self.states:
            dp[state] = (
                self.start[state]
                * self.emission[state][sequence[0]]
            )

        for observation in sequence[1:]:
            new_dp = {}

            for current in self.states:
                probability = sum(
                    dp[previous]
                    * self.transition[previous][current]
                    for previous in self.states
                )

                new_dp[current] = (
                    probability
                    * self.emission[current][observation]
                )

            dp = new_dp

        return sum(dp.values())

    def backward(self, sequence):
        dp = {state: 1.0 for state in self.states}

        for observation in reversed(sequence[1:]):
            new_dp = {}

            for current in self.states:
                new_dp[current] = sum(
                    self.transition[current][next_state]
                    * self.emission[next_state][observation]
                    * dp[next_state]
                    for next_state in self.states
                )

            dp = new_dp

        return sum(
            self.start[state]
            * self.emission[state][sequence[0]]
            * dp[state]
            for state in self.states
        )

    def viterbi(self, sequence):
        dp = {}
        path = {}

        for state in self.states:
            dp[state] = (
                self.start[state]
                * self.emission[state][sequence[0]]
            )
            path[state] = [state]

        for observation in sequence[1:]:
            new_dp = {}
            new_path = {}

            for current in self.states:
                candidates = [
                    (
                        dp[previous]
                        * self.transition[previous][current]
                        * self.emission[current][observation],
                        previous
                    )
                    for previous in self.states
                ]

                best_probability, best_previous = max(candidates)

                new_dp[current] = best_probability
                new_path[current] = (
                    path[best_previous] + [current]
                )

            dp = new_dp
            path = new_path

        best_state = max(dp, key=dp.get)

        return path[best_state], dp[best_state]


states = ["Rainy", "Sunny"]

observations = ["walk", "shop", "clean"]

start = {
    "Rainy": 0.6,
    "Sunny": 0.4
}

transition = {
    "Rainy": {"Rainy": 0.7, "Sunny": 0.3},
    "Sunny": {"Rainy": 0.4, "Sunny": 0.6}
}

emission = {
    "Rainy": {
        "walk": 0.1,
        "shop": 0.4,
        "clean": 0.5
    },
    "Sunny": {
        "walk": 0.6,
        "shop": 0.3,
        "clean": 0.1
    }
}

hmm = HiddenMarkovModel(
    states, observations, start, transition, emission
)

sequence = ["walk", "shop", "clean"]

print("Observation Sequence:", sequence)

print("Forward Probability:",
      hmm.forward(sequence))

print("Backward Probability:",
      hmm.backward(sequence))

best_path, probability = hmm.viterbi(sequence)

print("Most Likely Hidden States:", best_path)
print("Viterbi Probability:", probability)
