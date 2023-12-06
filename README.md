# Quantum Circuit Simulator

## Overview

This README contains instructions to run my simulator for a quantum circuit.
The simulator supports two simulation models:

1. **Matrix Representation:** Optimal for up to 10 qubits.
2. **Ket Representation:** Efficiently tested up to 16 qubits. This is the default simulation model and is used for all functionalities.

## Important Note

- No easy way has been implemented to switch between the Matrix and Ket simulators. The default is set to the Ket simulator, which works for all functionalities.
- To install necessary packages, run `pip install -r requirements.txt`.

## Features

- **Supported Gates:** Includes X, H, T, Tdg, and CX gates.
- **QASM File Input:** Simulates quantum circuits defined in QASM files.
- **Output:** Outputs the final states of the quantum system post-simulation.

## Results
Additionally, you can run the `test.py` script to execute a series of algorithms. This script also plots the runtime in relation to the number of qubits and lines, providing valuable insights into the simulator's performance.
The algorithms tested for these results are located in the `algorithms` folder. They have varying numbers of qubits and gates, which is why a color gradient is used to represent the number of gates.

**Note:** The matrix representation circuit in this simulator can handle systems up to 13 qubits. Beyond this, the program may crash due to excessive memory usage.

### Quantum Simulation: Matrix Representation

<img src="Results/matrix.png" width="800">

### Quantum Simulation: Ket Representation

<img src="Results/kets.png" width="800">

## Future Work

More optimization is needed and libraries like Pyzx can be used for this purpose.

## Usage

To run the simulator, use the following command:

```bash
python simulator.py "filename.qasm"
```
```bash
python test.py "output_filename"
```



