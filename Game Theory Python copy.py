import numpy as np
import nashpy as nash
import matplotlib.pyplot as plt

# Cold War Payoff Matrices
usa_payoff = np.array([[10, 20],
                       [0, 15]])
ussr_payoff = np.array([[10, 0],
                        [20, 15]])

# Create the game
game = nash.Game(usa_payoff, ussr_payoff)

print("US Payoff Matrix:")
print(usa_payoff)
print("\nUSSR Payoff Matrix:")
print(ussr_payoff)

# Find Nash equilibria
print("\nNash Equilibria (strategy probabilities for US and USSR):")
equilibria = list(game.support_enumeration())
for eq in equilibria:
    print(f"US: {eq[0]}, USSR: {eq[1]}")

# Plot both payoff matrices
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# USA matrix
cax1 = ax1.matshow(usa_payoff, cmap="coolwarm")
ax1.set_title("USA Payoff Matrix", pad=15)
ax1.set_xlabel("USSR Strategy\n(0 = Build, 1 = Not Build)")
ax1.set_ylabel("USA Strategy\n(0 = Build, 1 = Not Build)")
for (i, j), val in np.ndenumerate(usa_payoff):
    ax1.text(j, i, f'{val}', ha='center', va='center', color='black')
fig.colorbar(cax1, ax=ax1)

# USSR matrix
cax2 = ax2.matshow(ussr_payoff, cmap="viridis")
ax2.set_title("USSR Payoff Matrix", pad=15)
ax2.set_xlabel("USSR Strategy\n(0 = Build, 1 = Not Build)")
ax2.set_ylabel("USA Strategy\n(0 = Build, 1 = Not Build)")
for (i, j), val in np.ndenumerate(ussr_payoff):
    ax2.text(j, i, f'{val}', ha='center', va='center', color='white')
fig.colorbar(cax2, ax=ax2)

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Player A (Ron) moves first
G.add_edge("Start", "Ron: Confess", label="Confess")
G.add_edge("Start", "Ron: Not Confess", label="Not Confess")

# Player B (David) responds
G.add_edge("Ron: Confess", "David: Confess (5,5)", label="Confess")
G.add_edge("Ron: Confess", "David: Not Confess (0,10)", label="Not Confess")
G.add_edge("Ron: Not Confess", "David: Confess (10,0)", label="Confess")
G.add_edge("Ron: Not Confess", "David: Not Confess (1,1)", label="Not Confess")

# Positions for clear layout
pos = {
    "Start": (0, 3),
    "Ron: Confess": (-2, 2),
    "Ron: Not Confess": (2, 2),
    "David: Confess (5,5)": (-3, 1),
    "David: Not Confess (0,10)": (-1, 1),
    "David: Confess (10,0)": (1, 1),
    "David: Not Confess (1,1)": (3, 1)
}

# Draw the graph
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2200,
        font_size=10, font_weight='bold', arrows=True)

# Draw edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black", font_size=9)

plt.title("Prisoner's Dilemma Game Tree (Ron & David)", fontsize=14, pad=15)
plt.axis('off')
plt.tight_layout()
plt.show()


