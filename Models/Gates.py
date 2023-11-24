import numpy as np
from functools import reduce


HELPERS = {"|0><0|": np.array([[1, 0], [0, 0]]),
           "|1><1|": np.array([[0, 0], [0, 1]]),
           "|0><1|": np.array([[0, 1], [0, 0]]),
           "|1><0|": np.array([[0, 0], [1, 0]])}


class SingleQubitGate():
    def __init__(self, name, N, target, gate):
        self.target = target # Target qubit
        self.gate = gate # Type of gate
        self.N = N # Number of qubits
        self._gate_matrix = None
        self.name = name

    @property
    def gate_matrix(self):
        if self._gate_matrix is None:
            if self.N == 1:
                return self.gate
            gate_list = [np.identity(2) if i != self.target else self.gate for i in range(self.N)]
            tensor_product_matrix = reduce(lambda x, y: np.kron(x, y), gate_list)
            self._gate_matrix = tensor_product_matrix
        return self._gate_matrix


    def apply(self, state):
        return np.dot(self.gate_matrix, state)
    
    def __repr__(self):
        return self.name + "[" + str(self.target) + "]"
    

    def __eq__(self, other):
        if isinstance(other, SingleQubitGate):  
            return self.target == other.target and self.name == other.name
        return False

class X(SingleQubitGate):
    def __init__(self, name, N, target):
        gate = np.array([[0, 1], [1, 0]])
        super().__init__(name, N, target, gate)



class H(SingleQubitGate):
    def __init__(self, name, N, target):
        gate = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        super().__init__(name, N, target, gate)


class T(SingleQubitGate):
    def __init__(self, name, N, target):
        gate = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
        super().__init__(name, N, target, gate)


    
class TDG(SingleQubitGate):
    def __init__(self, name, N, target):
        gate = np.array([[1, 0], [0, np.exp(-1j * np.pi / 4)]])
        super().__init__(name, N, target, gate)



class MultiQubitGate():
    def __init__(self, name,  N, control, target, gate):
        self.target = target # Target qubit
        self.control = control # Control qubit
        self.gate = gate # Type of gate
        self.N = N # Number of qubits
        self.name = name
        self._gate_matrix = None

    @property
    def gate_matrix(self):
        if self._gate_matrix is None:
            first_term  = [np.identity(2) if i != self.control else HELPERS["|0><0|"] for i in range(self.N)]
            first_term = reduce(lambda x, y: np.kron(x, y), first_term)

            second_term = [np.identity(2) if i != self.control else HELPERS["|1><1|"] for i in range(self.N)]
            second_term[self.target] = self.gate
            second_term = reduce(lambda x, y: np.kron(x, y), second_term)

            
            matrix = first_term + second_term
            self._gate_matrix = matrix
        return self._gate_matrix
        
    def apply(self, state):
        return np.dot(self.gate_matrix, state)
    
    def __eq__(self, other):
        if isinstance(other, MultiQubitGate):
            return self.target == other.target and self.control == other.control and self.name == other.name
        return False
    
    def __repr__(self) -> str:
        return self.name + "[" + str(self.control) + "," + str(self.target) + "]"

class CNOT(MultiQubitGate):
    def __init__(self, name, N, control, target):
        gate = np.array([[0, 1], [1, 0]])
        super().__init__(name, N, control, target, gate)
