from lib import get_most_populated_cities, TravelingPath
from optimizer import SA
from visualizer import plot_optimization_run, plot_paths
from config import T, N, COOLDOWN, DEBUG, MODES


if __name__ == '__main__':
    top_cities = get_most_populated_cities(30)
    traveling_path = TravelingPath(top_cities)
    sa_optimizer = SA(
        traveling_path=traveling_path,
        T=T,
        cooldown_coefficient=COOLDOWN
    )
    sa_optimizer.run(N=N, debug=DEBUG)

    if 'OPTIMIZATION_PROCESS_PLOT' in MODES:
        plot_optimization_run(sa_optimizer.log)  # to see optimization run
    if 'TRAVELLING_PATHS_PLOT' in MODES:
        plot_paths(top_cities, sa_optimizer.log)  # to see travelling paths with the country outline
