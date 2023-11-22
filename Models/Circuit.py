

class QuantumCircuit():
    """
    Create a quantum circuit with a given number of qubits and classical bits.
    """
    def __init__(self, qr, cr=0):
        self.qreg = qr
        self.creg = cr
        self.gates = []
    
    def add_gate(self, gate):
        """
        Add a gate to the circuit.
        """
        self.gates.append(gate)


    def run(sefl):
        """
        Run the circuit.
        """
        pass

    
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
    


    
