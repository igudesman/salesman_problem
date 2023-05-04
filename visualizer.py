from matplotlib import pyplot as plt
import plotly.graph_objects as go

from logger import LogEntry
from lib import City


def plot_optimization_run(logs: list[LogEntry]):
    plt.plot(
        list(map(lambda x: x.iteration, logs)),
        list(map(lambda x: x.distance, logs))
    )
    plt.xlabel('Iteration')
    plt.ylabel('Distance')
    plt.show()


def plot_paths(cities: list[City], logs: list[LogEntry]):
    frames: list[go.Frame] = []
    longitudes: list[float | None] = []
    latitudes: list[float | None] = []

    for log in logs:
        longitudes = []
        latitudes = []
        for i in range(1, len(log.traveling_path) + 1):
            longitudes += [
                log.traveling_path[i - 1].geo_lon,
                log.traveling_path[i % len(log.traveling_path)].geo_lon, None
            ]
            latitudes += [
                log.traveling_path[i - 1].geo_lat,
                log.traveling_path[i % len(log.traveling_path)].geo_lat, None
            ]
        frames.append(
            go.Frame(
                data=go.Scattergeo(
                    lon=longitudes,
                    lat=latitudes,
                    mode='lines',
                    line=dict(width=1, color='red'),
                    opacity=0.5,
                    showlegend=False
                )
            )
        )
        frames[-1]['layout'].update(
            title_text=f''
                       f'Distance: {int(log.distance / log.traveling_path[0].reduction_ratio)}km.; '
                       f'Temperature: {log.temperature}; '
                       f'Iteration: {log.iteration}'
        )

    fig = go.Figure(
        data=[
            go.Scattergeo(
                lon=longitudes,
                lat=latitudes,
                mode='lines',
                line=dict(width=1, color='red'),
                opacity=0.5,
                showlegend=False
            )
        ],
        layout=go.Layout(
            updatemenus=[
                dict(
                    type='buttons',
                    buttons=[
                        dict(
                            label='Play',
                            method='animate',
                            args=[
                                None,
                                {
                                    'frame': {
                                        'duration': 0.01,
                                        'redraw': True
                                    },
                                    'transition': {'duration': 0}
                                }
                            ]
                        )
                    ]
                )
            ]
        ),
        frames=frames
    )

    for city in cities:
        fig.add_trace(
            go.Scattergeo(
                lon=[city.geo_lon],
                lat=[city.geo_lat],
                hoverinfo='text',
                text=city.name,
                marker=dict(
                    size=7,
                    color=hash(city.name) % 256,
                ),
                name=city.name
            )
        )

    fig.update_layout(
        title_text='Solving travelling salesman problem using Simulated Annealing optimization',
        geo=go.layout.Geo(
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
        ),
        height=900,
    )

    fig.show()
