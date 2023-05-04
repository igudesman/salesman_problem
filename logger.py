from dataclasses import dataclass

from lib import TravelingPath


@dataclass
class LogEntry:
    def __init__(
            self,
            traveling_path: TravelingPath,
            iteration: int,
            distance: float,
            temperature: float
    ):
        self.traveling_path: TravelingPath = traveling_path
        self.iteration: int = iteration
        self.distance: float = distance
        self.temperature: float = temperature

    def __str__(self) -> str:
        return f'[{self.iteration}. Distance: {self.distance}] ' + '->'.join(
            map(lambda x: str(x), self.traveling_path)
        )
