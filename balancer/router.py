class RoutingAlgorithm:
    def __init__(self, backends) -> None:
        self.backends = backends
        self.index = 0

        