import numpy as np

class SingleQubitGate():
    def __init__(self, N, target, gate):
        self.target = target # Target qubit
        self.gate = gate # Type of gate
        self.N = N # Number of qubits

    @property
    def gate_matrix(self):
        if self.N == 1:
            return self.gate
        gate_list = [np.identity(self.N) if i != self.target else self.gate for i in range(self.N)]
        tensor_product_matrix = np.kron(gate_list[0], gate_list[1])
        for i in range(2,self.N):
            tensor_product_matrix = np.kron(tensor_product_matrix, gate_list[i])
        return tensor_product_matrix


    def apply(self, state):
        return np.dot(self.gate_matrix, state)

class X(SingleQubitGate):
    def __init__(self, N, target):
        gate = np.array([[0, 1], [1, 0]])
        super().__init__(N, target, gate)

    def __repr__(self) -> str:
        return "x" + "[" + str(self.target) + "]"

class H(SingleQubitGate):
    def __init__(self, N, target):
        gate = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        super().__init__(N, target, gate)

    def __repr__(self) -> str:
        return "h" + "[" + str(self.target) + "]"


class T(SingleQubitGate):
    def __init__(self, N, target):
        gate = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
        super().__init__(N, target, gate)

    def __repr__(self) -> str:
        return "t" + "[" + str(self.target) + "]"



class MultiQubitGate():
    def __init__(self, N, control, target, gate):
        self.target = target # Target qubit
        self.control = control # Control qubit
        self.gate = gate # Type of gate
        self.N = N # Number of qubits

    @property
    def gate_matrix(self):
        # Need to implement this for non-adjacent qubits
        raise NotImplementedError


class CNOT(MultiQubitGate):
    def __init__(self, N, control, target):
        gate = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1]])
        super().__init__(N, control, target, gate)

    def __repr__(self) -> str:
        return "cx" + "[" + str(self.control) + "," + str(self.target) + "]"
    