import copy


class WeightedKet:
    def __init__(self, size, weight):
        self.ket = "0" * size
        self.weight = weight

    def __eq__(self, other):
        return self.ket == other.ket

    def __getitem__(self, index):
        return self.ket[index]

    def __setitem__(self, index, value):
        self.ket = self.ket[:index] + value + self.ket[index + 1 :]


class QuantumState:
    def __init__(self, qubits):
        self.N = qubits
        self.kets = [WeightedKet(self.N, complex(1))]  # |0000...0> to start

    def update_kets(self, new_kets):
        """
        Update the state with the new kets.
        """
        self.kets = new_kets

    def reduce(self):
        """
        Reduce the state to the minimum number of kets.
        """
        # Use a dictionary to combine weights of identical kets
        combined_kets = {}

        for ket in self.kets:
            if ket.weight != 0:
                # Convert the ket state to a tuple to use it as a dictionary key
                ket_key = tuple(ket.ket)
                if ket_key in combined_kets:
                    combined_kets[ket_key].weight += ket.weight
                else:
                    combined_kets[ket_key] = copy.deepcopy(ket)

        # Update self.kets with the combined kets
        self.kets = list(combined_kets.values())

    def __iter__(self):
        for ket in self.kets:
            yield ket
