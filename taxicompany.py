from taxi import Taxi
from invalidtaxiname import InvalidTaxiName
from passenger import Passenger
from trip import Trip

class TaxiCompany:
    def __init__(self) -> None:
        self.taxi_list: list[Taxi] = []
        self.trip_list: list[Trip] = []

    def addTaxi(self, id):
        taxi = Taxi(id)
        self.taxi_list.append(taxi)
        print("taxi qo'shildi ")
    

    def taxi(self, taxi: Taxi):
        for _taxi in self.taxi_list:
            if _taxi._id == taxi.id:
                return InvalidTaxiName

    def getAvailable(self):
        pass

    def callTaxi(self, passenge: Passenger, ):
        pass


