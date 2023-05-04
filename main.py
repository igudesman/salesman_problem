from lib import get_most_populated_cities, TravelingPath
from optimizer import SA
from visualizer import plot_optimization_run, plot_paths


if __name__ == '__main__':
    top_cities = get_most_populated_cities(30)
    traveling_path = TravelingPath(top_cities)
    sa_optimizer = SA(
        traveling_path=traveling_path,
        T=100.0,
        cooldown_coefficient=0.98
    )
    sa_optimizer.run(1000, debug=False)
    # plot_optimization_run(sa_optimizer.log)
    plot_paths(top_cities, sa_optimizer.log)


# T=100, cool=0.95, N=400
# T=100, cool=0.75, N=70
# T=100, cool=0.98, N=1000