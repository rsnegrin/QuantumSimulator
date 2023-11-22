import numpy as np
from Gates import H, X, T, CNOT # Import gates

GATES = {"h": H, 
         "x": X, 
         "t": T,
         'cx': CNOT}

class QuantumCircuit():
    """
    Create a quantum circuit with a given number of qubits and classical bits.
    """
    def __init__(self, qr, cr=0):
        self.qreg = qr # Number of qubits
        self.states = np.array([1] + [0] * (2**(qr)-1)) # Initial state
        self.creg = [0] * cr # Classical register
        self.gates = [] # Gates

    
    def add_gate(self, gate, target, control=None):
        """
        Add a gate to the circuit.
        """
        if control:
            self.gates.append(GATES[gate](self.qreg, control, target))
        else:
            self.gates.append(GATES[gate](self.qreg, target))

    def run(self):
        """
        Run the circuit.
        """
        for gate in self.gates:
            self.states = gate.apply(self.states)
        return self.states

    
    def __str__(self):
        output = "Quantum Circuit:\n"
        output += "Quantum Registers: " + str(self.qreg) + "\n"
        output += "Classical Registers: " + str(self.creg) + "\n"
        output += "Gates:\n"
        for gate in self.gates:
            output += str(gate) + "\n"

        output  += "Total gates: " + str(len(self.gates)) + "\n"
        output += "End of Circuit"
        return output
    


    
if __name__ == "__main__":
    # Create a circuit with 2 qubits
    qc = QuantumCircuit(2)
    # Add a Hadamard gate on qubit 0
    qc.add_gate("cx", 0, 1)
    # Run the circuit
    print(qc.run())
    # Print the circuit
    print(qc)