from copy import deepcopy
import numpy as np

from lib import TravelingPath
from logger import LogEntry


class SA:
    def __init__(
            self,
            traveling_path: TravelingPath,
            T: float = 10.0,
            cooldown_coefficient: float = 0.95
    ):
        self.traveling_path: TravelingPath = traveling_path
        self.T: float = T
        self.cooldown_coefficient: float = cooldown_coefficient
        self.iteration: int = 0
        self.log: list[LogEntry] = []

    @property
    def probability(self) -> float:
        raw_probability: float = np.exp(-self.traveling_path.distance/self.T)
        return 0.0 if raw_probability < 0.0 else min(abs(raw_probability), 1.0)

    @staticmethod
    def accept(old_probability: float, new_probability: float) -> bool:
        alpha: float = np.random.uniform()
        if alpha < new_probability / old_probability:
            return True
        return False

    def proposal_step(self) -> None:
        idx: tuple[int, int] = np.random.choice(len(self.traveling_path), 2, replace=False)

        old_probability: float = self.probability
        self.traveling_path.swap(idx)
        new_probability: float = self.probability

        if not SA.accept(old_probability, new_probability):
            self.traveling_path.swap(idx)

    def cooldown(self) -> None:
        if self.iteration % 2 == 0:
            self.T *= self.cooldown_coefficient

    def write_log(self) -> None:
        log_entry: LogEntry = LogEntry(
            deepcopy(self.traveling_path),
            self.iteration,
            self.traveling_path.distance,
            self.T
        )
        self.log.append(log_entry)

    def run(self, N: int, debug=False) -> None:
        while self.iteration < N:
            self.iteration += 1
            self.proposal_step()
            self.cooldown()
            self.write_log()
            if debug:
                print(self.log[-1])
