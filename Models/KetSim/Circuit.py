import numpy as np
from .Kets import QuantumState
import copy


class QuantumCircuit:
    """
    Create a quantum circuit with a given number of qubits and classical bits.
    """

    def __init__(self, qr, cr=0):
        self.qreg = qr  # Number of qubits
        self.state = QuantumState(qr)
        self.creg = [0] * cr  # Classical bits in state 0
        self.gates_array = []  # Array of gates in order of application
        self.gate_removed = 0  # Number of gates removed by the optimizer
        self.gates = {
            "SQG": {"h": self.h, "x": self.x, "t": self.t, "tdg": self.tdg},
            "MQG": {"cx": self.cx},
        }

    def add_gate(self, gate, control=None, target=None):
        """
        Add a gate to the circuit.
        """
        self.gates_array.append((gate, control, target))

    def run(self):
        """
        Run the circuit.
        """
        for gate in self.gates_array:
            name, control, target = gate
            if name in self.gates["SQG"]:
                self.gates["SQG"][name](target)
            else:
                self.gates["MQG"][name](control, target)
            self.state.reduce()
        return self.final_state()

    def x(self, qubit):
        """
        Apply a Pauli-X gate to a qubit.
        """
        for ket in self.state:
            if ket[qubit] == "0":
                ket[qubit] = "1"
            else:
                ket[qubit] = "0"

    def h(self, qubit):
        """
        Apply a Hadamard gate to a qubit.
        """
        new_states = []
        for ket in self.state:
            ket_zero = copy.deepcopy(ket)
            ket_one = copy.deepcopy(ket)
            ket_zero[qubit] = "0"
            ket_one[qubit] = "1"

            ket_zero.weight /= np.sqrt(2)
            ket_one.weight /= np.sqrt(2)

            if ket[qubit] == "1":
                ket_one.weight *= complex(-1)

            new_states.append(ket_zero)
            new_states.append(ket_one)
        self.state.update_kets(new_states)

    def t(self, qubit):
        """
        Apply a T gate to a qubit.
        """
        for ket in self.state:
            if ket[qubit] == "1":
                ket.weight *= np.exp(1j * np.pi / 4)

    def tdg(self, qubit):
        """
        Apply a T† gate to a qubit.
        """
        for ket in self.state:
            if ket[qubit] == "1":
                ket.weight *= np.exp(-1j * np.pi / 4)

    def cx(self, control, target):
        """
        Apply a CNOT gate to two qubits.
        """
        for ket in self.state:
            if ket[control] == "1":
                if ket[target] == "0":
                    ket[target] = "1"
                else:
                    ket[target] = "0"

    # Check this function, is giving wrong results
    def optimize(self):
        """
        Optimize the circuit.
        """
        pass

    def __str__(self):
        output = "Quantum Circuit:\n"
        output += "Number of Qubits: " + str(self.qreg) + "\n"
        output += "Total gates: " + str(len(self.gates_array)) + "\n"
        # output += "Gates removed by optimizer: " + str(self.gate_removed) + "\n"

        return output

    def final_state(self):
        """
        Return the final state of the circuit.
        """
        self.state.reduce()
        state = np.array([complex(0)] * 2**self.qreg)
        for ket in self.state:
            ket.weight = ket.weight
            value = int(ket.ket, 2)
            state[value] += ket.weight
        return state
