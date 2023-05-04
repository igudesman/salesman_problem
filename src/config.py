T: float = 100.0  # temperature
COOLDOWN: float = 0.95  # cooldown coefficient
N: int = 400  # number of iterations
MODES: list[str] = [
    'OPTIMIZATION_PROCESS_PLOT',
    # 'TRAVELLING_PATHS_PLOT',
]  # determines visualization type
DEBUG: bool = False  # writes debug info if True


# T=100, COOLDOWN=0.95, N=400
# T=100, COOLDOWN=0.75, N=70
# T=100, COOLDOWN=0.98, N=1000
