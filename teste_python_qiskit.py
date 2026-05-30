from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# 1. Cria o circuito (1 qubit e 1 bit clássico)
circuito = QuantumCircuit(1, 1)

# 2. Aplica a porta Hadamard (H). É ela que coloca o qubit em SUPERPOSIÇÃO!
circuito.h(0)

# 3. Mede o qubit
circuito.measure(0, 0)

# --- NOVIDADE: Desenhar o circuito ---
# Esse comando cria a imagem do seu circuito quântico
circuito.draw('mpl')
plt.show() # Abre uma janela mostrando o desenho técnico do seu circuito

# 4. Executa no simulador local
simulador = AerSimulator()
resultado = simulador.run(circuito, shots=1000).result()
contagem = resultado.get_counts()

print("\n--- RESULTADO DA SIMULAÇÃO ---")
print(contagem)
