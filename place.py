class Place:
    def __init__(self, address, tuman, mahalla) -> None:
        self._address = address
        self._tuman = tuman
        self._mahalla = mahalla

    @property
    def address(self):
        return self.address

    def toString(self) -> str:
        return f" address --> {self.address} "
    
    def getPlace(self):
        return f" hozirgi address --> {self._address} "