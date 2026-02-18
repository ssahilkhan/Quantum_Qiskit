from qiskit import QuantumCircuit


def create_bell_state_circuit() -> QuantumCircuit:
    """Create a 2-qubit Bell state circuit."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    return circuit


if __name__ == "__main__":
    qc = create_bell_state_circuit()
    print(qc)
