class Taxi:
    def __init__(self, id) -> None:
        self._id = id

    @property
    def id(self):
        return self.id

    def __str__(self) -> str:
        return f"taksi idsi {self.id}"