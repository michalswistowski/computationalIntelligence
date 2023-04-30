import matplotlib.pyplot as plt
import random

from aco import AntColony


plt.style.use("dark_background")


COORDS = (
    (20, 52, 100),
    (43, 50, 100),
    (20, 84, 100),
    (70, 65, 100)
)


# def random_coord():
#     r = random.randint(0, len(COORDS))
#     return r


# def plot_nodes(w=12, h=8):
#     for x, y in COORDS:
#         plt.plot(x, y, "g.", markersize=15)
#     plt.axis("off")
#     fig = plt.gcf()
#     fig.set_size_inches([w, h])


# def plot_all_edges():
#     paths = ((a, b) for a in COORDS for b in COORDS)

#     for a, b in paths:
#         plt.plot((a[0], b[0]), (a[1], b[1]))


# plot_nodes()

colony = AntColony(COORDS, ant_count=300, alpha=2, beta=2, 
                    pheromone_evaporation_rate=0.4, pheromone_constant=5000.0,
                    iterations=20)

optimal_nodes = colony.get_path() # najlepszy wynik

# for i in range(len(optimal_nodes) - 1):
#     plt.plot(
#         (optimal_nodes[i][0], optimal_nodes[i + 1][0]),
#         (optimal_nodes[i][1], optimal_nodes[i + 1][1]),
#     )


# plt.show()

# ant_count - 500 - im wyzsza tym bardziej spowalnia iteracje - dluzsze szukanie rozwiazania
# alpha - 0.9 - nie ma znaczacego wplywu na szybkosc 
# beta - 0.1 - nie ma znaczacego wplywu na szybkosc
# pheromone_evaporation_rate - 0.05 - nie ma znaczacego wplywu na szybkosc
# pheromone_constant - 5000 - nie ma znaczacego wplywu na szybkosc
# iterations - 500 - im wyzsza tym dluzej szuka rozwiazania

# mieszanie danych w parametrach nie zmienia zauwazalnie wyniku w porownaniu do pojedynczych parametrow
