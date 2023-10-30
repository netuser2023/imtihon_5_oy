class InvalidTaxiName(Exception):
    def __init__(self, id) -> None:
        self._id = str(id)
        self.message = self._id + " bu id oldindan kiritilgan "
        super.__init__(self.message)
        