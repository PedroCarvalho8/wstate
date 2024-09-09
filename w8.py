from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi
from qiskit.circuit.library import C3XGate

qreg_q = QuantumRegister(8, 'q')

circuit = QuantumCircuit(qreg_q)

circuit.h(qreg_q[0])
circuit.h(qreg_q[1])
circuit.h(qreg_q[2])
circuit.ccx(qreg_q[1], qreg_q[2], qreg_q[4])
circuit.append(C3XGate(), [qreg_q[2], qreg_q[0], qreg_q[1], qreg_q[4]])
circuit.ccx(qreg_q[0], qreg_q[2], qreg_q[5])
circuit.append(C3XGate(), [qreg_q[2], qreg_q[0], qreg_q[1], qreg_q[5]])
circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[6])
circuit.append(C3XGate(), [qreg_q[2], qreg_q[0], qreg_q[1], qreg_q[6]])
circuit.append(C3XGate(), [qreg_q[2], qreg_q[0], qreg_q[1], qreg_q[7]])
circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.x(qreg_q[2])
circuit.append(C3XGate(), [qreg_q[1], qreg_q[0], qreg_q[2], qreg_q[3]])
circuit.x(qreg_q[0])
circuit.x(qreg_q[1])
circuit.x(qreg_q[2])
circuit.cx(qreg_q[5], qreg_q[2])
circuit.cx(qreg_q[4], qreg_q[1])
circuit.cx(qreg_q[6], qreg_q[0])
circuit.cx(qreg_q[7], qreg_q[0])
circuit.cx(qreg_q[6], qreg_q[1])
circuit.cx(qreg_q[4], qreg_q[2])
circuit.cx(qreg_q[5], qreg_q[0])
circuit.cx(qreg_q[7], qreg_q[2])
circuit.cx(qreg_q[7], qreg_q[1])

#########################################

import os
from qiskit_aer import AerSimulator

os.system('cls')

circuit.measure_all()
simulador = AerSimulator()
resultado = simulador.run(circuit, shots = 1000).result().get_counts()
print(resultado.keys())

# 000 - q3
# 001 + q0
# 010 + q1
# 011 - q4 -
# 100 + q2
# 101 - q5 -
# 110 - q6 -
# 111 - q7 -