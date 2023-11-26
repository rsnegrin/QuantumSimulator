# Quantum Circuit Simulator

## Overview

This repository contains my personal simulator for a quantum circuit capable of handling systems with up to 16 qubits. 
The simulator supports two simulation models:

1. **Matrix Representation:** Optimal for up to 10 qubits.
2. **Ket Representation:** Efficiently tested up to 16 qubits.

## Features

- **Supported Gates:** Includes X, H, T, Tdg, and CX gates.
- **QASM File Input:** Simulates quantum circuits defined in QASM files.
- **Output:** Outputs the final states of the quantum system post-simulation.
- **Easy Mode Switching:** (In Development) Implementing a feature to easily switch between Matrix and Ket representations.
- **Measurements:** (In Development) Working on incorporating quantum measurements.

## Development Status

The Quantum Circuit Simulator is in active development. Current areas of focus include:

- Implementing an easy method to switch between Matrix and Ket representations.
- Adding functionality for quantum measurements.

Additionally, you can run the `test.py` script to execute a series of algorithms. This script also plots the runtime in relation to the number of qubits and lines, providing valuable insights into the simulator's performance.

Your contributions and feedback are invaluable in these areas.

## Usage

To run the simulator, use the following command:

```bash
python simulator.py "filename.qasm"
```
```bash
python test.py "output_filename"
```



