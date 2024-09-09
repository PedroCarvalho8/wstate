from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi, log2
from qiskit.circuit.library import MCXGate
import os

os.system('cls')

################################################

n: int = 4

################################################

qreg_q = QuantumRegister(2**n, 'q')

circuit = QuantumCircuit(qreg_q)

for i in range(n):
    circuit.h(qreg_q[i])

estados_inicias = [str(bin(i).replace("0b", "")).rjust(2**n, "0") for i in range(2**n)]

estados_unicos = []
for estado in estados_inicias:
    qnt_uns = 0
    for num in estado[-n:]:
        qnt_uns = qnt_uns + 1 if num == '1' else qnt_uns
    if qnt_uns != 1:
        estados_unicos.append({estado: qnt_uns})

for index_estado, estado in enumerate(estados_unicos):
    for key in estado.keys():
        qnts_uns = estado[key] 
        match qnts_uns:

            case 0:
                for bit in range(n):
                    circuit.x(bit)
                circuit.mcx(control_qubits=list(range(n)), target_qubit=n)    
                for bit in range(n):
                    circuit.x(bit)

            case _:
                bits = list(key[:-(n+1):-1])
                circuit.mcx(control_qubits=[int(index) for index, bit in enumerate(bits) if bit == '1'], target_qubit=n+index_estado)
                if sum([int(bit) for bit in bits]) != n:
                    # circuit.mcx(control_qubits=list(range(n)), target_qubit=n+index_estado)
                    bits_vazios = []
                    for index, bit in enumerate(bits):
                        if bit == '0':
                            bits_vazios.append(tuple([index, bit]))
                    for i in range((2**(n-sum([int(bit) for bit in bits]))) - 1):
                        lista_bits = list(range(n))
                        if i == 0:
                            circuit.mcx(control_qubits=lista_bits, target_qubit=n+index_estado)
                        else:
                            try:
                                lista_bits.remove(bits_vazios[i-1][0])
                            except: None
                            circuit.mcx(control_qubits=lista_bits, target_qubit=n+index_estado)

                for index, bit in enumerate(bits):
                    if bit == "1":
                        circuit.cx(control_qubit=n+index_estado, target_qubit=index)           


#####################################

from qiskit_aer import AerSimulator

print(circuit)

circuit.measure_all()
simulador = AerSimulator()
resultado = simulador.run(circuit, shots = 1000).result().get_counts()

print('''
====================================
            ESTADOS
====================================
''')

for estado in sorted([key for key in resultado.keys()]):
    for char in estado:
        if char == '1': print('\033[91m' + char + '\033[0m', end='')
        else : print(char, end='')
    print('\033[90m' + ' : ' , end="")
    print(str(resultado[estado]) + '\033[0m')