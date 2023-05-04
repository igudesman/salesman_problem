import heapq
import csv
from dataclasses import dataclass

import geopy.distance


@dataclass
class City:
    def __init__(self, population, name, geo_lat, geo_lon):
        self.population: str = population
        self.name: str = name
        self.geo_lat: float = geo_lat
        self.geo_lon: float = geo_lon
        self.reduction_ratio: float = 0.0001

    def __str__(self) -> str:
        return self.name

    def distance_to(self, city: 'City') -> float:
        return geopy.distance.geodesic(
            (city.geo_lat, city.geo_lon),
            (self.geo_lat, self.geo_lon),
        ).km * self.reduction_ratio


def get_most_populated_cities(n: int = 30, file_name: str = 'data/city.csv') -> list[City]:
    most_populated_cities: list[str] = []
    with open(file_name, 'r') as file:
        cities = csv.reader(file)
        columns: list[str] = next(cities)
        for row in cities:
            city_data = (
                int(row[columns.index('population')]),
                row[columns.index('city')] if row[columns.index('city')] != '' else row[columns.index('region')],
                float(row[columns.index('geo_lat')]),
                float(row[columns.index('geo_lon')]),
            )
            heapq.heappush(
                most_populated_cities,
                city_data
            )
            if len(most_populated_cities) > n:
                heapq.heappop(most_populated_cities)
    return list(map(
        lambda x: City(*x),
        most_populated_cities
    ))


class TravelingPath:
    def __init__(self, cities: list[City]):
        self.cities: list[City] = cities

    @property
    def distance(self) -> float:
        distance: float = 0.0
        for i in range(1, len(self.cities)):
            distance += self.cities[i].distance_to(self.cities[i-1])
        return distance

    def swap(self, idx: tuple[int, int]) -> 'TravelingPath':
        self.cities[idx[0]], self.cities[idx[1]] = self.cities[idx[1]], self.cities[idx[0]]
        return self

    def __iter__(self):
        return iter(self.cities)

    def __getitem__(self, item):
        return self.cities.__getitem__(item)

    def __len__(self):
        return len(self.cities)
