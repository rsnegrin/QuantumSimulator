import subprocess
import time
import matplotlib.pyplot as plt
import sys

files = [
    ("miller_11.qasm", 3, 54),
    ("decod24-v2_43.qasm", 4, 56),
    ("one-two-three-v3_101.qasm", 5, 74),
    ("hwb5_53.qasm", 6, 1340),
    ("alu-bdd_288.qasm", 7, 88),
    ("f2_232.qasm", 8, 1210),
    ("con1_216.qasm", 9, 958),
    ("mini_alu_305.qasm", 10, 177),
    ("wim_266.qasm", 11, 990),
    ("cm152a_212.qasm", 12, 1225),
    ("squar5_261.qasm", 13, 1997),
]
# ("sym6_316.qasm", 14, 274)]
# ("rd84_142.qasm", 15, 347),
# ("cnt3-5_179.qasm", 16, 179)]


# Number of times to run each file
num_runs = 1

# Store runtime, number of qubits, and number of lines
runtimes = []
qubits = []
lines = []


# Function to run the file and measure runtime
def run_file(filename):
    start_time = time.time()
    subprocess.run(
        ["python", "simulator.py", "Algorithms/" + filename], capture_output=True
    )
    return time.time() - start_time


# Test each file multiple times and record the runtimes
for file in files:
    filename, num_qubit, _ = file
    print("Testing", filename)
    total_time = 0
    for _ in range(num_runs):
        total_time += run_file(filename)
    average_time = total_time / num_runs
    runtimes.append(average_time)
    qubits.append(num_qubit)
    print("Average time:", average_time)
    print("--------------------")


# Save a file with the results

filename = sys.argv[1]
with open(f"Results/{filename}.txt", "w") as file:
    for i in range(len(files)):
        file.write(f"{files[i][0]}: {runtimes[i]} s\n")

# Plot runtime vs number of qubits
plt.figure(figsize=(10, 5))
plt.plot(qubits, runtimes, "o-", label="Runtime vs Qubits")
plt.xlabel("Number of Qubits")
plt.ylabel("Runtime (s)")
plt.title("Runtime vs Number of Qubits")
plt.legend()
plt.savefig(f"Results/{filename}.png")
