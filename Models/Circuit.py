import numpy as np
from .Gates import H, X, T, TDG, CNOT
import time 

class QuantumCircuit():
    """
    Create a quantum circuit with a given number of qubits and classical bits.
    """

    GATES = {"h": H, 
         "x": X, 
         "t": T,
        "tdg": TDG,
         'cx': CNOT}

    def __init__(self, qr, cr=0):
        self.qreg = qr # Number of qubits 
        self.creg = [0] * cr # Classical bits
        self.gates_array = [] # Array of gates
        self.gate_removed = 0 # Number of gates removed by the optimizer
        self.gate_cache = {} # Cache of gates to save memory and time

    def add_gate(self, gate, control=None, target=None):
        """ 
        Add a gate to the circuit.
        """
        if control is not None:
            gateid = gate+str(control)+str(target)
            if not self.gate_cache.get(gateid):
                self.gate_cache[gateid] = self.GATES[gate](gate, self.qreg, control, target)
                self.gates_array.append(self.gate_cache[gateid])
            else:
                self.gates_array.append(self.gate_cache[gateid])
        else:
            gateid = gate+str(target)
            if not self.gate_cache.get(gateid):
                self.gate_cache[gateid] = self.GATES[gate](gate, self.qreg, target)
                self.gates_array.append(self.gate_cache[gateid])
            else:
                self.gates_array.append(self.gate_cache[gateid])

    def run(self):
        """
        Run the circuit.
        """
        start = time.time()
        state = np.array([1] + [0] * (2 ** self.qreg - 1))
        if self.qreg > 13:
            print("Too many qubits, can't run the circuit.")
            return state
        for gate in self.gates_array:
            state = gate.apply(state)

        end = time.time()
        print(f"RUNTIME: {str(end - start)} s")
        return state
    

    # Check this function, is giving wrong results
    def optimize(self):
        """
        Optimize the circuit.
        """
        remove = []
        for i in range(len(self.gates_array)):
            try: 
                if self.gates_array[i] == self.gates_array[i+1]:
                    if i not in remove:
                        remove.append(i)
                    if i+1 not in remove:
                        remove.append(i+1)
            except IndexError:
                pass
        for i in remove:
            self.gates_array.pop(i)
        self.gate_removed += len(remove)

    def __str__(self):
        output = "Quantum Circuit:\n"
        output += "Number of Qubits: " + str(self.qreg) + "\n"
        output  += "Total gates: " + str(len(self.gates_array)) + "\n"
        # output += "Gates removed by optimizer: " + str(self.gate_removed) + "\n"

        return output