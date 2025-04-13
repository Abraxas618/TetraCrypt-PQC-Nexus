# sim/simulate_swarm.py

from node import Node
from ledger import Ledger
from config import SWARM_SIZE, TRUST_THRESHOLD
import time

nodes = [Node(i) for i in range(SWARM_SIZE)]
ledger = Ledger()

# Simulate temporal consensus
for t in range(3):
    print(f"\n⏱️  Timestep {t}")
    for node in nodes:
        ledger.add_block(node.id, node.state, timestamp=time.time())

    for i, n1 in enumerate(nodes):
        for j, n2 in enumerate(nodes):
            if i != j:
                n1.trust_vector[j] = n1.vote_trust(n2.state)

    consensus = sum((n.trust_vector.mean() > TRUST_THRESHOLD) for n in nodes)
    print(f"🧠 Consensus met by {consensus}/{SWARM_SIZE} nodes")
